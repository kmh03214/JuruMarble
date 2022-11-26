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
        self.sx, self.sy = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x,self.y))

if __name__ == "__main__":
    print(1)
    