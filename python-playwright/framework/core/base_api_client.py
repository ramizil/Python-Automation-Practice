"""Layer 1 — a product-agnostic base API client.

This is the equivalent of a Java HTTP/login *interceptor*: cross-cutting concerns
(auth header injection + request/response logging) live in ONE place. Every
product client (BookerApiClient, a future BillingApiClient, ...) extends this and
gets that behaviour for free, instead of repeating it on every call.

It wraps Playwright's ``APIRequestContext`` and funnels everything through a
single ``call()`` method — the one choke point where the interceptor logic runs.
"""

from __future__ import annotations

from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse

from .logger import get_logger


class BaseApiClient:
    def __init__(self, request: APIRequestContext, *, name: str | None = None) -> None:
        self.request = request
        self.log = get_logger(name or type(self).__name__)
        self._token: str | None = None

    def set_token(self, token: str) -> None:
        """Store an auth token; it is then injected as a cookie on every call."""
        self._token = token

    def _headers(self, extra: dict[str, str] | None = None) -> dict[str, str]:
        # The "interceptor": default JSON headers + auth, merged with per-call extras.
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        if self._token:
            headers["Cookie"] = f"token={self._token}"
        if extra:
            headers.update(extra)
        return headers

    def call(
        self,
        method: str,
        path: str,
        *,
        data: Any | None = None,
        headers: dict[str, str] | None = None,
    ) -> APIResponse:
        self.log.info(">>> %s %s", method.upper(), path)
        resp = self.request.fetch(path, method=method, data=data, headers=self._headers(headers))
        self.log.info("<<< %s %s -> %s", method.upper(), path, resp.status)
        return resp
