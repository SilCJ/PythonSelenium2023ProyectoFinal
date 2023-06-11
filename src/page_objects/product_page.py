
class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(ProductPage, self).__init__(driver, wait_driver)

    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text

    def producto_compare(self, email: str):
        self.element("search_btn").wait_clickable().click()
        self.element("product_btn").wait_clickable().click()
        self.element("compare1_btn").wait_clickable().click()
        self.element("compare2_btn").wait_clickable().click()
        self.element("link_compare").wait_clickable().click()