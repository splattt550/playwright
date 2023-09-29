# coding: utf-8
import time
import unittest
import pyautogui
from playwright.sync_api import sync_playwright


class PWTests(unittest.TestCase):

    def test_pyauto(self):
        ishere = pyautogui.locateCenterOnScreen(r"D:\jb\code.png")
        if isinstance(ishere, pyautogui.Point):
            print(ishere.x, ishere.y)
            pyautogui.write(message="I am here!")
        updateX, updateY = pyautogui.locateCenterOnScreen(r"D:\jb\update.png")
        print(updateX, updateY)
        pyautogui.click(updateX, updateY)

    def test_playwtright(self):
        # with sync_playwright() as p:
        #     browser = p.chromium.launch()
        #     page = browser.new_page()
        #     page.goto("http://127.0.0.1:5000/")
        #     page.wait_for_selector('input[type="password"]')
        #     page.screenshot(path=r"D:\jb\sc.png")
        #     print(page.title())
        #     browser.close()
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            # Open new page
            page = context.new_page()
            # Go to http://127.0.0.1:5000/
            page.goto("http://127.0.0.1:5000/")
            # Uncheck #checkbox31e0b225 .mud-button-root .mud-checkbox-input
            page.locator("text=Установить WebHelp").click()
            # Uncheck #checkbox6e2d92c7 .mud-button-root .mud-checkbox-input
            page.locator("text=Установить DevelopmentStudio").click()
            # Uncheck #checkbox3bf9c01c .mud-button-root .mud-checkbox-input
            page.locator("text=Установить DeploymentToolUI").click()
            # Click button:has-text("Обновить")
            page.locator("button:has-text(\"Обновить\")").click()
            # Fill #radio30850d26 input[role="radio"]
            page.screenshot(path=r"D:\jb\sc.png")
            # ---------------------
            context.close()
            browser.close()

    def test_playwright2(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            # Open new page
            page = context.new_page()
            # Go to http://127.0.0.1:5000/
            page.goto("http://127.0.0.1:5000/")
            # Click text=Адрес сайта Для работы в локальной сети укажите имя компьютера. Для работы через >> input[type="text"]
            page.locator("text=Адрес сайта Для работы в локальной сети укажите имя компьютера. Для работы через >> input[type=\"text\"]").click()
            # Press a with modifiers
            page.locator("text=Адрес сайта Для работы в локальной сети укажите имя компьютера. Для работы через >> input[type=\"text\"]").press("Control+a")
            # Fill text=Адрес сайта Для работы в локальной сети укажите имя компьютера. Для работы через >> input[type="text"]
            page.locator("text=Адрес сайта Для работы в локальной сети укажите имя компьютера. Для работы через >> input[type=\"text\"]").fill("playwright")
            # Click text=https >> nth=0
            page.locator("text=https").first.click()
            # Click [id="_feaef0de"] >> text=http
            page.locator("p:has-text('http') >> nth=1").click()
            # Check text=Сервер БД СерверБаза данныхПользователь Пароль >> input[type="checkbox"]
            page.locator("text=Сервер БД СерверБаза данныхПользователь Пароль >> input[type=\"checkbox\"]").check()
            # Click text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type="text"]
            page.locator("text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type=\"text\"]").click()
            # Click text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type="text"]
            page.locator("text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type=\"text\"]").click()
            # Press a with modifiers
            page.locator("text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type=\"text\"]").press("Control+a")
            # Fill text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type="text"]
            page.locator("text=Сервер БД Укажите строку подключения к СУБД в формате ConnectionString. >> input[type=\"text\"]").fill("TestConnectionString")
            # Check text=Сервер RabbitMQ СерверПортВиртуальный хостПользователь ПарольТочка обмена >> input[type="checkbox"]
            page.locator("text=Сервер RabbitMQ СерверПортВиртуальный хостПользователь ПарольТочка обмена >> input[type=\"checkbox\"]").check()
            # Click text=Сервер RabbitMQ Строка подключения к серверу RabbitMQ >> input[type="text"]
            page.locator("text=Сервер RabbitMQ Строка подключения к серверу RabbitMQ >> input[type=\"text\"]").click()
            # Press a with modifiers
            page.locator("text=Сервер RabbitMQ Строка подключения к серверу RabbitMQ >> input[type=\"text\"]").press("Control+a")
            # Fill text=Сервер RabbitMQ Строка подключения к серверу RabbitMQ >> input[type="text"]
            page.locator("text=Сервер RabbitMQ Строка подключения к серверу RabbitMQ >> input[type=\"text\"]").fill("TestRabbitMQString")
            # Check text=Сервер MongoDB СерверПортПользователь Пароль >> input[type="checkbox"]
            page.locator("text=Сервер MongoDB СерверПортПользователь Пароль >> input[type=\"checkbox\"]").check()
            # Uncheck text=Сервер MongoDB Строка подключения к серверу MongoDB >> input[type="checkbox"]
            page.locator("text=Сервер MongoDB Строка подключения к серверу MongoDB >> input[type=\"checkbox\"]").uncheck()
            # Click text=Папка с данными Данная папка должна существовать. В ней будут созданы подпапки д >> input[type="text"]
            page.locator("text=Папка с данными Укажите существующую папку для хранения  >> input[type=\"text\"]").click()
            # Fill text=Папка с данными Данная папка должна существовать. В ней будут созданы подпапки д >> input[type="text"]
            page.locator("text=Папка с данными Укажите существующую папку для хранения  >> input[type=\"text\"]").fill("C:/")
            # Click text=Папка с данными
            page.locator("text=Папка с данными").click()
            # Click text=Папка с данными Данная папка должна существовать. В ней будут созданы подпапки д >> input[type="text"]
            page.locator("text=Папка с данными Укажите существующую папку для хранения  >> input[type=\"text\"]").click()
            # Press a with modifiers
            page.locator("text=Папка с данными Укажите существующую папку для хранения  >> input[type=\"text\"]").press("Control+a")
            # Fill text=Папка с данными Данная папка должна существовать. В ней будут созданы подпапки д >> input[type="text"]
            page.locator("text=Папка с данными Укажите существующую папку для хранения  >> input[type=\"text\"]").fill("D:/")
            # Click text=ПарольПри создании БД этот пароль будет установлен для всех служебных пользовате >> input[type="password"]
            page.locator("text=ПарольПри создании  >> input[type=\"password\"]").click()
            # Fill text=ПарольПри создании БД этот пароль будет установлен для всех служебных пользовате >> input[type="password"]
            page.locator("text=ПарольПри создании   >> input[type=\"password\"]").fill("11111")
            # Click text=ПарольПовторите пароль >> input[type="password"]
            page.locator("text=ПарольПовторите пароль >> input[type=\"password\"]").click()
            # Fill text=ПарольПовторите пароль >> input[type="password"]
            page.locator("text=ПарольПовторите пароль >> input[type=\"password\"]").fill("11111")
            # Click text=Код системы Выдается при первой поставке системы, используется для генерации штр >> input[type="text"]
            page.locator("text=Код системы Запросите в службе  >> input[type=\"text\"]").click()
            # Fill text=Код системы Выдается при первой поставке системы, используется для генерации штр >> input[type="text"]
            page.locator("text=Код системы Запросите в службе  >> input[type=\"text\"]").fill("Test")
            # Uncheck #checkbox9e081c0f .mud-button-root .mud-checkbox-input
            # page.locator("text=Установить WebHelp").click()
            # Click button:has-text("Установить")
            page.locator("button:has-text(\"Установить\")").click()
            time.sleep(1)
            with open(r'D:\Projects\SungeroScripts\etc\config.yml','r', encoding='utf-8') as f:
                file1 = f.read()
                with open(r'D:\Projects\SungeroScripts\etc\config_test.yml','r', encoding='utf-8') as f2:
                    file2 = f2.read()
                    self.assertEqual(file1, file2)

            context.close()
            browser.close()



