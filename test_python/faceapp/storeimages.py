# スクレイピング
import requests
from bs4 import BeautifulSoup
import os
# pandas
import pandas as pd
# detectapi
import json
import pprint
import base64

# スクレイピング対象のURL
url = 'https://www.stardust.co.jp/stardustplanet/'

headers = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
images = []
names = []
files_path = []

#df = pd.DataFrame(columns=['name','image_url','file_path'])

# 画像URLの取得
for image_url in soup.select('div > img'):
    #print('http:'+ image_url.get('src'))
    images.append('http:' + image_url.get('src'))

# 人物名の取得
for name in soup.select('div > img'):
    # print(name.get('alt'))
    names.append(name.get('alt'))

# 画像URLをローカルファイルとして保存する
for target in images:
    re = requests.get(target)
    files_path.append(
        'C:/Users/nakamura.yo/Documents/test_python/faceapp/images/' + target.split('/')[-1])
    with open('C:/Users/nakamura.yo/Documents/test_python/faceapp/images/' + target.split('/')[-1], 'wb') as f:
        f.write(re.content)

    #temp_se = pd.Series([name,image_url,files_path], index=df.columns)
    #df = df.append(temp_se,ignore_index=True)


# テーブルへの格納
data = {
    'name': names,
    'image_url': images,
    'file_path': files_path
}

df = pd.DataFrame(data)

df.to_csv(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\storeimages.csv')

print('終了')
