import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
import requests

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(r'Driver', chrome_options=options
                          )
wait = WebDriverWait(driver, 10)

# 取得したデータフレームを格納するアウトプットディレクトリ
outputfiles_dir = 'OutputDir'

# todo
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)


# 食べログのBASE_URL
BASE_URL = 'https://tabelog.com/'

# 変数
key_word = 'ケバブサンド'

driver.get(BASE_URL)
time.sleep(1)

# フィールドに値をセット
driver.find_element_by_id("sk").send_keys(key_word)

# 検索実行
driver.find_element_by_id("js-global-search-btn").click()
time.sleep(1)
wait.until(EC.presence_of_all_elements_located)

# ケバブで検索された画面が開く
cur_url = driver.current_url

headers = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(cur_url, headers=headers).content, 'lxml')


def getCurURL():
    cur_url = driver.current_url
    headers = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(
        cur_url, headers=headers).content, 'lxml')
    return soup


# 取得した情報を格納する変数
store_names = []
detail_urls = []
addresses = []
scores = []
reviews = []

# 関数店舗名の取得店舗詳細URLの取得


def getLink(soup):
    for store_name in soup.find_all(class_='list-rst__rst-name-target cpy-rst-name'):
        store_names.append(store_name.getText())
        detail_urls.append(store_name.get('href'))
    return detail_urls

# 関数スコアの取得


def getScore(soup):
    for score in soup.find_all(class_='c-rating__val c-rating__val--strong list-rst__rating-val'):
        scores.append(score.getText())
    return scores


def getScoreDetail(soup):
    score = soup.find(class_='rdheader-rating__score-val-dtl')
    scores.append(score.getText())
    return scores


# 関数口コミ数の取得


def getReview(soup):
    for review in soup.find_all(class_='list-rst__rvw-count-num cpy-review-count'):
        reviews.append(review.getText())
    return reviews


def getReviewDetail(soup):
    review = soup.select_one(".rdheader-rating__review-target .num")
    reviews.append(review.get_text())
    return reviews


# 関数住所の取得


def getAddress():
    for address in detail_urls:
        cur_url = address
        soup = BeautifulSoup(requests.get(
            cur_url, headers=headers).content, 'lxml')
        elements = soup.find("p", class_='rstinfo-table__address')
        addresses.append(elements.get_text())
        # 追加
        getScoreDetail(soup)
        getReviewDetail(soup)
    return addresses, reviews, scores


# todo次のページのごとにbsの更新
while True:
    time.sleep(5)
    wait.until(EC.presence_of_all_elements_located)
    cur_url = driver.current_url
    soup = BeautifulSoup(requests.get(
        cur_url, headers=headers).content, 'lxml')
    getLink(soup)
    # getScore(soup)
    # getReview(soup)
    try:
        target = driver.find_element_by_link_text("次の20件")
        target.click()
    except:
        break

getAddress()

# リストの値をテーブルのカラムへの格納
data = {
    'store_name': store_names,
    'score': scores,
    'review': reviews,
    'detail_url': detail_urls,
    'address': addresses
}
# テーブルを定義
df = pd.DataFrame(data)

df = df.replace(' - ', '0')

# テーブルをCSVファイルとして出力する
df.to_csv(
    outputfiles_dir + 'tabelog.csv', index=False)

print('終了')
