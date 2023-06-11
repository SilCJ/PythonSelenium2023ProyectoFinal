class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CheckoutPage, self).__init__(driver, wait_driver)

    def addresbuying(self, firstname: str, lastname: str, company: str, address: str, city: str, postcode: str):
        self.element("firstname_input").wait_clickable().send_keys(firstname)
        self.element("lastname_input").wait_clickable().send_keys(lastname)
        self.element("company_input").wait_clickable().send_keys(company)
        self.element("address_input").wait_clickable().send_keys(address)
        self.element("city_input").wait_clickable().send_keys(city)
        self.element("postcode_input").wait_clickable().send_keys(postcode)
        self.element("country_select").wait_clickable().click()
        self.driver.find_element("country_select")
        self.driver.find_element("state_select")
        self.element("continue_btn").wait_clickable().click()

    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text
