"""Thin client for the restful-booker API, built on Playwright's
``APIRequestContext``.

restful-booker quirks worth knowing:
- ``POST /auth`` returns a ``token`` you must send as a cookie to update/delete.
- Write endpoints want ``Content-Type: application/json`` and
  ``Accept: application/json``.
- ``DELETE`` returns ``201 Created`` (not 200/204) on success.
"""

from __future__ import annotations

from typing import Any

from playwright.sync_api import APIRequestContext


class BookerClient:
    def __init__(self, request: APIRequestContext) -> None:
        self.request = request
        self._token: str | None = None

    # ---- auth ---- #
    def auth(self, username: str, password: str) -> str:
        resp = self.request.post("/auth", data={"username": username, "password": password})
        assert resp.ok, f"auth failed: {resp.status} {resp.text()}"
        token: str = resp.json()["token"]
        self._token = token
        return token

    @property
    def _auth_headers(self) -> dict[str, str]:
        if not self._token:
            raise RuntimeError("Call auth() before update/delete.")
        return {
            "Cookie": f"token={self._token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    # ---- bookings ---- #
    def create_booking(self, booking: dict[str, Any]):
        return self.request.post(
            "/booking",
            data=booking,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )

    def get_booking(self, booking_id: int):
        return self.request.get(f"/booking/{booking_id}", headers={"Accept": "application/json"})

    def update_booking(self, booking_id: int, booking: dict[str, Any]):
        return self.request.put(f"/booking/{booking_id}", data=booking, headers=self._auth_headers)

    def delete_booking(self, booking_id: int):
        return self.request.delete(f"/booking/{booking_id}", headers=self._auth_headers)
