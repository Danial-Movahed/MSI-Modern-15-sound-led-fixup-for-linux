#!/bin/bash
set -e
mkdir -p /home/$USER/.local/bin
cp mutefixapi /home/$USER/.local/bin
cp muteledctl.py /home/$USER/.local/bin/muteledctl
echo "/home/${USER}/.local/bin/muteledctl" >> /home/$USER/.profile
echo "${USER} ALL=(ALL) NOPASSWD: /home/${USER}/.local/bin/muteledctl" | pkexec env EDITOR="tee -a" visudo
chmod +x /home/$USER/.local/bin/muteledctl
/home/$USER/.local/bin/muteledctl &
notify-send "MSI Keyboard led fix has been installed!"
