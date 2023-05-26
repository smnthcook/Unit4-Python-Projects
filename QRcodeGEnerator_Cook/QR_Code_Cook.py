'''
QR Code Generator
Samantha Cook
5/2/2023
Python II
'''

import qrcode

message = input("Enter your secret message! >> ")
image = qrcode.make(message)
image.save("secret_message.png")
print("Your QR code with the secret message was generated!")