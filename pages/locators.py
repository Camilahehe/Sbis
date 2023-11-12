from selenium.webdriver.common.by import By

class SbisMainPage():
    # Кнопка контакты
    CONTACT_BUTTON = (By.XPATH,"//*[@id='wasaby-content']/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a")

class SbisContactsPage():
    TENZOR_BUTTON = (By.CSS_SELECTOR,"#contacts_clients > div.sbis_ru-container > div > div > div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 > div > a > img")
    RESP_BUTTON = (By.XPATH, "//*[@id='container']/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    PARTNERS_INFO = (By.CSS_SELECTOR, "[class='icon-24 icon-Signature icon-hover sbisru-Contacts-List__icon']")
    KAMCHATKA = (By.CSS_SELECTOR,"[title = 'Камчатский край']")
    TITLE_WEB = (By.CSS_SELECTOR, "[class = 'state-1']")
class TenzorMainPage():
    STATE_PEOPLE = (By.XPATH, "//*[contains(text(), 'Сила')]") # Статья сила в людях
    ABOUT_STATE = (By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a") # Кнопка подробнее под статьей

class TenzorAboutPage():
    PICTURES = (By.CSS_SELECTOR, "[class= 'tensor_ru-About__block3-image-filter']")



