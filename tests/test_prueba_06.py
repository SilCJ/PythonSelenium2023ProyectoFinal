from src.page_objects.checkout_page import CheckoutPage
from selenium.webdriver.support.select import Select


def select_by_visible_text(param):
    select_by_visible_text("Mexico")
    select.select_by_visible_text("Distrito Federal")


def test_search(web_drivers):
    checkout_page = CheckoutPage(*web_drivers)
    checkout_page.open()
    checkout_page.addressbuyin("Silvia", "Castillo", "Test", "Alvaro Obregón", "CDMX", "06100")
    select_by_visible_text("Mexico")
    select.select_by_visible_text("Distrito Federal")

