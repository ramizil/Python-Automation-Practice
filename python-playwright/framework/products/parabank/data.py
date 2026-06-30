"""Test-data factory for Parabank.

Tests must be independent and repeatable, so each run registers a brand-new
customer with a unique username. ``new_customer`` builds that record.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field


@dataclass
class Customer:
    first_name: str = "Rami"
    last_name: str = "Tester"
    street: str = "1 Test St"
    city: str = "Testville"
    state: str = "CA"
    zip_code: str = "90001"
    phone: str = "5551234567"
    ssn: str = "123-45-6789"
    username: str = field(
        default_factory=lambda: f"rami{int(time.time() * 1000)}{random.randint(100, 999)}"
    )
    password: str = "Test1234!"
    # Filled in after registration (via the API login lookup).
    customer_id: int | None = None


def new_customer() -> Customer:
    return Customer()
