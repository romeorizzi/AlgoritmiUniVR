#!/usr/bin/python
import os
from sys import stderr, exit, argv
import datetime

os.system(f'date +"%Y-%m-%d_%B  %A%ttime: %H:%M" >> ./go.log')
os.system(f'echo " algo class goalgo.py" >> ./go.log')
os.system(f'echo >> ./go.log')
os.system(f'google-chrome https://wbo.ophir.dev/boards/algo{str(datetime.date.today())}_1')
os.system(f'google-chrome --new-window https://etherpad.wikimedia.org/p/algo_meetings{str(datetime.date.today())[:4]}')
os.system(f'google-chrome https://etherpad.wikimedia.org/p/algo{str(datetime.date.today())}')
os.system(f'google-chrome https://univr.zoom.us/j/94457731757')

os.system('echo URLs:')
os.system('echo " - Zoom algo room: https://univr.zoom.us/j/94457731757"')
os.system(f'echo " - Etherpad algo index page: https://etherpad.wikimedia.org/p/algo_meetings{str(datetime.date.today())[:4]}"')
os.system(f'echo " - Etherpad meeting report: https://etherpad.wikimedia.org/p/algo{str(datetime.date.today())}"')
os.system(f'echo " - Collaborative WhiteBoard: https://etherpad.wikimedia.org/p/algo{str(datetime.date.today())}_1"')
