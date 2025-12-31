# AWG-wofi
Набор скриптов для удобной работы с [`AmneziaWG`](https://github.com/amnezia-vpn/amneziawg-go) с помощью [`wofi`](https://github.com/SimplyCEO/wofi) в [`Arch Linux`](https://archlinux.org)
![](images/1.png)
## Установка зависимостей
```shell
sudo pacman -S git wofi polkit python bash libnotify python-pip
sudo systemctl enable --now polkit.service
```


## Установка AmneziaWG 
```shell
git clone https://aur.archlinux.org/yay.git && cd yay
makepkg -si

yay -S amneziawg-tools amneziawg-dkms
```

## Клонирование репозитория
```shell
git clone https://github.com/Flat447/AWG-wofi.git
cd AWG-wofi
python install.py
```
После этого можно использовать команду `wofi-vpn` либо запускать из любого лаунчера приложений скрипт AWG
