from src.page_objects.register_page import RegisterPage


def test_search(web_drivers):
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.registrarse1("Silvia", "Castillo", "silvia.castillo.juarez@gmail.com", "5539304887", "TestQA123", "TestQA123")
