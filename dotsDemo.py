#Erik Hansen
#10/5/2017
#dotsDemo.py

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(10):
    for i in range(20):
        Sprite(dot,(20 + 50*i, 20 + 50*j))
App().run()
