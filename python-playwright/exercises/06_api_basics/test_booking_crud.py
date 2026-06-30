import pytest

from framework import config
from framework.api.booker_client import BookerClient

BOOKING = {
    "firstname": "Alan",
    "lastname": "Turing",
    "totalprice": 200,
    "depositpaid": True,
    "bookingdates": {"checkin": "2025-06-01", "checkout": "2025-06-10"},
    "additionalneeds": "Late checkout",
}


def test_booking_crud_lifecycle(booker: BookerClient):
    # TODO 1: create the BOOKING, assert status 200 + firstname echoed back
    # TODO 2: GET it back, assert lastname == "Turing"
    # TODO 3: auth as admin, PUT an update (e.g. firstname -> "Alonzo"), assert it
    # TODO 4: DELETE it (expect 201), then GET should be 404
    pytest.fail("TODO: implement, then delete this line")
