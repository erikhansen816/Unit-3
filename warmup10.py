#Erik Hansen
#10/5/2017
#dotsDemo.py

from ggame import *

red = Color(0xFF0000,.5)
red1 = Color(0xFF0000,.8)

triangle1 = PolygonAsset([(40,10),(60,40),(20,40)],LineStyle(1,red),red)
triangle2 = PolygonAsset([(40,55),(60,25),(20,25)],LineStyle(1,red),red1)
for j in range(10):
    for i in range(20):
        Sprite(triangle1,(20 + 50*i, 20 + 50*j))
        Sprite(triangle2,(20 + 50*i, 20 + 50*j))
App().run()
