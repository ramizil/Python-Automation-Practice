// JSON Schemas + a tiny validator for the restful-booker API.
//
// Why schemas? A value assertion (`expect(body.firstname).toBe('Grace')`) proves
// ONE record looks right today. A schema asserts the *contract*: every field
// exists with the right type. It catches breaking changes (renamed fields, a
// number turned into a string) that value checks miss.
//
// We validate with Ajv (the de-facto JSON Schema validator for JS/TS).
import Ajv, { type Schema } from 'ajv';

const ajv = new Ajv({ allErrors: true });

// Shape of a single booking from GET /booking/{id}.
// restful-booker's GET omits the top-level bookingid, so it is NOT required.
export const bookingSchema = {
  type: 'object',
  required: ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates'],
  properties: {
    firstname: { type: 'string', minLength: 1 },
    lastname: { type: 'string', minLength: 1 },
    totalprice: { type: 'number' }, // reject "150" (string)
    depositpaid: { type: 'boolean' },
    bookingdates: {
      type: 'object',
      required: ['checkin', 'checkout'],
      properties: {
        checkin: { type: 'string' },
        checkout: { type: 'string' },
      },
    },
    additionalneeds: { type: 'string' }, // optional in restful-booker
  },
  additionalProperties: true, // tolerate new fields; set false for strict mode
} as const;

// GET /booking -> array of { bookingid: integer }.
export const bookingIdListSchema = {
  type: 'array',
  items: {
    type: 'object',
    required: ['bookingid'],
    properties: { bookingid: { type: 'integer' } },
  },
} as const;

/**
 * Validate `data` against `schema`. Returns true on success; on failure throws
 * an Error whose message lists every mismatch (handy in test output).
 */
export function validateOrThrow(schema: Schema, data: unknown): boolean {
  const validateFn = ajv.compile(schema);
  if (!validateFn(data)) {
    const details = (validateFn.errors ?? [])
      .map((e) => `${e.instancePath || '(root)'} ${e.message}`)
      .join('; ');
    throw new Error(`Schema validation failed: ${details}`);
  }
  return true;
}
