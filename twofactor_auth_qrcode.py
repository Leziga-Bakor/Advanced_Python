import pyotp
import qrcode

key = 'letsdothis'

# Make sure to install qrcode with pip install qrcode

# uri = pyotp.totp.TOTP(key).provisioning_uri(name='Username', 
#                                             issuer_name='lhi App')

# print(uri)

# qrcode.make(uri).save("totp.png")

totp = pyotp.TOTP(key)
while True:
    print(totp.verify(input('Enter code: ')))