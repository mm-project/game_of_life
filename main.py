from libs.renderer import Renderer
from libs.world import World

r = Renderer() 
w = World()
while w.has_life() is not 0: 
    r.render(w)
    w.update()



