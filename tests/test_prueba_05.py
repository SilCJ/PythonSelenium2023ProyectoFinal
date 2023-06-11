from src.page_objects.product_page import ProductPage


def test_search(web_drivers):
    product_page = ProductPage(*web_drivers)
    product_page.open()
