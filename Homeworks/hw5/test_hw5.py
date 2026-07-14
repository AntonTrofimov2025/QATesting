from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_iframe_text(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/iframes.html')
    iframe = driver.find_element(By.ID, 'my-iframe')
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'content'),
                                          'semper posuere integer et senectus justo curabitur.'))
    our_text = driver.find_element(By.ID, 'content')
    assert 'semper posuere integer et senectus justo curabitur.' in our_text.text

def test_drag_photos(driver):
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
    iframe = driver.find_element(By.CSS_SELECTOR, '[class="demo-frame"]')
    driver.switch_to.frame(iframe)
    first_photo = driver.find_element(By.CSS_SELECTOR, '#gallery li:nth-child(1)')
    trash = driver.find_element(By.ID, 'trash')
    ActionChains(driver).scroll_by_amount(0, 200).perform()
    ActionChains(driver).drag_and_drop(first_photo, trash).perform()
    WebDriverWait(driver, 10).until(lambda dr: len(dr.find_elements(By.CSS_SELECTOR, '#trash > ul li')) == 1)
    WebDriverWait(driver, 10).until(lambda dr: len(dr.find_elements(By.CSS_SELECTOR, '[id="gallery"] li')) == 3)

