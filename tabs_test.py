
import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os
from pathlib import Path

file_path_os = os.path.join('C:\\', 'Users', 'ICH', 'Downloads', 'images.jpg')
file_path_pathlib = str(Path('C:/Users/ICH/Downloads/images.jpg'))

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_with_tabs(driver):
    # sleep(3)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.execute_script("window.open('https://the-internet.herokuapp.com/javascript_alerts', '_blank');")
    driver.execute_script("window.open('https://google.com', '_blank');")
    # Получаем список всех вкладок
    tabs = driver.window_handles
    print("Идентификаторы вкладок:", tabs)
    # Переключаемся на вторую вкладку (Google)
    sleep(2)
    driver.switch_to.window(tabs[0])
    sleep(2)
    print("Текущая вкладка:", driver.current_window_handle)
    driver.close()
    sleep(2)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
    print("Текущая вкладка:", driver.current_window_handle)
    sleep(2)
    
def test_with_hover(driver):
    url = "https://the-internet.herokuapp.com/hovers"
    driver.get(url)
    element_to_hover = driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(5)")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    sleep(5)

def test_dragging(driver):
    driver.get("https://jqueryui.com/droppable/")
    # Переключаемся в iframe, если drag-and-drop внутри фрейма
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    # Находим элементы
    source = driver.find_element(By.ID, "draggable")  # Что перетаскиваем
    target = driver.find_element(By.ID, "droppable")  # Куда перетаскиваем

    # Выполняем перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(5)

def test_upload(driver):
    url = "https://the-internet.herokuapp.com/upload"
    driver.get(url)

    # Находим input-элемент
    file_input = driver.find_element(By.ID, "file-upload")

    # Указываем путь к файлу
    file_path = "C:\\Users\\ICH\\Downloads\\images.jpg"  # Укажите путь к файлу на своем компьютере
    file_input.send_keys(file_path_pathlib)
    sleep(3)

    # Отправляем форму (если требуется)
    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()
    sleep(3)

# ------------------------------

def test_consent(driver):
    driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
    driver.add_cookie({
        'name': 'FCCDCF',
        'value':
            '%5Bnull%2Cnull%2Cnull%2C%5B%22CQnVtgAQnVtgAEsACBRUCnFoAP_gAEPgABBoMGoB_C7EbCFCiDJ3IKMEMAhHABBAY'
            'sAwAAYAAgAADBIQIAQCgkEYBASAFCACCAAAKASBAAAgCAAAAUAAIAAFAABAAAwAIBAIIAAAgAAAAEAAAAAACIAAEQCAAAAE'
            'AEAAkAgAAAIAWEAAAAAAAACBAAAAAAAAAAAAAAAABAEAAQAAQAAAAAAAiAAAAAAAABAIAAAAAAAAAAAAAAAAAAAAAAgAAAA'
            'AAAAAABAAAAAAAQgAAAAAAAAAAAAAAAAAAEAAAAAAIMGoB_C7EbCFCiDBXIKMEMAhXABAAYsAwAAYAAgAADBIQIAQCkkESB'
            'ACAECAACAAAIAQBAAAoAAgAAEAAAAAVAABAAAwAIBAIAEAAgAAAQEAAAAAACIAAEQCAAAAEAEAAgAgAAAIAWEAAAAAAAACB'
            'AAAAAAAAAAAAAAAAAAEAACAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAEAAAAA'
            'AAAAAAAAAAEAAAAAAIAA.IMGoB_C7EbCFCiDJ3IKMEMAhXABBAYsAwAAYAAgAADBIQIAQCkkEaBASAFCACCAAAKASBAAAoC'
            'AgAAUAAIAAVAABAAAwAIBAIIEAAgAAAQEAAAAAACIAAEQCAAAAEAEAAkAgAAAIAWEAAAAAAAACBAAAAAAAAAAAAAAAABAEA'
            'ASAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQgAAEAAAAAAAAAAAAAAAEAAAAAAIA%'
            '22%2C%222~61.89.122.161.184.196.230.314.340.442.445.494.550.576.827.1025.1029.1033.1046.1047.10'
            '51.1097.1126.1166.1301.1342.1415.1725.1942.1958.1987.2068.2072.2074.2107.2213.2219.2223.2224.23'
            '28.2331.2416.2501.2567.2568.2575.2657.2778.2869.2878.2908.2920.2963.3005.3023.3126.3235.3253.33'
            '09.3731.6931.8931.13731.15731.33931~dv.%22%2C%225A58EBEE-7160-48DC-A96E-96CB48077623%22%5D%2Cnu'
            'll%2Cnull%2C%5B%5B32%2C%22%5B%5C%2298303be6-23fe-4fe5-b2b0-7162cef72cb2%5C%22%2C%5B1784035184%2'
            'C276000000%5D%5D%22%5D%5D%5D',
        'domain': '.globalsqa.com',
        'path': '/',
        'secure': False
    })
    driver.refresh()
    sleep(5)

