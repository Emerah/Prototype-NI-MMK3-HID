# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : main.py
# @Date    : 2020-04-30 14:59:09
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0

from sys_util import suspend_ni_backend_support
from device_util import create_bulk_device, get_bulk_interface, get_bulk_transfer_endpoint
from message_util import fill_screen_with_color
import usb
import random
import time

vid = 0x17cc  # ni id
pid = 0x1600  # maschine mk3 id
white = 'ffffffff'
black = '00000000'
greenish = '0fa00fa0'
gray = '75307530'
brown = 'bfe3bfe3'
blue = '2c2e2c2e'
red = '04060406'
orange = '080a080a'
purple = '383a383a'
cyan = '24262426'
yellow = '14161416'
mint = '20222022'
green = '1c1e1c1e'
colors = [white, black, gray, green, brown, blue, red, orange, purple, cyan, yellow, greenish, mint]


if __name__ == "__main__":
    running = False
    if running:
        suspend_ni_backend_support()
    device = create_bulk_device(vid, pid)
    interface = get_bulk_interface(device)
    endpoint = get_bulk_transfer_endpoint(interface)
    usb.util.claim_interface(device, interface)
    for i in range(20):
        color = random.choice(colors)
        m1, m2 = fill_screen_with_color(color)
        device.write(endpoint, m1)
        device.write(endpoint, m2)
        time.sleep(0.50)
    usb.util.release_interface(device, interface)
    usb.util.dispose_resources(device)
    print('done')
