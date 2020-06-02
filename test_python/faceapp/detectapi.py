import requests
import json
import pprint
import base64
import pandas as pd

from PIL import Image, ImageDraw

from glob import glob


file_path = 'C:/Users/nakamura.yo/Documents/test_python/faceapp/images/Image from iOS.jpg'
savefile = 'C:/Users/nakamura.yo/Documents/test_python/faceapp/outputfiles/savefile'

url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

img_file = []
gender = []
age = []
beauty_male = []
beauty_female = []

# for input_file in file_path:
with open(file_path, 'rb') as f:
    img_file = base64.encodebytes(f.read())

config = {
    'api_key': '***',
    'api_secret': '***',
    'image_base64': img_file,
    'return_landmark': 1,
    'return_attributes': 'gender,age,beauty'
}
res = requests.post(url, data=config)

data = json.loads(res.text)

# Save json data to 'savefile'
with open(savefile + '.json', 'w') as f:
    json.dump(data, f, indent=4)

# Display the response data on the screen
data_json = json.dumps(data, indent=4)
# print(data_json)

for face in data['faces']:
    if 'attributes' in face:
        #face_token = face['face_token']
        #face_token = file_path
        gender.append(face['attributes']['gender']['value'])
        age.append(face['attributes']['age']['value'])
        beauty_male.append(face['attributes']['beauty']['male_score'])
        beauty_female.append(face['attributes']['beauty']['female_score'])

# テーブルへの格納
data_culums = {
    'file_path': file_path,
    'gender': gender,
    'age': age,
    'beauty_male': beauty_male,
    'beauty_female': beauty_female
}

df = pd.DataFrame(data_culums, index=['i', ])

print(df)
