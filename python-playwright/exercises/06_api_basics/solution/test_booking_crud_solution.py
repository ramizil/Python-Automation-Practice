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
    create = booker.create_booking(BOOKING)
    assert create.status == 200
    booking_id = create.json()["bookingid"]
    assert create.json()["booking"]["firstname"] == "Alan"

    assert booker.get_booking(booking_id).json()["lastname"] == "Turing"

    booker.auth(**config.BOOKER_ADMIN)
    updated = dict(BOOKING, firstname="Alonzo")
    put = booker.update_booking(booking_id, updated)
    assert put.status == 200
    assert put.json()["firstname"] == "Alonzo"

    assert booker.delete_booking(booking_id).status == 201
    assert booker.get_booking(booking_id).status == 404
