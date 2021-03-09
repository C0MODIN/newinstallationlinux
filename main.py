import os
from pynput.keyboard import Key, Controller

keyboard = Controller()

#Update system

os.system('sudo apt update')

#Install repository
os.system('sudo add-apt-repository ppa:graphics-drivers/ppa') #NVIDIA Repo
keyboard.press(Key.enter)
keyboard.release(Key.enter)

os.system('sudo add-apt-repository -y ppa:webupd8team/haguichi') #GUI for hamachi
keyboard.press(Key.enter)
keyboard.release(Key.enter)

os.system('sudo add-apt-repository ppa:lutris-team/lutris') #Plataform for games
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#Packages installation. Replace/add package do you want to install.

packages = "packages.txt"

with open(packages) as f:
    pkg = f.read()

os.system(f'sudo apt install {pkg}')

keyboard.press('s')
keyboard.release('s')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#installation from external software

os.system('wget -P config/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('wget -P config/ https://cdn.cloudflare.steamstatic.com/client/installer/steam.deb')
os.system('wget -O config/discord.deb https://discordapp.com/api/download?platform=linux&format=deb')
os.system('wget -P config/ https://www.vpn.net/installers/logmein-hamachi_2.1.0.203-1_amd64.deb')

os.system('sudo dpkg -i config/*.deb')
os.system('sudo apt install -f')
os.system('sudo dpkg -i config/*.deb')
os.system('rm config/*.deb')

#Python pip install
#os.system('pip3 install pygame')

#Git installation
os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"') #OH_MY_ZSH
os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')


#Fonts
os.system('wget -P /usr/share/fonts/ https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf')
os.system('wget -P /usr/share/fonts/ https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf')
os.system('wget -P /usr/share/fonts/ https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf')
os.system('wget -P /usr/share/fonts/ https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf')


#Configuration of system grub(only nvidia) like zsh tmux etc...

config_zsh = 'config/.zshrc'
config_bash = 'config/.bashrc'
config_p10k = 'config/.p10k.zsh'
testfile = 'packages.txt'

os.system('mkdir ~/.myosconfig')
os.system('cp config/kdeneonblack.svg config/kdeneonwhite.svg ~/.myosconfig')

os.system('cp config/.zshrc ~/.zshrc')
os.system('cp config/.bashrc ~/.bashrc')
os.system('cp config/.p10k.zsh ~/.p10k.zsh')

#Final
os.system('sudo apt autoremove')
keyboard.press('s')
keyboard.release('s')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
