import pytest
from jsonschema import ValidationError, validate

from framework.schemas.booking import BOOKING_ID_LIST_SCHEMA, BOOKING_SCHEMA

BOOKING = {
    "firstname": "Ada",
    "lastname": "Lovelace",
    "totalprice": 175,
    "depositpaid": True,
    "bookingdates": {"checkin": "2025-03-01", "checkout": "2025-03-04"},
    "additionalneeds": "Breakfast",
}


def test_booking_response_matches_contract(booker, booker_request):
    # TODO 1: create BOOKING, GET it back, validate(body, BOOKING_SCHEMA)
    # TODO 2: GET /booking (list) via booker_request, validate against
    #         BOOKING_ID_LIST_SCHEMA
    # TODO 3: build a broken booking (e.g. totalprice="175" or drop lastname)
    #         and assert validate(...) raises ValidationError
    pytest.fail("TODO: implement the steps above, then delete this line")
