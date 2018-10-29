import sys
import os

#class BioCell:
#    def __init__(self, posx, posy):
#        self.x = posx
#        self.y = posy
#        #self.is_alive = 1
 

class World:
    def __init__(self):
        self.iteration = 0
        #self.n = 204
        #self.m = 51       
        self.n = 5
        self.m = 5
        self.cells = [[0 for x in range(self.n)] for y in range(self.m)] 
        self.cells[0][0] = 1
        self.cells[0][2] = 1
        self.cells[1][1] = 1
        self.cells[1][2] = 1     
        #self.cells[4][4] = 1
        #self.cells[4][5] = 1
        #self.cells[2][2] = 1
        self.alive_count = 4
        #self.to_be_born = []

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
            elif j is self.m-1:
                count = self.cells[i][j-1] + self.cells[i+1][j] + self.cells[i+1][j-1] 
            else:
                count = self.cells[i][j-1] + self.cells[i][j+1] + self.cells[i+1][j-1]+ self.cells[i+1][j] + self.cells[i+1][j+1] 
        elif i is self.n-1:
            if j is 0: 
                count = self.cells[i-1][j] + self.cells[i-1][j+1] + self.cells[i][j+1]  
            elif j is self.m-1:
                count = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i][j-1] 
            else:
                count = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i-1][j+1]  + self.cells[i][j-1] + self.cells[i][j+1]
        else:
            if j is 0: 
                count = self.cells[i-1][j] + self.cells[i+1][j] + self.cells[i][j+1] + self.cells[i-1][j+1] + self.cells[i+1][j+1]  
            elif j is self.m-1:
                count = self.cells[i-1][j] + self.cells[i+1][j] + self.cells[i][j-1] + self.cells[i-1][j-1] + self.cells[i+1][j-1]
            else:        
                for a in range(-1,0,1):
                    for b in range(-1,0,1):
                        count = count + self.cells[i+a][j+b]
        
        if count is not 0:
            print ("->count: ",count)
            #os.exit(1)
            
        return count
        
    def update(self):
        self.alive_count = 0
        to_be_born = []
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                print("inspecting element cell[",i,"][",j,"] = ",self.cells[i][j])
                if self.cells[i][j] is 1:
                    self.alive_count = self.alive_count + 1
                    
                num = self.get_num_neihboors(i,j)
                if ( self.cells[i][j] != 0 ) and ( num >= 4 or num <= 2 ):
                    self.cells[i][j] = 0   
                if ( self.cells[i][j] == 0 ) and ( num is 3  ):
                    to_be_born.append([i,j])
        
        for a,b in to_be_born:
            self.cells[a][b] = 1

        self.iteration = self.iteration + 1
    
    def get_cells(self):
        return self.cells
 
 
 
class Renderer:
    def __init__(self):
        self.dummy = 1
        
    def render(self,w):
        #os.system("sleep 1; clear")
        cells = w.get_cells()
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                #os.system("clear")
                print(cells[i][j], end='', flush=True)
            print()
        print()
   

r = Renderer() 
w = World()
while w.has_life() is not 0: 
    #r.render(w)
    w.update()
