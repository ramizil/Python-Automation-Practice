import { defineConfig, devices } from '@playwright/test';
import { URLS, IGNORE_HTTPS_ERRORS } from './src/config';

// Only the worked reference examples in tests/ run by default.
// Run an exercise explicitly, e.g.  npx playwright test exercises/01_first_test
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  // Public demo sites behind a proxy can be slow; give them room and don't
  // overwhelm the network by launching too many browsers at once.
  workers: process.env.CI ? 2 : 4,
  timeout: 60_000,
  expect: { timeout: 10_000 },
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: URLS.saucedemo,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    ignoreHTTPSErrors: IGNORE_HTTPS_ERRORS,
    navigationTimeout: 45_000,
    actionTimeout: 15_000,
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
