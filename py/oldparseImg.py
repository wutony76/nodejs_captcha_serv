from __future__ import print_function
import os, sys
import ddddocr
import requests

def parseImg(url):
  
  ocr = ddddocr.DdddOcr()
  pathFile = '1.png'
  res = requests.get('http://' + url, stream=True)

  if res.status_code == 200:
    with open(pathFile,'wb') as file_path:
      for chunck in res:
        file_path.write(chunck)
    print("The Image has been downloaded")

    with open(pathFile, 'rb') as f:
      img_bytes = f.read()
    res = ocr.classification(img_bytes)
    # print(res)
    return res


def main():
  print('run main')
  argv = list(sys.argv)
  url = argv[1]
  # output = parseImg(url)
  print('python print')
  print(url)


if __name__ == "__main__":
  print('start.run.py')
  main()