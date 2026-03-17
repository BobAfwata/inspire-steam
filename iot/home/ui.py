import network
import time
from machine import Pin, I2C
import ssd1306
import urequests

# OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Buttons
btn_up = Pin(10, Pin.IN, Pin.PULL_UP)
btn_down = Pin(11, Pin.IN, Pin.PULL_UP)
btn_select = Pin(12, Pin.IN, Pin.PULL_UP)

# WiFi credentials
SSID = "Wokwi-GUEST"
PASSWORD = ""

# Device states
light = False
fan = False

# Screen states
HOME = 0
LIGHT = 1
FAN = 2
WIFI = 3

state = HOME

# WIFI CONNECT
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        time.sleep(1)

    return wlan.ifconfig()[0]

ip = connect_wifi()

# API CONTROL
def send_command(device, value):
    try:
        url = "http://example.com/device"
        data = {"device":device,"state":value}
        urequests.post(url,json=data)
    except:
        pass

# DRAW SCREENS
def draw_home():
    oled.fill(0)
    oled.text("HOME AUTOMATION",0,0)
    oled.text("Light:"+str(light),0,20)
    oled.text("Fan:"+str(fan),0,30)
    oled.show()

def draw_light():
    oled.fill(0)
    oled.text("LIGHT CONTROL",0,0)
    oled.text("State:",0,20)

    if light:
        oled.text("ON",50,20)
    else:
        oled.text("OFF",50,20)

    oled.show()

def draw_fan():
    oled.fill(0)
    oled.text("FAN CONTROL",0,0)
    oled.text("State:",0,20)

    if fan:
        oled.text("ON",50,20)
    else:
        oled.text("OFF",50,20)

    oled.show()

def draw_wifi():
    oled.fill(0)
    oled.text("WIFI STATUS",0,0)
    oled.text(ip,0,20)
    oled.show()

# MAIN LOOP
while True:

    # NEXT SCREEN
    if not btn_up.value():
        state += 1
        if state > WIFI:
            state = HOME
        time.sleep(0.3)

    # PREVIOUS SCREEN
    if not btn_down.value():
        state -= 1
        if state < HOME:
            state = WIFI
        time.sleep(0.3)

    # SELECT ACTION
    if not btn_select.value():

        if state == LIGHT:
            light = not light
            send_command("light",light)

        if state == FAN:
            fan = not fan
            send_command("fan",fan)

        time.sleep(0.3)

    # DISPLAY STATE
    if state == HOME:
        draw_home()

    elif state == LIGHT:
        draw_light()

    elif state == FAN:
        draw_fan()

    elif state == WIFI:
        draw_wifi()

    time.sleep(0.1)