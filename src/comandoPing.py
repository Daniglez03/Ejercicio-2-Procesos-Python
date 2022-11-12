import os
import platform

if platform.system() == 'Linux':

    def ping(host):
        command = os.system("ping -c 4 " + host)
    print(ping("8.8.8.8"))
