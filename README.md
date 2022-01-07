# MSI Modern 15 sound led fixup for linuxA simple program to fix the MSI Modern 15 speaker and microphone mute LEDs.# Installation## Requirements[`pulsectl`](https://pypi.org/project/pulsectl) module for python
## Instructions
Clone the repository:

```git clone https://github.com/Danial-Movahed/MSI-Modern-15-sound-led-fixup-for-linux.git```
Double click install.sh

After the installation is finished, a notification will pop up.

# Known bugs### Delay between button press and let state changingThere is a delay of 0.2 at the end of muteledctl.py. This is to reduce the CPU usage when the neither of the buttons are pressed.# Credits[YodyPa](https://github.com/YoyPa) for [isw](https://github.com/YoyPa/isw): A program for controlling the fans in MSI laptops (Bits of code where used from this project)