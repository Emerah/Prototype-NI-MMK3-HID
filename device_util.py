# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : device_util.py
# @Date    : 2020-04-30 16:07:59
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0


import usb


def create_bulk_device(vid, pid):
    device = usb.core.find(idVendor=vid, idProduct=pid)
    assert device is not None
    device.set_configuration()
    return device


def _get_correct_interface_index_for_device(device_name):
    if device_name == 'Maschine MK3':
        interface_index = 5
        return interface_index
    elif device_name == 'KOMPLETE KONTROL S49 NK2':
        interface_index = 3
        return interface_index
    else:
        print('wrong interface number was supplied')
        return


def get_bulk_interface(device):
    config = device.get_active_configuration()
    # account for maschine and komplete
    index = _get_correct_interface_index_for_device(device.product)
    interface = config[(index, 0)]
    assert interface is not None
    return interface


def get_bulk_transfer_endpoint(interface):
    endpoint = usb.util.find_descriptor(interface, custom_match=lambda ep: usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_OUT)
    assert endpoint is not None
    return endpoint
