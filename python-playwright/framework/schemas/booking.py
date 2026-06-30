"""JSON Schemas (Draft 2020-12) for the restful-booker API.

Why keep schemas here instead of inline in tests?
- Reuse: many tests can validate against the same contract.
- One place to update when the API changes (a single failing schema then
  pinpoints every test that relies on the broken field).
- Readability: the test asserts behaviour; the schema documents the shape.

A JSON Schema describes the *structure* of data: which keys must exist
(``required``), the type of each value (``type``), nested objects, arrays, etc.
``jsonschema.validate(instance, schema)`` raises ``ValidationError`` if the data
doesn't match — that's how we catch a backend that renamed ``totalprice`` to
``price`` or started returning it as a string.
"""

from __future__ import annotations

# Shape of a single booking as returned by GET /booking/{id}.
# Note: restful-booker's GET omits the top-level "bookingid"; that id lives in
# the create/list responses, so it is NOT required here.
BOOKING_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Booking",
    "type": "object",
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
    "properties": {
        "firstname": {"type": "string", "minLength": 1},
        "lastname": {"type": "string", "minLength": 1},
        # totalprice is a number (int or float); reject strings like "150".
        "totalprice": {"type": "number"},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "required": ["checkin", "checkout"],
            "properties": {
                "checkin": {"type": "string"},
                "checkout": {"type": "string"},
            },
        },
        # additionalneeds is optional in restful-booker, so it's not "required".
        "additionalneeds": {"type": "string"},
    },
    # The API may add new keys over time; allowing them keeps tests robust.
    # Flip to False if you want to fail on *any* unexpected field (strict mode).
    "additionalProperties": True,
}

# Shape of GET /booking — an array of objects each carrying an integer id.
BOOKING_ID_LIST_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "BookingIdList",
    "type": "array",
    "items": {
        "type": "object",
        "required": ["bookingid"],
        "properties": {"bookingid": {"type": "integer"}},
    },
}
