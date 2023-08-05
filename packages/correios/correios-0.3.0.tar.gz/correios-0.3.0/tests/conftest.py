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


from datetime import datetime, timedelta

import factory
import pytest
from pytest_factoryboy import register

from correios.models.address import Address
from correios.models.posting import TrackingCode
from correios.models.user import FederalTaxNumber, StateTaxNumber, Contract, PostingCard, User


@pytest.fixture
def valid_federal_tax_number():
    return FederalTaxNumber("73.119.555/0001-20")


@pytest.fixture
def valid_state_tax_number():
    return StateTaxNumber("73.119.555/0001-20")


@pytest.fixture
def datetime_object():
    return datetime(1970, 4, 1)


@pytest.fixture
def default_user():
    return User(name="ECT", federal_tax_number="34028316000103", state_tax_number="0733382100116", status_number=1)


# noinspection PyShadowingNames
@pytest.fixture
def default_contract(datetime_object):
    contract = Contract(
        number=9912208555,
        customer_code=279311,
        direction_code=10,
        direction="DR - BRASÍLIA",
        status_code="A",
        start_date=datetime_object,
        end_date=datetime_object + timedelta(days=5),
        posting_cards=[]
    )
    return contract


# noinspection PyShadowingNames
@pytest.fixture
def default_posting_card(default_contract, datetime_object):
    posting_card = PostingCard(
        contract=default_contract,
        number=57018901,
        administrative_code=8082650,
        start_date=datetime_object,
        end_date=datetime_object + timedelta(days=5),
        status=1,
        status_code="I",
        unit=8,
    )

    return posting_card


@pytest.fixture
def tracking_code():
    return TrackingCode(code="PD325270157BR")


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    name = factory.Faker("name", locale="pt_BR")
    street = factory.Faker("street_name", locale="pt_BR")
    number = factory.Faker("building_number", locale="pt_BR")
    city = factory.Faker("city", locale="pt_BR")
    state = factory.Faker("estado_sigla", locale="pt_BR")
    zip_code = factory.Faker("postcode", locale="pt_BR")
    complement = factory.Faker("secondary_address")
    neighborhood = factory.Sequence(lambda n: "Neighborhood #{}".format(n))
    phone = factory.Faker("phone_number", locale="pt_BR")
    cellphone = factory.Faker("phone_number", locale="pt_BR")
    email = factory.Faker("email")
    latitude = factory.Faker("latitude", locale="pt_BR")
    longitude = factory.Faker("longitude", locale="pt_BR")


register(AddressFactory, "sender_address")
register(AddressFactory, "receiver_address")
