import pytest

@pytest.mark.usefixtures("setup")
class TestUserCart:

    def test_add_any_item(self):
        self.auth_page.input_username_password('standard_user')
        self.common.click_by_id("add-to-cart-sauce-labs-backpack")
        self.common.get_cart_link_n_click()
        self.cart_page.assert_cart_page()
        self.common.click_by_id('checkout')
        self.checkout_page.fill_form()
        self.common.click_by_id('continue')
        self.common.assert_naming_of_container_item(4)
        self.common.click_by_id('finish')
        self.checkout_page.assert_text_in_order_confirmation()
        self.checkout_page.back_home()
        self.inventory_page.scroll_up()
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

    def test_add_sauce_labs_bolt(self):
        self.auth_page.input_username_password('problem_user')
        self.inventory_page.assert_inventory_page()
        self.common.click_by_id("add-to-cart-sauce-labs-backpack")
        self.common.assert_elements_quantity_by_number(1)
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

    def test_hw6_add_three_items(self):
        self.auth_page.input_username_password('standard_user')
        self.inventory_page.add_many_cart_items('add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bolt-t-shirt', 'add-to-cart-sauce-labs-onesie')
        self.common.get_cart_link_n_click()
        self.cart_page.assert_cart_page()
        self.common.click_by_id('checkout')
        self.checkout_page.fill_form()
        self.common.click_by_id('continue')
        self.checkout_page.scroll_down_by(500)
        self.checkout_page.assert_total_price('58.29')
        self.common.click_by_id('finish')
        self.checkout_page.assert_text_in_order_confirmation()
        self.checkout_page.back_home()
        self.inventory_page.scroll_up()
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

