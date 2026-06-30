"""Topic 6 (worked example): API testing basics against restful-booker.

Covers: auth token, create, read, update (auth'd), delete (auth'd).
    pytest tests/api/test_booker.py
"""
import pytest

from framework import config
from framework.api.booker_client import BookerClient

pytestmark = pytest.mark.api


NEW_BOOKING = {
    "firstname": "Grace",
    "lastname": "Hopper",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"},
    "additionalneeds": "Breakfast",
}


def test_health_check(booker_request):
    # restful-booker exposes /ping for a simple 201 health check.
    resp = booker_request.get("/ping")
    assert resp.status == 201


def test_create_and_read_booking(booker: BookerClient):
    create = booker.create_booking(NEW_BOOKING)
    assert create.status == 200
    body = create.json()
    booking_id = body["bookingid"]
    assert body["booking"]["firstname"] == "Grace"

    read = booker.get_booking(booking_id)
    assert read.status == 200
    assert read.json()["lastname"] == "Hopper"


def test_update_requires_auth_then_succeeds(booker: BookerClient):
    booking_id = booker.create_booking(NEW_BOOKING).json()["bookingid"]

    booker.auth(**config.BOOKER_ADMIN)
    updated = dict(NEW_BOOKING, firstname="Ada", totalprice=999)
    resp = booker.update_booking(booking_id, updated)
    assert resp.status == 200
    assert resp.json()["firstname"] == "Ada"
    assert resp.json()["totalprice"] == 999


def test_delete_booking(booker: BookerClient):
    booking_id = booker.create_booking(NEW_BOOKING).json()["bookingid"]
    booker.auth(**config.BOOKER_ADMIN)

    resp = booker.delete_booking(booking_id)
    assert resp.status == 201  # restful-booker returns 201 on delete

    # It should now be gone (404).
    assert booker.get_booking(booking_id).status == 404
