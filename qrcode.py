import pyqrcode
import sys
import re

data = sys.argv[1]

img = pyqrcode.create(data)

# Extract the domain name from data
domain_name = re.sub(r'https?://(www\.)?', '', data).split('/')[0]

img.png(domain_name + '.png', scale = 10)

print('QR code generated successfully')
