"""Topic 7 (worked example): API schema / contract validation.

Value assertions ("firstname == Grace") prove ONE record is right today.
Schema assertions prove the *contract* still holds: every field exists and has
the right type. They catch breaking changes (renamed/removed fields, a number
turned into a string) that value checks miss.

    pytest tests/api/test_booker_schema.py
"""

import pytest
from jsonschema import ValidationError, validate

from framework.schemas.booking import BOOKING_ID_LIST_SCHEMA, BOOKING_SCHEMA

pytestmark = pytest.mark.api


BOOKING = {
    "firstname": "Grace",
    "lastname": "Hopper",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"},
    "additionalneeds": "Breakfast",
}


def test_created_booking_matches_schema(booker):
    booking_id = booker.create_booking(BOOKING).json()["bookingid"]

    body = booker.get_booking(booking_id).json()
    # Raises jsonschema.ValidationError (failing the test) if the shape is wrong.
    validate(instance=body, schema=BOOKING_SCHEMA)


def test_booking_list_matches_schema(booker_request):
    body = booker_request.get("/booking", headers={"Accept": "application/json"}).json()
    validate(instance=body, schema=BOOKING_ID_LIST_SCHEMA)


def test_schema_rejects_bad_shape():
    # Demonstrates the schema actually has teeth: totalprice as a string and a
    # missing lastname must both fail validation.
    broken = dict(BOOKING, totalprice="150")
    del broken["lastname"]
    with pytest.raises(ValidationError):
        validate(instance=broken, schema=BOOKING_SCHEMA)
