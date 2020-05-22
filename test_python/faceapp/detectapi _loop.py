import requests
import json
import pprint
import base64
import pandas as pd

from PIL import Image, ImageDraw

import glob

url = 'https://api-us.faceplusplus.com/facepp/v3/detect'


#img_file =[]


gender = []
age = []
beauty_male = []
beauty_female = []
i = 0


#file_path = 'C:/Users/nakamura.yo/Documents/test_python/faceapp/images/1030.L.jpg'
#savefile =  'C:/Users/nakamura.yo/Documents/test_python/faceapp/outputfiles/savefile'


file_path = glob.glob(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\images\*')


list_df = pd.DataFrame(
    columns=['file_path', 'gender', 'age', 'beauty_male', 'beauty_female'])


# ファイル分繰り返す
for input_file in file_path:
    i += 1
    # print(input_file)
    with open(input_file, 'rb') as f:
        img_file = base64.encodebytes(f.read())

    # print(img_file)

    # config
    config = {
        'api_key': 'PUQy6dGCzDwmqEdT1g6zXZwATyzNqYlO',
        'api_secret': 'QdODMy8Lq087Xv-85vzDLtOJmltTdMQh',
        'image_base64': img_file,
        'return_landmark': 1,
        'return_attributes': 'gender,age,beauty'
    }

    # APIをPOSTする
    res = requests.post(url, data=config)

    # LOADする
    data = json.loads(res.text)

    # DUMPする
    data_json = json.dumps(data, indent=4)

    # カラムにjsonデータを格納する
    for face in data['faces']:
        if 'attributes' in face:
            gender = face['attributes']['gender']['value']
            age = face['attributes']['age']['value']
            beauty_male = face['attributes']['beauty']['male_score']
            beauty_female = face['attributes']['beauty']['female_score']
        else:
            gender = None
            age = None
            beauty_male = None
            beauty_female = None

        temp_se = pd.Series(
            [input_file, gender, age, beauty_male, beauty_female], index=list_df.columns)
        list_df = list_df.append(temp_se, ignore_index=True)

list_df.to_csv(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\detectapi.csv')
print('finish')


'''


url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

img_file =[]
gender = []
age = []
beauty_male = []
beauty_female = []




#for input_file in file_path:
with open(file_path, 'rb') as f:
    img_file=base64.encodebytes(f.read())

config = {
    'api_key': 'PUQy6dGCzDwmqEdT1g6zXZwATyzNqYlO',
    'api_secret': 'QdODMy8Lq087Xv-85vzDLtOJmltTdMQh',
    'image_base64': img_file,
    'return_landmark': 1,
    'return_attributes':'gender,age,beauty'
    }
res = requests.post(url, data=config)

data = json.loads(res.text)

# Save json data to 'savefile'
#with open(savefile + '.json', 'w') as f:
 #   json.dump(data, f, indent=4)
    
# Display the response data on the screen
data_json = json.dumps(data, indent=4)
#print(data_json)

for face in data['faces']:
    if 'attributes' in face:
        #face_token = face['face_token']
        #face_token = file_path
        gender.append(face['attributes']['gender']['value'])
        age.append(face['attributes']['age']['value'])
        beauty_male.append(face['attributes']['beauty']['male_score'])
        beauty_female.append(face['attributes']['beauty']['female_score'])

#テーブルへの格納
data_culums = {
    'file_path':file_path,
    'gender': gender,
    'age': age,
    'beauty_male': beauty_male,
    'beauty_female': beauty_female
    }

df = pd.DataFrame(data_culums, index=['i',])

print(df)


'''
