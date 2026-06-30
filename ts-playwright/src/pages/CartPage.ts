import { Locator, Page } from '@playwright/test';

export class CartPage {
  readonly page: Page;
  readonly items: Locator;
  readonly checkoutButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.items = page.locator('.cart_item');
    this.checkoutButton = page.locator('#checkout');
  }

  async itemNames(): Promise<string[]> {
    return this.page.locator('.cart_item .inventory_item_name').allInnerTexts();
  }

  async checkout(): Promise<void> {
    await this.checkoutButton.click();
  }
}
