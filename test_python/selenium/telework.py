from selenium import webdriver
import time
import pandas as pd

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# MBCのURL
MBC_URL = 'https://wa.motionboard.jp/motionboard/main'

# 変数
tenant = 'tenant'
id = 'id'
password = 'pw'


# webdriverの指定
driver = webdriver.Chrome(
    r'path')

# driver.get('https://www.google.com/')
driver.get(MBC_URL)
time.sleep(1)

# フィールドに値をセット
driver.find_element_by_id("tenant").send_keys(tenant)
driver.find_element_by_id("id").send_keys(id)
driver.find_element_by_id("pw").send_keys(password)

# 検索実行
# driver.find_element_by_class_name('gb_g').click()
driver.find_element_by_id("button").click()
time.sleep(1)
