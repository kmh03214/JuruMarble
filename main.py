import pygame
import os

current_dir = os.getcwd()


class ogu:
    def __init__(self,base_path):
        self.x, self.y = 0, 0
        self.sx, self.sy = 0, 0
        
        self.current_frame = 0
        self.cnt = 0
        self.base_path = base_path
        self.frames = os.listdir(base_path)
        self.frames_length = len(self.frames)

    def put_img(self):
        self.img = pygame.image.load(self.base_path + '/' + self.frames[self.cnt])
        self.sx, self.sy = self.img.get_size()
        self.cnt = (self.cnt+1)%self.frames_length

    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x,self.y))

class obj:
    def __init__(self):
        self.x, self.y = 0, 0
        self.move = 0
    def put_img(self,address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x,self.y))

    
        

# 1. game init
pygame.init()
# 2. game window config
# screen_width = 745
# screen_height = 526

screen_width = 1000
screen_height = 500


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("** Juru Mable **")

# 3. game config
clock =  pygame.time.Clock()


# background = pygame.image.load("/Users/myhwan/Python/JuruMarble/assets/background.jpeg")
# background = pygame.image.load("/Users/myhwan/Python/JuruMarble/assets/ogu.gif")

grid_size = (200,100)
grid = []
for gx in range(0,screen_width,grid_size[0]):
    a = []
    for gy in range(0,screen_width,grid_size[1]):
        a.append(pygame.Rect(gx,gy,grid_size[0],grid_size[1]))
    grid.append(a)

# for x in range(len(grid)):
#     for y in range(len(grid[0])):
#         print(grid[x][y].center)


# 4. main event
running = True
ogu1_path = current_dir + '/JuruMarble/assets/ogu1'
ogu2_path = current_dir + '/JuruMarble/assets/ogu2'
ogu1 = ogu(ogu1_path)
ogu2 = ogu(ogu2_path)

while running:
    # 4-1. FPS 
    clock.tick(10)
    # 4-2 event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 4-3 change over time
    # screen.blit(background, (0, 0))
    ogu1.put_img()
    ogu1.change_size(100,100)
    ogu2.x, ogu2.y = 100,100
    ogu2.put_img()
    ogu2.change_size(50,50)

    # 4-4 그리기
    ogu1.show()
    ogu2.show()
    pygame.display.update() # 게임화면 다시 그리기



# 5. game quit
pygame.quit()

