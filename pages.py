from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class UrbanRoutesPage:
    #Localizadores
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    ORDER_TAXI_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Chamar um táxi']")
    COMFORT_OPTION_LOCATOR = (By.XPATH, '//div[text()="Comfort"]')
    COMFORT_SELECTED_LOCATOR = (By.XPATH, '//div[contains(@class, "tcard active")]//div[text()="Comfort"]')
    PHONE_MODAL = (By.XPATH, "//div[contains(text(), 'Insira seu número de telefone')]")
    PHONE_NUMBER_OPTION_LOCATOR = (By.XPATH, '//div[text()="Número de telefone"]')
    PHONE_NUMBER_INPUT_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Próximo"]')
    SMS_CODE_LOCATOR = (By.XPATH, '//div[text()="Digitar o código do SMS"]')
    SMS_CODE_INPUT_LOCATOR = (By.ID, 'code')
    SMS_CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirmar"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-button filled" and contains (.,"Método de pagamento")]')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Adicionar cartão"]')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CVV_LOCATOR = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Adicionar"]')
    CARD_CHECKBOX_LOCATOR= (By.ID, "card-1")
    CLOSE_BUTTON_LOCATOR = (By.XPATH,
                            '//div[contains(@class,"payment-picker")]//button[@class="close-button section-close"]')
    COMMENT_FIELD_LOCATOR = (By.ID, 'comment')
    BLANKET_CHECKBOX_LOCATOR = (By.XPATH, '//div[text()="Cobertor e lençóis"]')
    BLANKET_CHECKED_LOCATOR = (By.XPATH, '//div[@class="r-sw"]//div[contains(@class,"switch-on")]')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, '//div[@class="r-group-items"]//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER_LOCATOR = (By.XPATH, '//div[@class="r-group-items"]//div[@class="counter-value"]')
    TAXI_CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Pedir"]')
    SEARCH_MODAL_LOCATOR = (By.XPATH, "//div[text()='Buscar carro']")
    DRIVER_MODAL_LOCATOR = (By.XPATH, "//div[contains(text(), 'O motorista vai chegar em')]")


    def __init__(self, driver):
        self.driver = driver  # Inicilizar o driver

    def click_from_field(self):
        wait = WebDriverWait(self.driver, 10)
        # Clica no label que está interceptando
        label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="from"]')))
        label.click()

        # Inserir De
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def click_to_location(self):
        # Clica no label que está associado ao campo "Para"
        wait = WebDriverWait(self.driver, 10)
        to_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="to"]')))
        to_label.click()

    def enter_to_location(self, to_text):
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

        #Definir a rota
    def set_route(self, address_from, address_to):
        self.click_from_field ()
        self.enter_from_location(address_from)
        self.click_to_location()
        self.enter_to_location(address_to)


    def click_personal_option(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.PERSONAL_OPTION_LOCATOR))
        element.click()

    def click_call_taxi_button(self):
        # Aguardar o botão aparecer antes de clicar
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.ORDER_TAXI_BUTTON_LOCATOR)).click()



    def is_tariff_button_selected(self):
        elements = self.driver.find_elements(*self.COMFORT_SELECTED_LOCATOR)
        if len(elements) > 0:
            return True
        else:
            return False

    def click_comfort_tariff_button(self):
        self.driver.find_element(*self.COMFORT_OPTION_LOCATOR).click()

        

    def selected_comfort_tariff(self):
        self.click_personal_option()
        self.click_call_taxi_button()
        if not self.is_tariff_button_selected():
            self.click_comfort_tariff_button()
        else:
            pass



    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_OPTION_LOCATOR).click()

    def is_phone_modal_open(self):
        elements = self.driver.find_elements (*self.PHONE_MODAL)
        return len (elements)>0


    def enter_phone_number_field(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def click_sms_code(self):
        self.driver.find_element(*self.SMS_CODE_LOCATOR).click()

    def input_sms_code(self, sms_code):
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(sms_code)

    def click_confirm_button(self):
        self.driver.find_element(*self.SMS_CONFIRM_BUTTON_LOCATOR).click()



        #Preencher número de telefone
    def fill_phone_number_field(self, phone_number):
        self.click_phone_number_field()
        self.enter_phone_number_field(phone_number)
        self.click_next_button()

        self.click_sms_code()
        sms_code = retrieve_phone_code(self.driver)
        self.input_sms_code(sms_code)
        self.click_confirm_button()




    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def input_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    def click_cvv_button(self):
        self.driver.find_element(*self.CVV_LOCATOR).click()

    def input_cvv(self, cvv):
        self.driver.find_element(*self.CVV_LOCATOR).send_keys(cvv)

    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def is_card_selected(self):
        card_checkbox = self.driver.find_element(*self.CARD_CHECKBOX_LOCATOR)
        return card_checkbox.is_selected()

    def click_close_button(self):
        wait = WebDriverWait(self.driver, 10)
        close_button = wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON_LOCATOR))
        close_button.click()





        #Preencher informações do cartão
    def fill_card_info(self, card_number, cvv):
        self.click_payment_method()
        self.click_add_card()
        self.input_card_number(card_number)
        self.click_cvv_button()
        self.input_cvv(cvv)
        self.click_add_card_button()
        self.is_card_selected()
        self.click_close_button()




    def click_comment_field(self):
        # Clica no label em vez do input para evitar ElementClickInterceptedException
        comment_label = self.driver.find_element(By.XPATH, "//label[@for='comment']")
        comment_label.click()

    def input_comment_field(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD_LOCATOR).send_keys(comment)

        
    def get_comment_field_value(self):
        return self.driver.find_element(*self.COMMENT_FIELD_LOCATOR).get_attribute("value")


    def click_blanket_checkbox(self):
        # Teste: clicar diretamente no slider
        slider = self.driver.find_element(By.XPATH, "//span[@class='slider round']")
        slider.click()

    def comment_for_driver(self, comment):
        self.click_comment_field()
        self.input_comment_field(comment)
        return self.get_comment_field_value()  # Retorna o valor para verificação





    def is_blanket_toogle_on(self):
        toggle_input = self.driver.find_element(By.XPATH, "//input[@class='switch-input']")
        return toggle_input.is_selected()  # Retorna True se checked, False se não

    def request_blanket_checkbox(self):
        self.click_blanket_checkbox()
        self.is_blanket_toogle_on()

    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def order_2_ice_creams(self):
        for cont in range(2):
            self .click_ice_cream_plus()



    def get_ice_cream_counter_value(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER_LOCATOR).text

    def taxi_confirm_button(self):
        self.driver.find_element(*self.TAXI_CONFIRM_BUTTON_LOCATOR).click()


    def wait_for_driver_modal(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.DRIVER_MODAL_LOCATOR))








