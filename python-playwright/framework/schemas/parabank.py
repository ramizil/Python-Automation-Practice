"""JSON Schemas for Parabank's REST API (used by the capstone, topic 11)."""

from __future__ import annotations

ACCOUNT_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ParabankAccount",
    "type": "object",
    "required": ["id", "customerId", "type", "balance"],
    "properties": {
        "id": {"type": "integer"},
        "customerId": {"type": "integer"},
        "type": {"type": "string", "enum": ["CHECKING", "SAVINGS", "LOAN"]},
        "balance": {"type": "number"},
    },
    "additionalProperties": True,
}

ACCOUNTS_LIST_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ParabankAccountList",
    "type": "array",
    "items": ACCOUNT_SCHEMA,
}

TRANSACTION_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ParabankTransaction",
    "type": "object",
    "required": ["id", "accountId", "type", "amount"],
    "properties": {
        "id": {"type": "integer"},
        "accountId": {"type": "integer"},
        "type": {"type": "string"},
        "amount": {"type": "number"},
        "description": {"type": "string"},
    },
    "additionalProperties": True,
}

TRANSACTIONS_LIST_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ParabankTransactionList",
    "type": "array",
    "items": TRANSACTION_SCHEMA,
}
