# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : message_util.py
# @Date    : 2020-04-30 18:30:07
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0


def fill_screen_with_color(color):
    msg1 = '84000060000000000000000001e001100100ff00{}0300000040000000'.format(color)
    msg2 = '84000160000000000000000001e001100100ff00{}0300000040000100'.format(color)
    m1 = bytes.fromhex(msg1)
    m2 = bytes.fromhex(msg2)
    return (m1, m2)


def create_message(screen, data, x_pos, y_pos, width, height):
    return create_message_header(screen, x_pos, y_pos, width, height)


def create_message_header(screen, x_pos, y_pos, width, height):
    header = create_message_header(screen, x_pos, y_pos, width, height)
    print(header)
