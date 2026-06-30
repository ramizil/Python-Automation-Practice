// Test-data factory for Parabank. Each run registers a unique customer so tests
// stay independent and repeatable.
export interface Customer {
  firstName: string;
  lastName: string;
  street: string;
  city: string;
  state: string;
  zipCode: string;
  phone: string;
  ssn: string;
  username: string;
  password: string;
  customerId?: number; // filled after registration via the API login lookup
}

export function newCustomer(): Customer {
  const username = `rami${Date.now()}${Math.floor(Math.random() * 900 + 100)}`;
  return {
    firstName: 'Rami',
    lastName: 'Tester',
    street: '1 Test St',
    city: 'Testville',
    state: 'CA',
    zipCode: '90001',
    phone: '5551234567',
    ssn: '123-45-6789',
    username,
    password: 'Test1234!',
  };
}
