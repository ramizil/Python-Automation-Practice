// Central test configuration: target URLs and demo credentials.
// Override any URL with an environment variable (e.g. SAUCEDEMO_URL=...).

export const URLS = {
  saucedemo: process.env.SAUCEDEMO_URL ?? 'https://www.saucedemo.com',
  bookerApi: process.env.BOOKER_API_URL ?? 'https://restful-booker.herokuapp.com',
  dummyjson: process.env.DUMMYJSON_URL ?? 'https://dummyjson.com',
  parabank: process.env.PARABANK_URL ?? 'https://parabank.parasoft.com/parabank',
};

export const SAUCE_PASSWORD = 'secret_sauce';

export const SAUCE_USERS = {
  standard: 'standard_user',
  lockedOut: 'locked_out_user',
  problem: 'problem_user',
  performanceGlitch: 'performance_glitch_user',
} as const;

export const BOOKER_ADMIN = { username: 'admin', password: 'password123' };

// Demo sites may be accessed through a TLS-inspection proxy (corporate
// "self-signed certificate in chain"). Default ON so the suite runs everywhere;
// set IGNORE_HTTPS_ERRORS=false to enforce real certificate checks.
export const IGNORE_HTTPS_ERRORS = process.env.IGNORE_HTTPS_ERRORS !== 'false';
