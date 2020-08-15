import os

#Update system
os.system('sudo apt update')
print("Actualizando paquetes")
#Packages installation

pkg = ["git","meson","cmake","zsh","neovim","cpu-x","scrcpy","libreoffice","libreoffice-plasma"]
#print(pkg[0])

for packages in pkg:
    os.system(f'sudo apt install {packages}')

#Git installation
