class Renderer:
    def __init__(self):
        self.dummy = 1
        
    def render(self,w):
        os.system("sleep 1; clear")
        cells = w.get_cells()
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                #os.system("clear")
                print(cells[i][j], end='', flush=True)
            print()
        print()
   
