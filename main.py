# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : main.py
# @Date    : 2020-04-30 14:59:09
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0

import random
import time

import usb

from device_util import (create_bulk_device, get_bulk_interface, get_bulk_transfer_endpoint)
from message_util import create_color_fill_message
from sys_util import suspend_ni_backend_support

# white = 'ffffffff'
# black = '00000000'
# greenish = '0fa00fa0'
# gray = '75307530'
# brown = 'bfe3bfe3'
# blue = '2c2e2c2e'
# red = '04060406'
# orange = '080a080a'
# purple = '383a383a'
# cyan = '24262426'
# yellow = '14161416'
# mint = '20222022'
# green = '1c1e1c1e'

vid = 0x17cc  # ni id
pid = 0x1600  # maschine mk3 id
white = 65535
black = 0
greenish = 4000
gray = 33000
brown = 49123
blue = 11310
red = 1030
orange = 2058
purple = 14394
cyan = 9254
yellow = 5142
mint = 8226
green = 7198

colors = [white, black, gray, green, brown, blue, red, orange, purple, cyan, yellow, greenish, mint]


def color_test(color1=0, color2=0, bg_color=0):
    screen_width = 480
    screen_height = 272
    x_pos = 0
    y_pos = 0
    bg_message1 = create_color_fill_message(screen_index=0, color=bg_color, x_pos=x_pos, y_pos=y_pos, width=screen_width, height=screen_height)
    bg_message2 = create_color_fill_message(screen_index=1, color=bg_color, x_pos=x_pos, y_pos=y_pos, width=screen_width, height=screen_height)
    usb.util.claim_interface(device, interface)
    # draw backgroud
    device.write(endpoint, bg_message1)
    device.write(endpoint, bg_message2)
    time.sleep(0.1)
    usb.util.release_interface(device, interface)
    usb.util.dispose_resources(device)


if __name__ == "__main__":
    running = False
    if running:
        suspend_ni_backend_support()
    device = create_bulk_device(vid, pid)
    interface = get_bulk_interface(device)
    endpoint = get_bulk_transfer_endpoint(interface)
    for i in range(10):
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        bg_color = random.choice(colors)
        color_test(bg_color=bg_color)
        time.sleep(0.4)
    print('done')
