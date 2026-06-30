// Config for running the practice exercises (skeletons + solutions).
// Example:  npx playwright test -c playwright.exercises.config.ts 01_first_test
import baseConfig from './playwright.config';

export default {
  ...baseConfig,
  testDir: './exercises',
};
