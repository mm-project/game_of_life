import sys
import os

#from colorama import Fore, Back, Style 
#class BioCell:
#    def __init__(self, posx, posy):
#        self.x = posx
#        self.y = posy
#        #self.is_alive = 1
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Renderer:
    def __init__(self):
        self.dummy = 1
        
    def render(self,w):
        os.system("clear")
        cells = w.get_cells()
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                #os.system("clear")
                if cells[i][j] is 1:
                    print(bcolors.WARNING + "X" + bcolors.ENDC,end='', flush=True)
                else:
                    print(" ", end='', flush=True)
            print()
        print()
        os.system("sleep 0.1")
