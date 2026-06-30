// Layer 2 — SauceDemo business steps.
// Reusable business actions ("log in as standard", "check out") composed from
// the page objects, so Layer-3 tests never touch selectors.
import { Page } from '@playwright/test';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../config';
import { LoginPage } from '../../pages/LoginPage';
import { InventoryPage } from '../../pages/InventoryPage';
import { CartPage } from '../../pages/CartPage';
import { CheckoutPage } from '../../pages/CheckoutPage';
import { getLogger, Logger } from '../../core/logger';

export class SauceDemoSteps {
  private loginPage: LoginPage;
  private inventory: InventoryPage;
  private cart: CartPage;
  private checkoutPage: CheckoutPage;
  private log: Logger;

  constructor(page: Page) {
    this.loginPage = new LoginPage(page);
    this.inventory = new InventoryPage(page);
    this.cart = new CartPage(page);
    this.checkoutPage = new CheckoutPage(page);
    this.log = getLogger('SauceDemoSteps');
  }

  async loginAs(userKey: keyof typeof SAUCE_USERS = 'standard'): Promise<this> {
    this.log.info(`login as ${userKey}`);
    await this.loginPage.open();
    await this.loginPage.login(SAUCE_USERS[userKey], SAUCE_PASSWORD);
    return this;
  }

  async addItemsToCart(names: string[]): Promise<this> {
    this.log.info(`add to cart: ${names.join(', ')}`);
    for (const name of names) await this.inventory.addItemToCart(name);
    return this;
  }

  /** Complete checkout for whatever is in the cart; return the confirmation text. */
  async checkout(first: string, last: string, postal: string): Promise<string> {
    this.log.info(`checkout as ${first} ${last}`);
    await this.inventory.goToCart();
    await this.cart.checkout();
    await this.checkoutPage.fillInformation(first, last, postal);
    await this.checkoutPage.finish();
    return this.checkoutPage.completeHeader.innerText();
  }
}
