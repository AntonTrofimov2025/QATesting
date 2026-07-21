import pytest

@pytest.mark.usefixtures("setup")
class TestUserCart:

    def test_add_any_item(self):
        self.auth_page.login_with_credentials('standard_user')
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.click_cart_button()
        self.cart_page.assert_cart_page()
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_form_and_continue()
        self.checkout_page.assert_container_item_name(4)
        self.checkout_page.click_finish()
        self.checkout_page.assert_text_in_order_confirmation()
        self.checkout_page.back_home()
        self.inventory_page.scroll_up_by(300)
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

    def test_add_sauce_labs_bolt(self):
        self.auth_page.login_with_credentials('problem_user')
        self.inventory_page.assert_inventory_page()
        self.inventory_page.add_backpack_to_cart()
        self.common.assert_elements_quantity_by_number(1)
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

    def test_hw6_add_three_items(self):
        self.auth_page.login_with_credentials('standard_user')
        self.inventory_page.add_many_cart_items()
        self.inventory_page.click_cart_button()
        self.cart_page.assert_cart_page()
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_form_and_continue()
        self.checkout_page.scroll_down_by(500)
        self.checkout_page.assert_total_price('58.29')
        self.checkout_page.click_finish()
        self.checkout_page.assert_text_in_order_confirmation()
        self.checkout_page.back_home()
        self.inventory_page.scroll_up_by(300)
        self.inventory_page.burger_click()
        self.inventory_page.reset_state()
        self.auth_page.log_out()

