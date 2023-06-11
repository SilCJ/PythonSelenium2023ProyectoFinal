from src.page_objects.login_page import LoginPage


def forgotpassword(web_drivers):
    login_page = LoginPage(*web_drivers)
    login_page.open()
    login_page("silvia.castillo.juarez@gmail.com")
