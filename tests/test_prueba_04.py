from src.page_objects.search_page import SearchPage


def test_searchnew(web_drivers):
    search_page = SearchPage(*web_drivers)
    search_page.open()