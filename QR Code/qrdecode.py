from PIL import Image
from pyzbar.pyzbar import decode




decodeQR = decode(Image.open('devfix.png'))

print(decodeQR[0].data.decode('ascii'))
