import deathbycaptcha
import time
import pyscreenshot as ImageGrab
from Xlib import display
x = 0
while x < 10:
    data = display.Display().screen().root.query_pointer()._data
    print data["root_x"]
    print data["root_y"]
    x = x + 1
    time.sleep(1)

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.save('im.png')


'''

# Put your DBC account username and password here.
# Use deathbycaptcha.HttpClient for HTTP API.
client = deathbycaptcha.SocketClient("ryan.cassels@hotmail.com", "nutella1234!")

try:
    balance = client.get_balance()
    print balance
    time.sleep(5)
    # Put your CAPTCHA file name or file-like object, and optional
    # solving timeout (in seconds) here:
    captcha = client.decode("2.jpg")
    if captcha:
        # The CAPTCHA was solved; captcha["captcha"] item holds its
        # numeric ID, and captcha["text"] item its text.
        print "CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"])

except deathbycaptcha.AccessDeniedException:
    print "error"
    # Access to DBC API denied, check your credentials and/or balance
'''
