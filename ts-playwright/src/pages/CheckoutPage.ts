import { Locator, Page } from '@playwright/test';

export class CheckoutPage {
  readonly page: Page;
  readonly firstName: Locator;
  readonly lastName: Locator;
  readonly postalCode: Locator;
  readonly continueButton: Locator;
  readonly finishButton: Locator;
  readonly completeHeader: Locator;

  constructor(page: Page) {
    this.page = page;
    this.firstName = page.locator('#first-name');
    this.lastName = page.locator('#last-name');
    this.postalCode = page.locator('#postal-code');
    this.continueButton = page.locator('#continue');
    this.finishButton = page.locator('#finish');
    this.completeHeader = page.locator('.complete-header');
  }

  async fillInformation(first: string, last: string, postal: string): Promise<void> {
    await this.firstName.fill(first);
    await this.lastName.fill(last);
    await this.postalCode.fill(postal);
    await this.continueButton.click();
  }

  async finish(): Promise<void> {
    await this.finishButton.click();
  }
}
