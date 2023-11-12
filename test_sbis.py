from pages.sbis_main_page import MainPage
from pages.sbis_contacts_page import ContactsPage
from pages.tenzor_main_page import TenzorPage
from pages.tenzor_about import TenzorAbout
from pages.new_page_contakts import Contacts2Page

def test_1(browser):
    link = "https://sbis.ru/"
    browser.implicitly_wait(5)                 # настраиваем неявное ожидание

    page = MainPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                 # открываем страницу
    page.go_to_contacts_page()                  # находим кнопку контакты и кликаем по ней

    page2 = ContactsPage(browser, link)
    page2.go_to_tenzor_page()                   # находим кнопку Тензор и переходим по ней


    page3 = TenzorPage(browser, link)
    page3.change_window()                      # меняем активное окно
    page3.find_container()                     # находим нужную статью
    page3.click_about()                        # кликаем на подробнее

    page4 = TenzorAbout(browser, link)
    page4.find_pictures()                      # находим раздел с фотографиями и проверяем их параметры

def test_2(browser):
    link = "https://sbis.ru/contacts/16-respublika-tatarstan?tab=clients"
    browser.implicitly_wait(5)

    page = ContactsPage(browser, link)
    page.open()                                # открываем страницу
    page.info_region()                         # проверяем определяется ли правильное местоположение

    page.info_partner()                        # проверяем есть ли информация о партнерах
    page.change_region()                       # меняем регион


    page = Contacts2Page(browser, link)
    page.check_region()                        # проверяем все ли корректно поменялось








