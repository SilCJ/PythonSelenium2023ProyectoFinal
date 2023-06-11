from src.page_objects.account_page import AccountPage
from src.page_objects.register_page import RegisterPage



def test_valid_register(web_drivers):
    expected_title = "Register Account"
    expected_right_menus = ["My Account", "Edit Account", "Password", "Address Book"]
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    account_page = AccountPage(*web_drivers)
    actual_title = account_page.get_title()
    assert expected_title == actual_title, f"Page title after login should be {expected_title}"
