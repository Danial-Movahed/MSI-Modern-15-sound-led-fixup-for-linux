#!/usr/bin/env python3
import pulsectl
from time import sleep
from os import system, getuid
import pwd

pulse = pulsectl.Pulse('localhost')

def fixLedspeaker():
    global selSpeaker
    if pulse.sink_list()[selSpeaker].mute == 1:
        system("sudo /home/"+pwd.getpwuid(getuid()).pw_name+"/.local/bin/mutefixapi 44 228")
    else:
        system("sudo /home/"+pwd.getpwuid(getuid()).pw_name+"/.local/bin/mutefixapi 44 224")
def fixLed():
    global sel
    if pulse.source_list()[sel].mute == 1:
        system("sudo /home/"+pwd.getpwuid(getuid()).pw_name+"/.local/bin/mutefixapi 43 140")
    else:
        system("sudo /home/"+pwd.getpwuid(getuid()).pw_name+"/.local/bin/mutefixapi 43 136")
modeSpeaker=False
selSpeaker=1
mode=False
sel=1
while True:
    speakers=pulse.sink_list()
    defaultspeakers=pulse.server_info().default_sink_name
    for i in range(len(speakers)):
        if defaultspeakers == speakers[i].name:
            selSpeaker=i
            break
    if not modeSpeaker and speakers[selSpeaker].mute == 1:
        fixLedspeaker()
        modeSpeaker=not modeSpeaker
    elif modeSpeaker and speakers[selSpeaker].mute == 0:
        fixLedspeaker()
        modeSpeaker=not modeSpeaker
    mics=pulse.source_list()
    defaultmic=pulse.server_info().default_source_name
    for i in range(len(mics)):
        if defaultmic == mics[i].name:
            sel=i
            break
    if not mode and mics[sel].mute == 1:
        fixLed()
        mode=not mode
    elif mode and mics[sel].mute == 0:
        fixLed()
        mode=not mode
    sleep(0.2)
