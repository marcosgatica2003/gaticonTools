#!/bin/bash

function instalacionDebian {
    echo "En breve"
}

function instalacionArchLinux {
    echo "PROCESO 1: ACTUALIZACIÓN"
    pacman -Syu

    echo "PREPARACIÓN: CONFIGURAR LAS VELOCIDADES DEL CPU Y VENTILADORES"
    pacman -S lm_sensors cpupower
    cpupower frequency-set --governor powersave --min 800MHz --max 1.60GHz
    pwmconfig

    echo "PROCESO 2: INSTALACIÓN DE PAQUETES BASE"
    pacman -S alacritty tmux vim i3-wm git sudo polybar dunst xorg xinit feh evince base-devel flameshot openssh sshfs texlive-full ttf-font-awesome ttf-hack-nerd rofi discord eom zathura zathura-pdf-poppler 

    echo "PROCESO 3: INSTALACIÓN DE YAY"
    git clone https://aur.archlinux.org/yay.git /tmp/  && makepkg -si /tmp/yay 

    echo "PROCESO 4: INSTALACIÓN DE PAQUETES YAY"
    yay -Syu
    yay -S librewolf-bin simplescreenrecorder latexmk

    echo "PROCESO 5: INSTALACIÓN DE ARCHIVOS CONFIG"
    cp -r ../configVIM/vimrc $HOME/.vimrc
    mkdir -p $HOME/.vim/templates
    mkdir -p $HOME/.vim/spell
    cp -r ../configVIM/plantillasVIM/* $HOME/.vim/templates
    cp -r ../configVIM/diccionarios* $HOME/.vim/spell

    cp -r ../configuracionesEsenciales/zshrc $HOME/.zshrc
    cp -r ../configuracionesEsenciales/config/* $HOME/.config/
    cp -r ../configuracionesEsenciales/tmux.conf $HOME/.tmux.conf

    mkdir -p $HOME/.config/configuracionesRofi
    cp -r ../configuracionesRofi/* $HOME/.config/configuracionesRofi
    
    mkdir -p $HOME/Wallpapers
    cp ../configuracionesEsenciales/wallpapers.tar.gz $HOME/Wallpapers/
    tar $HOME/Wallpapers/wallpapers.tar.gz
    rm $HOME/Wallpapers/wallpapers.tar.gz

    echo "TERMINADO!"

}

echo -e "---------------------------------------------"
echo -e "| Script de instalación  de mi sistema base |"
echo -e "---------------------------------------------"

echo "Sistema base: "

if [ -f /etc/debian_version ]; then
    sistemaBase=2 
    echo "Debian"
    sleep 2
elif [ -f /etc/arch-release ]; then
    sistemaBase=1
    echo "Arch Linux"
    sleep 2
    instalacionArchLinux()
else
	echo "Sistema no soportado"
	exit 1
fi
echo -e "---------------------------------------------"


