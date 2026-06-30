"""Topic 12 (worked example): layered framework architecture — API.

Layer 1: BaseApiClient (auth + logging interceptor) — product-agnostic.
Layer 2: BookerApiClient (endpoints) + BookerSteps (workflows).
Layer 3: this test — only business steps + assertions.

Run with logs visible to see the Layer-1 interceptor in action:
    pytest tests/api/test_layered_steps.py -s --log-cli-level=INFO
"""

import pytest

from framework import config
from framework.products.booker import BookerApiClient, BookerSteps

pytestmark = pytest.mark.api


def test_booking_lifecycle_via_steps(booker_request):
    client = BookerApiClient(booker_request)  # Layer 2 client on Layer 1 infra
    steps = BookerSteps(client)  # Layer 2 workflows

    booking_id = steps.create_paid_booking("Grace", "Hopper")
    assert client.get(booking_id).status == 200

    steps.cancel_booking(booking_id, config.BOOKER_ADMIN)
    assert client.get(booking_id).status == 404
