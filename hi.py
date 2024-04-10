def __init__(self, x, y):
		self.images_right=[]
		self.images_left=[]
		self.index=0
		self.counter=0
		for num in range(1,5):
			img_right=pygame.image.load(f'img/guy{num}.png')
			img_right=pygame.transform.scale(img_right,(40,80))
			img_left= pygame.transform.flip(img_right,True,False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.dead_image=pygame.image.load("img/ghost.png")
		self.image= self.images_right[self.index]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.width=self.image.get_width()
		self.height=self.image.get_height()
		self.vel_y=0
		self.jumped=False 
		self.direction=0