# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : message_util.py
# @Date    : 2020-04-30 18:30:07
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0


def create_color_fill_message(screen_index, color, x_pos, y_pos, width, height):
    header = create_message_header(screen_index, x_pos, y_pos, width, height)
    repeat_command = repeat_pixels(int(width*height/2), color, color)
    blit = blit_command()
    end_transfer = end_transfer_command(screen_index)
    return header + repeat_command + blit + end_transfer


def create_message_header(screen, x_pos, y_pos, width, height):
    start_transfer = bytes.fromhex('8400')
    screen_index = screen.to_bytes(1, 'big')
    fixed_key = bytes.fromhex('6000000000')
    x_pos = x_pos.to_bytes(2, 'big')
    y_pos = y_pos.to_bytes(2, 'big')
    width = width.to_bytes(2, 'big')
    height = height.to_bytes(2, 'big')
    header = start_transfer + screen_index + fixed_key + x_pos + y_pos + width + height
    return header


def repeat_pixels(count, pixel1, pixel2):
    header = bytes.fromhex('0100')
    count = count.to_bytes(2, 'big')
    pixel1 = pixel1.to_bytes(2, 'big')
    pixel2 = pixel2.to_bytes(2, 'big')
    return header + count + pixel1 + pixel2


def blit_command():
    command = bytes.fromhex('03000000')
    return command


def end_transfer_command(screen):
    header = bytes.fromhex('4000')
    parameter1 = screen.to_bytes(1, 'big')
    parameter2 = bytes.fromhex('00')
    return header + parameter1 + parameter2
