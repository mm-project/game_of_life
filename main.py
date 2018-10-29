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
    
class World:
    def __init__(self):
        self.iteration = 0
        #self.n = 204
        #self.m = 51       
        self.n = 200
        self.m = 53
        self.cells = [[0 for x in range(self.n)] for y in range(self.m)] 
        self.cells[20][21] = 1
        self.cells[21][22] = 1
        self.cells[22][20] = 1
        self.cells[22][21] = 1
        self.cells[22][22] = 1
        self.alive_count = 5

    def has_life(self):
        if self.alive_count > 0:
            print("-----> iteration: ",self.iteration," cells:",self.alive_count)
            return 1
        return 0
    
    def get_num_neihboors(self,i,j):
        #print("-getting neibhorhood info cell[",i,"][",j,"] = ",self.cells[i][j])
        count = 0
        if i is 0:
            if j is 0:
                count = self.cells[i+1][j] + self.cells[i][j+1] + self.cells[i+1][j+1] 
            elif j is self.n-1:
                count = self.cells[i][j-1] + self.cells[i+1][j] + self.cells[i+1][j-1] 
            else:
                #print("-getting neibhorhood info cell[",i,"][",j,"] = ",self.cells[i][j])
                count = self.cells[i][j-1]
                count = count + self.cells[i][j+1] 
                count = count + self.cells[i+1][j+1] 
                count = count + self.cells[i+1][j] 
                count = count + self.cells[i+1][j-1]  
        elif i is self.m-1:
            if j is 0: 
                count = self.cells[i-1][j] + self.cells[i-1][j+1] + self.cells[i][j+1]  
            elif j is self.n-1:
                count = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i][j-1] 
            else:
                count = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i-1][j+1]  + self.cells[i][j-1] + self.cells[i][j+1]
        else:
            if j is 0: 
                count = self.cells[i-1][j] + self.cells[i+1][j] + self.cells[i][j+1] + self.cells[i-1][j+1] + self.cells[i+1][j+1]  
            elif j is self.n-1:
                count = self.cells[i-1][j] + self.cells[i+1][j] + self.cells[i][j-1] + self.cells[i-1][j-1] + self.cells[i+1][j-1]
            else:        
                count = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i-1][j+1] + self.cells[i][j+1]
                count = count + self.cells[i+1][j+1] + self.cells[i+1][j] + self.cells[i-1][j-1] + self.cells[i][j-1] 
                #FIXME
                #print("here--")
                #for a in range(-1,0,1):
                #    for b in range(-1,0,1):
                #        print("----->cell[",i+a,"][",j+b,"]") 
                #        count = count + self.cells[i+a][j+b]
        
        #if count is not 0:
        #    print ("->neibhoors count: ",count)
        #else:
        #    print ("->count: no neibhoors")
            
        return count
        
    def update(self):
        self.alive_count = 0
        to_be_born = []
        to_be_died = []
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                #print("inspecting element cell[",i,"][",j,"] = ",self.cells[i][j])
                if self.cells[i][j] is 1:
                    self.alive_count = self.alive_count + 1
                    
                num = self.get_num_neihboors(i,j)
                if ( self.cells[i][j] != 0 ) and ( num >= 3 or num < 2 ):
                    #print("->will be killed:")
                    to_be_died.append([i,j])
                if ( self.cells[i][j] == 0 ) and ( num is 2  ):
                    #print("->will be born:")
                    to_be_born.append([i,j])
                
                #print()
        
        #print("Creating...")
        for a,b in to_be_born:
            #print("->cell[",a,"][",b,"]") 
            self.cells[a][b] = 1
        
        #print("Erasing...")
        for a,b in to_be_died:
            #print("->cell[",a,"][",b,"]") 
            self.cells[a][b] = 0
        
        self.iteration = self.iteration + 1
        
    
    def get_cells(self):
        return self.cells
 
 
 
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
                    print(bcolors.WARNING + "1" + bcolors.ENDC,end='', flush=True)
                else:
                    print(0, end='', flush=True)
            print()
        print()
        os.system("sleep 0.1")
   

r = Renderer() 
w = World()
#w.update()
while w.has_life() is not 0: 
    r.render(w)
    w.update()
