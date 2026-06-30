"""Layer 2 — restful-booker business steps.

Workflows a test cares about ("create a paid booking", "cancel a booking"),
composed from the BookerApiClient. Tests call these and assert outcomes.
"""

from __future__ import annotations

from .client import BookerApiClient


class BookerSteps:
    def __init__(self, client: BookerApiClient) -> None:
        self.client = client

    def create_paid_booking(self, firstname: str, lastname: str, *, total: int = 150) -> int:
        booking = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": total,
            "depositpaid": True,
            "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"},
            "additionalneeds": "Breakfast",
        }
        resp = self.client.create(booking)
        return resp.json()["bookingid"]

    def cancel_booking(self, booking_id: int, admin: dict[str, str]) -> None:
        # Cancelling needs auth — the client handles token injection for us.
        self.client.auth(**admin)
        self.client.delete(booking_id)
