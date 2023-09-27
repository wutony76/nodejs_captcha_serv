import ddddocr
import requests

ocr = ddddocr.DdddOcr()
# with open('1.png', 'rb') as f:
#   img_bytes = f.read()

# # print('img >>>', img_bytes)
# res = ocr.classification(img_bytes)
# print(res)


# pip uninstall Pillow
# pip install Pillow==9.5.0

pathFile = '1.png'
res = requests.get('http://35.241.102.47/credit-wapi/captcha?key=452491012', stream=True)

if res.status_code == 200:
  with open(pathFile,'wb') as file_path:
    for chunck in res:
      file_path.write(chunck)
  print("The Image has been downloaded")

  with open('1.png', 'rb') as f:
    img_bytes = f.read()
  res = ocr.classification(img_bytes)
  print(res)

else:
  print("Null")

