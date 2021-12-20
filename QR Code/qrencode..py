import pyqrcode 
from PIL import Image

# def encode():

s = " "
url = pyqrcode.create(s)
# url.png("pontotel.png", scale=8)

url.svg("1.svg", scale=10)

 
# def decode():
    # decodeQR = decode(Image.open('devfix.png'))
    # print(decodeQR[0].data.decode('ascii'))


