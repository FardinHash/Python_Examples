# libraries
import pyqrcode
import png

QRtext = input(print('Enter text to generate QR: '))

QRimg = input(print('Enter image name to save: '))

QRimg = QRimg + '.png'

FinalQR = pyqrcode.create(QRtext)

FinalQR.show()
FinalQR.png(QRimg, scale=6)
