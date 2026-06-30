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
    booking_id = booker.create_booking(BOOKING).json()["bookingid"]
    body = booker.get_booking(booking_id).json()
    validate(instance=body, schema=BOOKING_SCHEMA)

    listing = booker_request.get("/booking", headers={"Accept": "application/json"}).json()
    validate(instance=listing, schema=BOOKING_ID_LIST_SCHEMA)

    broken = dict(BOOKING, totalprice="175")
    del broken["lastname"]
    with pytest.raises(ValidationError):
        validate(instance=broken, schema=BOOKING_SCHEMA)
