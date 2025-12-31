#!/bin/python3

import os

os.system("sudo mkdir /etc/amnezia/amneziawg 2> /dev/null; sudo cp src/WARP.conf /etc/amnezia/amneziawg; sudo cp src/vpn-dns-helper src/vpn-up src/vpn-down src/wofi-vpn /usr/local/bin; sudo cp src/wofi-vpn.desktop /usr/share/applications; sudo cp src/awg.png /usr/share/icons; sudo chmod 777 /usr/local/bin/*; echo \"Установка завершена\"")
