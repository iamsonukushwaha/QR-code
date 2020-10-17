import pyqrcode

data = 'https://singlebucks.blogspot.com/'

img = pyqrcode.create(data)

img.png('website.png',scale = 10)