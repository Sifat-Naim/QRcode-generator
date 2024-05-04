import qrcode as qr
link = input("Give a link: ")
img= qr.make(link)
img.save('QR.png')