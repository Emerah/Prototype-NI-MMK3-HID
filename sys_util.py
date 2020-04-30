# -*- coding: utf-8 -*-
# @Project : MMK3-HID-Control
# @File	   : sys_util.py
# @Date    : 2020-04-30 15:17:00
# @Author  : Emerah (MaXaR) - ahmed.emerah@icloud.com
# @Link    : https://github.com/Emerah
# @Version : 1.0.0

import os
import re
import subprocess


def process_is_currently_active(process):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for i in s.stdout:
        if re.search(process, i):
            return True
    return False


def suspend_ni_backend_support():
    processes = [b'NIHardwareAgent', b'NIHostIntegrationAgent', b'NTKDaemon']
    request_presmission_message = 'for this to work, we must suspend natinve instruments services. do you agree? (y/n)?: '
    response = input(request_presmission_message)
    if response.lower() == 'yes' or response == 'y':
        for process in processes:
            if process_is_currently_active(process):
                proc = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
                result, err = proc.communicate()
                for line in result.splitlines():
                    if process in line:
                        pid = int(line.split(None, 1)[0])
                        res = os.system('kill -9 ' + str(pid))
                        if res == 0:
                            print('{} has been suspended'.format(str(process)))
            else:
                print('{} was not running'.format(str(process)))
    elif response.lower() == 'no' or response.lower() == 'n':
        print('you chose no .. unfortunately we can not access the device now.')
    else:
        print('this did not make sense. answer can be y or n ?')
    print('exiting with grace')
