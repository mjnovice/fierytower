import pygame
import random

# This class represents the platform we jump on
class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		Ball.image=pygame.image.load('ball.png')
		self.image=Ball.image
		self.rect=self.image.get_rect()
	

class Platform (pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		Platform.image=pygame.image.load('ter.png')		
		self.image = Platform.image		
		#self.image = pygame.Surface([width, height])
		#self.image.fill(color)
		self.rect = self.image.get_rect()
# This class represents the Player at the bottom that the user controls
class Player(pygame.sprite.Sprite):
	# -- Attributes
	# Set speed vector of player
	change_x=0
	change_y=0
	# Triggered if the player wants to jump.
	jump_ready = False
	# Count of frames since the player hit 'jump' and we
	# collided against something. Used to prevent jumping
	# when we haven't hit anything.
	frame_since_collision = 0
	frame_since_jump = 0
	# -- Methods
	# Constructor function
	def __init__(self,x,y):
		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)
		# Set height, width
		Player.image=pygame.image.load('full_up_rest.png')		
		self.image = Player.image#.load("")(#Surface([15, 15])
		
		self.rect=self.image.get_rect()
		self.rect.topleft = [x,y]
		# Change the speed of the player
	def changespeed_x(self,x):
		self.change_x = x
	def changespeed_y(self,y):
		self.change_y = y
	
	#find new position for the player
	def update(self,blocks):
		# Save the old x position, update, and see if we collided.
		old_x = self.rect.left
		new_x = old_x + self.change_x
		self.rect.left = new_x
		collide = pygame.sprite.spritecollide (self, blocks, False)
		if collide:
			# We collided, go back to the old pre-collision location
			self.rect.left = old_x
			# Save the old y position, update, and see if we collided.
		old_y = self.rect.top
		new_y = old_y + self.change_y
		self.rect.top = new_y
		block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
		for block in block_hit_list:
			# We collided. Set the old pre-collision location.
			self.rect.top = old_y
			self.rect.x = old_x
			# Stop our vertical movement
			self.change_y = 0
			# Start counting frames since we hit something
			self.frame_since_collision = 0
		# If the player recently asked to jump, and we have recently
		# had ground under our feet, go ahead and change the velocity
		# to send us upwards
		if self.frame_since_collision < 6 and self.frame_since_jump < 6:
			self.frame_since_jump = 100
			self.change_y -= 8
		# Increment frame counters
		self.frame_since_collision+=1
		self.frame_since_jump+=1
	# Calculate effect of gravity.
	def calc_grav(self,count):

		self.change_y += .15
		# See if we are on the ground.
		if self.rect.top >= 430 and self.change_y >= 0:
			if self.rect.top>=421:
				count-=5
				
		
			#player.image=pygame.image.load('full_up_rest.png')
			pygame.display.update()			
			self.change_y = 0
			self.rect.top = 430
			self.frame_since_collision = 0
		return count
	# Called when user hits 'jump' button
	def jump(self,blocks):
		self.jump_ready = True
		self.frame_since_jump = 0
pygame.init()
pygame.mixer.music.load('an-turr.ogg')#load music
pygame.mixer.music.play(-1)
jump=pygame.mixer.Sound('jump.wav')
#background=pygame.image.load('res/back.png').convert_alpha()
# Set the height and width of the screen
size=[640,480]
screen=pygame.display.set_mode(size)
background=pygame.image.load('back.png')
count=0
pygame.display.set_caption("JUMP!")

# Create platforms
block_list = pygame.sprite.RenderPlain()

all_sprites_list = pygame.sprite.RenderPlain()
steps=list()
gend=Ball()#for the moksha dwar!!
gend.rect.x=200
gend.rect.y=200
gendg = pygame.sprite.RenderPlain()
gendg.add(gend)
for i in range(100):
	block = Platform()
	#wal=Wall()
	# Set x and y based on block number
	block.rect.x = random.randint(73,247)
	block.rect.y = 480-100*i
	
	steps.append(block)
	block_list.add(steps[i])#we add all the sprite objects to the group block_list
	#block_list.add(wall[i])
	all_sprites_list.add(steps[i])
# Main program, create the blocks
player = Player(400, 400)
player.rect.x = 540
player.rect.y = 450
def scrolldownfunc(degree):
	
	for s in steps:
		s.rect.y=s.rect.y+degree
	
	player.rect.y=player.rect.y+degree
a=0
def drawstepsandplayer(block_list,a):
	block_list.remove()
	#draw new steps
	for i in range(100):
		sdf=pygame.sprite.RenderPlain()	#the sprite group to use its draw method 	
		sdf.add(steps[i])
		
		block_list.add(sdf)
		sdf.draw(screen)
		a+=1
	#draw player
	#lunch.y=lunch.y-1
	qwe=pygame.sprite.RenderPlain() #the sprite group to use its draw method	
	qwe.add(player)
	qwe.draw(screen)
red = (255, 0, 0)	
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
#pygame.time.set_timer(USEREVENT+1, 50)

# -------- Main Program Loop -----------
ballxmove = 3
ballymove = 3
score=0
coward=0
def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	# pick a font you have and set its size
	myfont = pygame.font.SysFont(Textfont, Textsize)
	# apply it to text on a label
	label = myfont.render(txtText, 1, Textcolor)
	# put the label object on the screen at point Textx, Texty
	screen.blit(label, (Textx, Texty))
	# show the whole thing
	pygame.display.flip()
while done==False:
					
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			coward=1
			done=True # Flag that we are done so we exit this loop	
				
					
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed_x(-6)
			if event.key == pygame.K_RIGHT:
				player.changespeed_x(6)
			if event.key == pygame.K_UP:
				pygame.key.set_repeat(0,0)
				player.image=pygame.image.load('full_up_jump.png')
				player.jump(block_list)
				jump.play(2)
			if event.key == pygame.K_DOWN:
				player.changespeed_y(6)
				
		if event.type == pygame.KEYUP:
			player.image=pygame.image.load('full_up_rest.png')
			if event.key == pygame.K_LEFT:
				player.changespeed_x(-0)
			if event.key == pygame.K_RIGHT:
				player.changespeed_x(0)
		
	scrolldownfunc(1) #to change the speed of scrolling 
	
	if player.rect.x >= 700:
		player.rect.x = -15
	if player.rect.x <= -20:
		player.rect.x = 699
	
	score+=player.calc_grav(count)
	player.update(block_list)			
	block_list.update()
	pygame.key.set_repeat()	
	# Set the screen background
	screen.blit(background,(0,0))
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	drawstepsandplayer(block_list,a)	
	#refreshsteps(lastblock,steps,block_list)	
	#all_sprites_list.draw(screen)
	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	# Limit to 20 frames per second
	gendg.draw(screen)
	gend.rect.x  += ballxmove	# Update ball position
	gend.rect.y += ballymove

	if gend.rect.x > 600:			# Ball reached screen edges?
		ballxmove = -2
	if gend.rect.x < 0:
		ballxmove = 2
	if gend.rect.y > 440:
		ballymove = -2
	if gend.rect.y < 0:
		ballymove = 2
	gendg.add(gend)		
	clock.tick(60)
	#time.delay(1)
	if pygame.sprite.spritecollide(player, gendg, True):
		done=True
	# Go ahead and update the screen with what we've drawn.
	#block_list.clear(screen)	
	#pygame.display.update()	
	pygame.display.flip()
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.\
rank=-1*score+1	
norank=1
if rank>1 and rank<100:
	final= "superb!"
if rank<=6:
	final="We Bow to You our Master!!!"
if rank>100 and rank<500:
	final= "good!!"
if rank>500 and rank<1000:
	final= "well tried!"
if rank>1000 :
	final= "give another shot!!"
if rank>10000:
	final= "seriously!! r u nuts??"
if coward:
	final="You do not deserve a rank"
	norank=0
screen.fill((0,0,0))
rank=str(rank)
r="Your rank is " +rank
printText("Game Over!!", "MS Comic Sans", 30, 230, 220, red)
if norank:
	printText(r, "MS Comic Sans", 30, 230, 250, red)
printText(final, "MS Comic Sans", 30, 230, 280, red)
#time.delay(10)

pygame.quit ()
