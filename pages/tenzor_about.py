from pages.base_page import BasePage
from pages.locators import TenzorAboutPage
class TenzorAbout(BasePage):
    def find_pictures(self):
        pictures = self.browser.find_elements(*TenzorAboutPage.PICTURES)
        width = pictures[0].size['width']
        height = pictures[0].size['height']
        for i in range(4):
            pic_w = pictures[i].size['width']
            pic_h = pictures[i].size['height']
            if width == pic_w and height == pic_h:
                print(" Картинка " + str(i+1) + " прошла проверку по высоте и ширине")
            else:
                print(" Ошибка: картинка " + str(i+1) + " не прошла проверку по высоте и ширине")

