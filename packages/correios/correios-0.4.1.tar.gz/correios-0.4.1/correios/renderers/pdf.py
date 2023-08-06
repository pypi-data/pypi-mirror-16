# Copyright 2016 Osvaldo Santana Neto
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from io import BytesIO
from typing import List

from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.lib import colors, pagesizes
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Flowable, Paragraph, Table, TableStyle

from correios.exceptions import RendererError
from correios.models.data import EXTRA_SERVICE_AR, EXTRA_SERVICE_MP, EXTRA_SERVICE_VD
from correios.models.posting import ShippingLabel, PostingList
from correios.models.user import ExtraService

VERTICAL_SECURITY_MARGIN = 6  # pt


class PDF:
    def __init__(self, page_size):
        self._file = BytesIO()
        self.canvas = Canvas(self._file, pagesize=page_size)
        self._saved = False

    @property
    def file(self) -> BytesIO:
        if not self._saved:
            self.canvas.save()
            self._saved = True

        self._file.seek(0)
        return self._file

    def save(self, filename):
        with open(filename, "wb") as pdf_file:
            pdf_file.write(self.file.read())

    def __bytes__(self):
        return self.file.getvalue()


class ShippingLabelFlowable(Flowable):
    def __init__(self, shipping_label: ShippingLabel, label_width, label_height, hmargin=5 * mm, vmargin=5 * mm):
        super().__init__()
        self.shipping_label = shipping_label

        self.label_width = label_width
        self.hmargin = hmargin
        self.width = self.label_width - (2 * hmargin)

        self.label_height = label_height
        self.vmargin = vmargin
        self.height = self.label_height - (2 * vmargin)

        self.x1 = self.hmargin
        self.y1 = self.vmargin
        self.x2 = self.hmargin + self.width
        self.y2 = self.vmargin + self.height

    def wrap(self, *args):
        return self.label_width, self.label_height

    def draw(self):
        canvas = self.canv
        canvas.setLineWidth(0.1)

        # logo
        logo = ImageReader(self.shipping_label.logo)
        canvas.drawImage(logo, self.x1 + 5 * mm, self.y2 - (27 * mm), width=25 * mm,
                         preserveAspectRatio=True, anchor="sw", mask="auto")

        # datagrid
        datagrid = createBarcodeDrawing("ECC200DataMatrix",
                                        value=self.shipping_label.get_datamatrix_info(),
                                        width=25 * mm, height=25 * mm)
        datagrid.drawOn(canvas, self.x1 + 40 * mm, self.y2 - (27 * mm))

        # symbol
        symbol = ImageReader(self.shipping_label.symbol)
        canvas.drawImage(symbol, self.x1 + 70 * mm, self.y2 - (27 * mm), width=25 * mm,
                         preserveAspectRatio=True, anchor="sw", mask="auto")

        # header shipping_labels
        label_style = ParagraphStyle(name="label", fontName="Helvetica", fontSize=7, leading=8)
        text = Paragraph("{}<br/>{}".format(self.shipping_label.get_invoice(),
                                            self.shipping_label.get_order()),
                         style=label_style)
        text.wrap(25 * mm, 14)
        text.drawOn(canvas, self.x1 + 5 * mm, self.y2 - (28 * mm) - 14)

        text = Paragraph("{}<br/>{}".format(self.shipping_label.get_contract_number(),
                                            self.shipping_label.get_service_name()),
                         style=label_style)
        text.wrap(25 * mm, 14)
        text.drawOn(canvas, self.x1 + 40 * mm, self.y2 - (28 * mm) - 14)

        text = Paragraph("{}<br/>{}".format(self.shipping_label.get_package_sequence(),
                                            self.shipping_label.get_weight()),
                         style=label_style)
        text.wrap(25 * mm, 14)
        text.drawOn(canvas, self.x1 + 70 * mm, self.y2 - (28 * mm) - 14)

        # tracking
        canvas.setFont("Helvetica-Bold", 10)
        canvas.drawCentredString(self.x1 + 42.5 * mm, self.y2 - 40 * mm,
                                 self.shipping_label.get_tracking_code())
        code = createBarcodeDrawing("Code128", value=str(self.shipping_label.tracking_code),
                                    width=75 * mm, height=18 * mm, quiet=0)
        code.drawOn(canvas, 10 * mm, self.y2 - (59 * mm))

        # extra services (first three)
        first_row = self.y2 - (40 * mm) - 10  # font-size=10pt
        for extra_service in self.shipping_label.extra_services:
            canvas.drawString(self.x2 - (10 * mm), first_row, extra_service.code)
            first_row -= 14

        # receipt
        receipt_style = ParagraphStyle(name="label", fontName="Helvetica", fontSize=8, leading=14)
        text = Paragraph(self.shipping_label.receipt_template, style=receipt_style)
        text.wrap(self.width - (10 * mm), 28)
        text.drawOn(canvas, self.x1 + (5 * mm), self.y2 - (60 * mm) - 28)

        # sender header
        canvas.setFillColor(colors.black)
        canvas.line(self.x1, self.y2 - (70 * mm), self.x2, self.y2 - (70 * mm))
        width = stringWidth(self.shipping_label.sender_header, "Helvetica", 10) + 2
        canvas.rect(self.x1, self.y2 - (70 * mm) - 14, width, 14, fill=True)

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.white)
        canvas.drawString(self.x1 + 4, self.y2 - (70 * mm) - 10, self.shipping_label.sender_header)

        carrier_logo = ImageReader(self.shipping_label.carrier_logo)
        canvas.drawImage(carrier_logo, self.x2 - 20 * mm, self.y2 - (70 * mm) - 12, height=10,
                         preserveAspectRatio=True, anchor="sw", mask="auto")

        # receiver
        receiver_style = ParagraphStyle("receiver", fontName="Helvetica", fontSize=10, leading=15)
        text = Paragraph(self.shipping_label.get_receiver_data(), style=receiver_style)
        text.wrap(self.width, 22 * mm)
        text.drawOn(canvas, self.x1 + 5 * mm, self.y2 - (98 * mm))

        # receiver zip barcode
        code = createBarcodeDrawing("Code128", value=str(self.shipping_label.receiver.zip_code),
                                    width=50 * mm, height=18 * mm, quiet=0)
        code.drawOn(canvas, self.x1 + 5 * mm, self.y2 - (117 * mm))

        # text
        text_style = ParagraphStyle("text", fontName="Helvetica", fontSize=10)
        text = Paragraph(self.shipping_label.text, style=text_style)
        width = self.x2 - (self.x1 + (45 * mm))
        text.wrap(width, 18 * mm)
        text.breakLines(width)
        text.drawOn(canvas, self.x1 + (45 * mm), self.y2 - (98 * mm))

        # sender
        canvas.line(self.x1, self.y2 - (118 * mm), self.x2, self.y2 - (118 * mm))
        sender_style = ParagraphStyle("sender", fontName="Helvetica", fontSize=9)
        text = Paragraph(self.shipping_label.get_sender_data(), style=sender_style)
        text.wrap(self.width, 22 * mm)
        text.drawOn(canvas, self.x1 + 5 * mm, self.y1 + 2 * mm)

        # border
        canvas.rect(self.x1, self.y1, self.width, self.height)


class PostingReportPDFRenderer:
    def __init__(self, page_size=pagesizes.A4, shipping_labels_margin=(0, 0), posting_list_margin=(5 * mm, 5 * mm)):
        self.shipping_labels = []  # type: List[ShippingLabel]
        self._tracking_codes = set()

        self.page_size = page_size
        self.page_width = page_size[0]
        self.page_height = page_size[1]

        self.posting_list = None  # type: PostingList
        self.posting_list_margin = posting_list_margin

        self.shipping_labels_margin = shipping_labels_margin
        self.shipping_labels_width = self.page_width - (2 * shipping_labels_margin[0])
        self.shipping_labels_height = self.page_height - (2 * shipping_labels_margin[1])

        self.col_size = self.shipping_labels_width / 2
        self.row_size = self.shipping_labels_height / 2
        self._label_position = (
            (shipping_labels_margin[0], self.page_height / 2),
            (shipping_labels_margin[0] + self.col_size, self.page_height / 2),
            (shipping_labels_margin[0], shipping_labels_margin[1]),
            (shipping_labels_margin[0] + self.col_size, shipping_labels_margin[1]),
        )

    def set_posting_list(self, posting_list: PostingList):
        if not posting_list.closed:
            raise RendererError("Cannot render an open posting list")

        self.posting_list = posting_list
        for shipping_label in posting_list.shipping_labels.values():
            self.add_shipping_label(shipping_label)

    def add_shipping_label(self, shipping_label: ShippingLabel):
        if shipping_label in self.shipping_labels:
            raise RendererError("Shipping Label {!s} already added".format(shipping_label.tracking_code))
        self.shipping_labels.append(shipping_label)

    def draw_grid(self, canvas):
        canvas.setLineWidth(0.2)
        canvas.setStrokeColor(colors.gray)
        canvas.line(self.shipping_labels_margin[0],
                    self.page_height / 2,
                    self.shipping_labels_width + self.shipping_labels_margin[0],
                    self.page_height / 2)
        canvas.line(self.page_width / 2,
                    self.shipping_labels_margin[1],
                    self.page_width / 2,
                    self.shipping_labels_height + self.shipping_labels_margin[1])

    def render_posting_list(self, pdf=None) -> PDF:
        if pdf is None:
            pdf = PDF(self.page_size)
        canvas = pdf.canvas

        width = self.page_width - (2 * self.posting_list_margin[0])
        height = self.page_height - (2 * self.posting_list_margin[1])

        x1, y1 = self.posting_list_margin[0], self.posting_list_margin[1]
        x2, y2 = width + self.posting_list_margin[0], height + self.posting_list_margin[1]
        label_style = ParagraphStyle(name="label", fontName="Helvetica", fontSize=8, leading=5 * mm)

        # logo
        logo = ImageReader(self.posting_list.logo)
        canvas.drawImage(logo, x1, y2 - 10.3 * mm, height=8 * mm,
                         preserveAspectRatio=True, anchor="sw", mask="auto")

        # head1
        canvas.setFont("Helvetica-Bold", size=14)
        canvas.drawCentredString(x2 - ((width - 40 * mm) / 2), y2 - 9 * mm,
                                 "Empresa Brasileira de Correios e Telégrafos".upper())

        # box
        canvas.setLineWidth(0.5)
        canvas.rect(x1, y2 - 45 * mm, width, 30 * mm)
        canvas.drawCentredString(x1 + width / 2, y2 - (15 * mm) - 15, "Lista de Postagem".upper())

        # header info
        spacer = 5 * mm
        col_width = width / 4

        col = 0
        header_label = ("<b>N° da Lista:</b> {!s}<br/>"
                        "<b>Contrato:</b> {!s}<br/>"
                        "<b>Cód. Administrativo:</b> {!s}<br/>"
                        "<b>Cartão:</b> {!s}")
        header = header_label.format(self.posting_list.number,
                                     self.posting_list.contract,
                                     self.posting_list.posting_card.administrative_code,
                                     self.posting_list.posting_card)
        text = Paragraph(header, style=label_style)
        text.wrap(col_width, 30 * mm)
        text.drawOn(canvas, x1 + spacer + col * col_width, y2 - (43 * mm))

        col = 1
        header_label = ("<b>Remetente:</b> {!s}<br/>"
                        "<b>Cliente:</b> {!s}<br/>"
                        "<b>Endereço:</b> {!s}<br/>"
                        "{!s}")
        header = header_label.format(self.posting_list.sender.name,
                                     self.posting_list.contract.customer_name[:30],
                                     self.posting_list.sender.display_address[0],
                                     self.posting_list.sender.display_address[1])
        text = Paragraph(header, style=label_style)
        text.wrap(col_width * 2, 30 * mm)
        text.drawOn(canvas, x1 + spacer + col * col_width, y2 - (43 * mm))

        col = 3
        header_label = "<b>Telefone:</b> {!s}<br/>"
        header = header_label.format(self.posting_list.sender.phone.display())
        text = Paragraph(header, style=label_style)
        text.wrap(col_width, 30 * mm)
        text.drawOn(canvas, x1 + spacer + col * col_width, y2 - (43 * mm))

        code = createBarcodeDrawing("Code128", value=str(self.posting_list.number),
                                    width=col_width * 0.6, height=10 * mm, quiet=0)
        code.drawOn(canvas, x1 + spacer + col * col_width, y2 - (35 * mm))

        # table
        style = [
            ('FONTNAME', (0, 0), (-1, -1), "Courier"),
            ('FONTNAME', (0, 0), (-1, 0), "Courier-Bold"),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('ALIGN', (6, 1), (6, -1), "RIGHT"),
        ]

        table = [
            ("Nº do Objeto", "CEP", "Peso", "AR", "MP", "VD",
             Paragraph("Valor<br/>Declarado", style=ParagraphStyle(name="th",
                                                                   fontName="Courier-Bold",
                                                                   fontSize=8,
                                                                   alignment=TA_CENTER)),
             "Nota Fiscal", "Volume", "Destinatário"),
        ]
        for i, shipping_label in enumerate(self.shipping_labels, start=1):
            row = (
                str(shipping_label.tracking_code),
                str(shipping_label.receiver.zip_code),
                str(shipping_label.package.posting_weight),
                "S" if ExtraService.get(EXTRA_SERVICE_AR) in shipping_label else "N",
                "S" if ExtraService.get(EXTRA_SERVICE_MP) in shipping_label else "N",
                "S" if ExtraService.get(EXTRA_SERVICE_VD) in shipping_label else "N",
                str(shipping_label.value).replace(".", ","),
                str(shipping_label.invoice_number),
                shipping_label.get_package_sequence(),
                shipping_label.receiver.name[:40],
            )
            # noinspection PyTypeChecker
            table.append(row)

            if i % 2:
                style.append(('BACKGROUND', (0, i), (-1, i), colors.lightgrey))

        table_flow = Table(
            table,
            colWidths=(25 * mm, 15 * mm, 10 * mm, 6 * mm, 6 * mm, 6 * mm, 20 * mm, 20 * mm, 20 * mm, width - 128 * mm),
            style=TableStyle(style),
        )
        w, h = table_flow.wrap(0, 0)
        table_flow.drawOn(canvas, x1, y2 - h - 50 * mm)

        # debug
        canvas.setStrokeColor(colors.red)
        # canvas.rect(x1 + 40 * mm, y2 - (10.3 * mm), width - 40 * mm, 8 * mm)
        # canvas.line(x1, y2 - 10 * mm, x2, y2 - 10 * mm)

        canvas.showPage()
        return pdf

    def render_labels(self, pdf=None) -> PDF:
        if pdf is None:
            pdf = PDF(self.page_size)

        canvas = pdf.canvas

        position = len(self._label_position) - 1
        for i, shipping_label in enumerate(self.shipping_labels):
            position = i % len(self._label_position)
            self.render_label(shipping_label, position, pdf)
            if position == len(self._label_position) - 1:
                self.draw_grid(canvas)
                canvas.showPage()

        if position != len(self._label_position) - 1:
            self.draw_grid(canvas)
            canvas.showPage()

        return pdf

    def render_label(self, shipping_label: ShippingLabel, position=0, pdf=None) -> PDF:
        single_label = pdf is None
        if single_label:
            pdf = PDF(self.page_size)

        canvas = pdf.canvas
        label = ShippingLabelFlowable(shipping_label, self.col_size, self.row_size)
        label.drawOn(pdf.canvas, *self._label_position[position])

        if single_label:
            self.draw_grid(canvas)
            canvas.showPage()

        return pdf

    def render(self) -> PDF:
        pdf = PDF(self.page_size)
        self.render_posting_list(pdf)
        self.render_labels(pdf)
        return pdf
