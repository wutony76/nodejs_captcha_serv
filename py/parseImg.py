from __future__ import print_function
import os, sys, socket
import requests
import ddddocr
import getpass

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# print('*ttt BASE_DIR', BASE_DIR)
HOST_NAME = socket.gethostname() # 主機名稱
USER_NAME = getpass.getuser() # 用戶名稱
BASE = '/Users'
# /Users/tony.wu/Downloads
# DOWNLOADS_PATH = os.path.join(BASE, USER_NAME,'Downloads','vcode.png') 
DOWNLOADS_PATH = os.path.join(BASE, USER_NAME,'Downloads') 
# print('*ttt DOWNLOADS_PATH', DOWNLOADS_PATH)

def checkImg(pathFile):
  file = os.path.join(DOWNLOADS_PATH, pathFile) 
  # print ('isfile > ', file, os.path.isfile(file))
  if os.path.isfile(file) == False:
    return -1

  ocr = ddddocr.DdddOcr()
  with open(file, 'rb') as f:
    img_bytes = f.read()
  res = ocr.classification(img_bytes)
  # print(res)
  # os.rmdir(DOWNLOADS_PATH)
  return res

def parseImg(url):
  httpUrl = 'http://' + url
  res = requests.get(httpUrl, stream=True)
  if res.status_code == 200:
    # print('img.res = ', res)
    pathFile = '1.png'
    ocr = ddddocr.DdddOcr()

    # 驗證圖片
    with open(pathFile,'wb') as file_path:
      for chunck in res:
        file_path.write(chunck)
    # print("The Image has been downloaded")

    with open(pathFile, 'rb') as f:
      img_bytes = f.read()
    res = ocr.classification(img_bytes)
    # print(res)
    return res

    # return res

def testLogin(): 
  print('start.testLogin')
  url = 'http://35.241.102.47/credit-wapi/wapi/login' #dev
  headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
  params = {
    "cmd":"login",
    "username":"newt06m003",
    "password":"/QCYkDagdMbokSCjCoMldXYEdDg: ",
    "key":472275467,
    "code":"1257",
    "loginUrl":"http://devuser.zzsjhhb.com",
    "salt":1695714354640,
    "clientType":1,
    "reqId":"957143546417504512",
    "version":"1.0",
    "sn":"",
    "token":"948bd710a750e0bb1cc0c6f5544a2964TEST","channel":"CDT_PC",
    "identity":"957143546417504512"
    }
  # {"cmd":"login","username":"newt06m003","password":"/QCYkDagdMbokSCjCoMldXYEdDg: ","key":472275467,"code":"1257","loginUrl":"http://devuser.zzsjhhb.com","salt":1695714354640,"clientType":1,"reqId":"957143546417504512","version":"1.0","sn":"","token":"948bd710a750e0bb1cc0c6f5544a2964TEST","channel":"CDT_PC","identity":"957143546417504512"}
  r = requests.post(url, data = params, headers = headers)
  print (r.text)

def main():
  argv = list(sys.argv)
  imgName = None
  if len(argv) > 1:
    imgName = argv[1] + '.png'
  # # print('run main.test123', len(argv), url)
  # # print('img.url = ', url)
  # result = parseImg(url)
  # # print('img.result = ', result)
  # print(result)

  result = checkImg(imgName)
  print(result)

  # testLogin()

if __name__ == "__main__":
  main()