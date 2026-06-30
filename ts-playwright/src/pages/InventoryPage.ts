import { Locator, Page } from '@playwright/test';

export class InventoryPage {
  readonly page: Page;
  readonly title: Locator;
  readonly cartLink: Locator;
  readonly cartBadge: Locator;

  constructor(page: Page) {
    this.page = page;
    this.title = page.locator('.title');
    this.cartLink = page.locator('.shopping_cart_link');
    this.cartBadge = page.locator('.shopping_cart_badge');
  }

  private addButtonFor(itemName: string): Locator {
    return this.page
      .locator('.inventory_item')
      .filter({ hasText: itemName })
      .getByRole('button', { name: 'Add to cart' });
  }

  async addItemToCart(itemName: string): Promise<void> {
    await this.addButtonFor(itemName).click();
  }

  async cartCount(): Promise<number> {
    if ((await this.cartBadge.count()) === 0) return 0;
    return Number(await this.cartBadge.innerText());
  }

  async goToCart(): Promise<void> {
    await this.cartLink.click();
  }
}
