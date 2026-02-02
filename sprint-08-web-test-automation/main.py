from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages import UrbanRoutesPage
import data
import helpers
from helpers import retrieve_phone_code

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Verificar se o servidor "Urban Routes" está funcionando corretamente"
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao servidor Urban Routes. Verifique se o servidor está ligado e ainda em execução")
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.urban_routes_page = UrbanRoutesPage(cls.driver)



    def test_end_to_end_taxi_order2(self):
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.urban_routes_page.selected_comfort_tariff()
        self.urban_routes_page.fill_phone_number_field(data.PHONE_NUMBER)
        self.urban_routes_page.fill_card_info(data.CARD_NUMBER, data.CARD_CODE)

        assert self.urban_routes_page.is_card_selected(), "O cartão não foi selecionado"
        self.urban_routes_page.click_comment_field()
        self.urban_routes_page.input_comment_field(data.MESSAGE_FOR_DRIVER)

        comment_text = self.urban_routes_page.get_comment_field_value()
        assert comment_text == data.MESSAGE_FOR_DRIVER
        self.urban_routes_page.click_blanket_checkbox()
        self.urban_routes_page.order_2_ice_creams()
        self.urban_routes_page.get_ice_cream_counter_value()
        self.urban_routes_page.taxi_confirm_button()
        self.urban_routes_page.wait_for_driver_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
