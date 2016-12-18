#! /bin/bash

# This is a new system bootstraping script. It takes the dotfiles in this
# directory and installs them onto the system, if the system is running
# the apt package manager then it also installs various utilities.

has_apt=$(which apt-get)

if [ "$has_apt" -eq "" ]; then
  echo "No apt-get on this system. Packages will not be installed."
else
  sudo apt-get install build-essential make nasm gdb vim binutils tmux python git 
fi

echo "Moving local dotfiles to their places ..."
cp .vimrc .gdbinit .tmux.conf .bashrc ~/
echo "Done."

