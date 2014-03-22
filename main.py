import pygame as py
from pygame.locals import *
from math import sqrt
from random import randrange

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 55

class CreditsScreen(object):
	def __init__(self):
		self.font = py.font.SysFont("Courier New", 15)
		
		self.text_1 = "Made by... I don't know..."
		self.text_2 = "I think its username was Luminnem,"
		self.text_3 = "or something like that"
		self.text_4 = "You could follow it on Twitter,"
		self.text_5 = "I think it would be a good idea"
		
		self.label_1 = self.font.render(self.text_1, 1, (255, 255, 255))
		self.label_2 = self.font.render(self.text_2, 1, (255, 255, 255))
		self.label_3 = self.font.render(self.text_3, 1, (255, 255, 255))
		self.label_4 = self.font.render(self.text_4, 1, (255, 255, 255))
		self.label_5 = self.font.render(self.text_5, 1, (255, 255, 255))
		
		self.selected = "[*]"
		self.unselected = "[ ]"
		self.smiles = [":)", ";)"]
		self.timer = 0
		self.delay = 250
		self.frame = 0
		
		self.menu_1 = "Back"
		self.menu_2 = "Play"
		self.menuLabel_1 = self.font.render(self.menu_1, 1, (255, 255, 255))
		self.menuLabel_2 = self.font.render(self.menu_2, 1, (255, 255, 255))
		self.select = -1
		
	def Update(self, sm):
		self.UpdateLabels()
		self.UpdateLabels()
		self.Controls(sm)
	
	def Controls(self, sm):
		key = py.key.get_pressed()
		if key[K_UP] and self.select > 0:
			self.select -= 1
		elif key[K_DOWN] and self.select < 1:
			self.select += 1
		elif key[K_RETURN] and self.select > -1:
			sm.currentScreen = self.select
			self.select = -1
		
	def UpdateLabels(self):
		self.UpdateMenuLabels()
		self.UpdateCreditsLabels()
		
	def UpdateMenuLabels(self):
		self.menu_1 = "Back"
		self.menu_2 = "Play"
		
		if self.select == 0:
			self.menu_1 = self.selected + self.menu_1
		else:
			self.menu_1 = self.unselected + self.menu_1
		
		if self.select == 1:
			self.menu_2 = self.selected + self.menu_2
		else:
			self.menu_2 = self.unselected + self.menu_2
			
		self.menuLabel_1 = self.font.render(self.menu_1, 1, (255, 255, 255))
		self.menuLabel_2 = self.font.render(self.menu_2, 1, (255, 255, 255))
		
	def UpdateCreditsLabels(self):
		self.text_5 = "I think it would be a good idea "+self.smiles[self.frame]
		self.label_5 = self.font.render(self.text_5, 1, (255, 255, 255))
		self.Timer()
		
		
	def Timer(self):
		if py.time.get_ticks() - self.timer > self.delay:
			self.timer = py.time.get_ticks()
			self.frame += 1
			if self.frame > len(self.smiles)-1:
				self.frame = 0
				
	def Render(self, screen):
		self.RenderMenu(screen)
		self.RenderText(screen)
	
	def RenderMenu(self, screen):
		x = SCREEN_WIDTH / 2 - self.menuLabel_1.get_width() / 2
		y = SCREEN_HEIGHT / 2 - (self.menuLabel_1.get_height() + self.menuLabel_2.get_height() + 20) / 2
		blankspace = 20
		screen.blit(self.menuLabel_1, (x, y + 0 * blankspace))
		screen.blit(self.menuLabel_2, (x, y + 1 * blankspace))
		
	def RenderText(self, screen):
		average = 0
		average += self.label_1.get_width()
		average += self.label_2.get_width()
		average += self.label_3.get_width()
		average += self.label_4.get_width()
		average += self.label_5.get_width()
		average = int((average / 5)/2)
		
		x = SCREEN_WIDTH / 2 - average
		y = 50
		blankspace = 20
		screen.blit(self.label_1, (x, y + 0 * blankspace))
		screen.blit(self.label_2, (x, y + 1 * blankspace))
		screen.blit(self.label_3, (x, y + 2 * blankspace))
		screen.blit(self.label_4, (x, y + 3 * blankspace))
		screen.blit(self.label_5, (x, y + 4 * blankspace))

class MatchEndScreen(object):
	def __init__(self):
		self.font = py.font.SysFont("Courier New", 15)
		self.bigFont = py.font.SysFont("Courier New", 25)
		self.select = 0
		self.time = 0
		self.delay = 250
		self.smiles = [[":)", ":D"], [":(", ":,("]]
		self.mode = 0
		self.frame = 0
		
		#STRINGS
		self.victory = "YOU WON!"
		self.defeat = "You lost"
		self.selected = "[*]"
		self.unselected = "[ ]"
		self.playAgain = "Play again (That's my Oompa Loompa)"
		self.giveUp = "Give up (Loser xD)"
		
		#Labels
		self.victoryLabel = self.font.render(self.victory, 1, (255, 255, 255))
		self.defeatLabel = self.font.render(self.defeat, 1, (255, 255, 255))
		self.playAgainLabel = self.font.render(self.playAgain, 1, (255, 255, 255))
		self.giveUpLabel = self.font.render(self.giveUp, 1, (255, 255, 255))
		
	def Update(self, sm):
		self.Controls(sm)
		self.UpdateLabels()
		self.Timer()
		
	def UpdateLabels(self):
		self.UpdateFinalMessageLabels()
		self.UpdateMenuLabels()
		
	def UpdateFinalMessageLabels(self):
		self.victory = "You Win "
		self.defeat = "You lost "
		if self.mode == 0:
			self.victory = self.victory + self.smiles[self.mode][self.frame]
			self.victoryLabel = self.font.render(self.victory, 1, (255, 255, 255))
		elif self.mode == 1:
			self.defeat = self.defeat + self.smiles[self.mode][self.frame]
			self.defeatLabel = self.font.render(self.defeat, 1, (255, 255, 255))
		
	def UpdateMenuLabels(self):
		self.playAgain = "Play again (That's my Oompa Loompa)"
		self.giveUp = "Give up (Only losers give up)"
		
		if self.select == 0:
			self.playAgain = self.selected + self.playAgain
		else:
			self.playAgain = self.unselected + self.playAgain
			
		if self.select == 1:
			self.giveUp = self.selected + self.giveUp
		else:
			self.giveUp = self.unselected + self.giveUp
			
		self.playAgainLabel = self.font.render(self.playAgain, 1, (255, 255, 255))
		self.giveUpLabel = self.font.render(self.giveUp, 1, (255, 255, 255))
		
	def Controls(self, sm):
		key = py.key.get_pressed()
		if key[K_UP] and self.select > 0:
			self.select -= 1
		elif key[K_DOWN] and self.select < 1:
			self.select += 1
		elif key[K_RETURN]:
			if self.select == 0:
				sm.play.Restart()
				sm.currentScreen = 1
			elif self.select == 1:
				sm.play.Restart()
				sm.currentScreen = 0

	def Timer(self):
		if py.time.get_ticks() - self.time > self.delay:
			self.time = py.time.get_ticks()
			self.frame += 1
			if self.frame > len(self.smiles[self.mode])-1:
				self.frame = 0
		
	def Render(self, screen, play):
			
		self.RenderFinalScore(screen, play)
		self.RenderFinalMessage(screen, play)
		self.RenderMenu(screen)
		
	def RenderMenu(self, screen):
		x = SCREEN_WIDTH / 2 - 200
		y = SCREEN_HEIGHT / 2
		blankspace = 20
		
		screen.blit(self.playAgainLabel, (x, y + 0 * blankspace))
		screen.blit(self.giveUpLabel, (x, y + 1 * blankspace))
		
	def RenderFinalScore(self, screen, play):
		finalScore = "Your score: %d / Enemy score: %d" % (play.player.score, play.enemy.score)
		finalScoreLabel = self.bigFont.render(finalScore, 1, (255, 255, 255))
		screen.blit(finalScoreLabel, (SCREEN_WIDTH / 2 - finalScoreLabel.get_width() / 2, 20))	
		
	def RenderFinalMessage(self, screen, play):
		x = 100
		y = 60
		if play.player.score > play.enemy.score:
			self.mode = 0
			screen.blit(self.victoryLabel, (x, y))
		else:
			self.mode = 1
			screen.blit(self.defeatLabel, (x, y))
		
class MenuScreen(object):
	def __init__(self):
		self.font = py.font.SysFont("Courier New", 15)
		self.bigFont = py.font.SysFont("Courier New", 50)
		self.select = 0
		self.smiles = [":)", ":D", "=)", "=D"]
		self.smile = 0
		
		self.time = 0
		self.delay = 500
		
	def Update(self, sm):
		self.Controls(sm)
		self.SmilesTimer()
	
	def Controls(self, sm):
		key = py.key.get_pressed()
		if key[K_UP] and self.select > 1:
			self.select -= 1
			
		elif key[K_DOWN] and self.select < 2:
			self.select += 1
		
		elif key[K_RETURN] and self.select > 0:
			sm.currentScreen = self.select
			self.select = -1
			
	def Render(self, screen):
		selected = "[*]"
		unselected = "[ ]"
		play = "Play"
		credit = "Credits"
		
		if self.select == 1:
			play = selected + play
		else:
			play = unselected + play
		
		if self.select == 2:
			credit = selected + credit
		else:
			credit = unselected + credit
			
		x = SCREEN_WIDTH / 2 - 100
		y = SCREEN_HEIGHT / 2
		blankspace = 20
		
		playLabel = self.font.render(play, 1, (255, 255, 255))
		creditLabel = self.font.render(credit, 1, (255, 255, 255))
		
		screen.blit(playLabel, (x, y + 0 * blankspace))
		screen.blit(creditLabel, (x, y + 1 * blankspace))
		
		self.DrawTitle(screen)
		
	def DrawTitle(self, screen):
		title = "PONG "+self.smiles[self.smile]
		titleLabel = self.bigFont.render(title, 1, (255, 255, 255))
		screen.blit(titleLabel, (SCREEN_WIDTH / 2 - 125, 50))
	
	def SmilesTimer(self):
		if py.time.get_ticks() - self.time > self.delay:
			self.time = py.time.get_ticks()
			
			self.smile += 1
			if self.smile > len(self.smiles)-1:
				self.smile = 0
		
		
class PlayScreen(object):
	def __init__(self):
		self.player = Player()
		self.ball = Ball()
		self.collisions = CollisionsManager()
		self.ui = UserInterface()
		self.enemy = Enemy()
		self.maxScore = 5
		
	def Update(self, sm):
		self.player.Update()
		self.ball.Update()
		self.enemy.Update(self.ball)
		self.collisions.CheckAll(self.player, self.enemy, self.ball)
		self.ui.Update(self.player, self.enemy)
		
		if self.player.score >= self.maxScore or self.enemy.score >= self.maxScore:
			sm.currentScreen = 3
		
	def Render(self, screen):
		self.player.Render(screen)
		self.ball.Render(screen)
		self.enemy.Render(screen)
		self.ui.Render(screen)
		
	def Restart(self):
		self.player.RestartAll()
		self.ball.Restart()
		self.enemy.RestartAll()

class ScreensManager(object):
	'''
	SCREENS ID
	0 -> Menu
	1 -> Play
	2 -> Credits
	3 -> Match end
	'''
	
	def __init__(self):
		self.currentScreen = 0
		self.menu = MenuScreen()
		self.play = PlayScreen()
		self.matchEnd = MatchEndScreen()
		self.creditsScreen = CreditsScreen()
		
	def Update(self):
		key = py.key.get_pressed()
		
		if self.currentScreen == 0:
			self.menu.Update(self)
				
		elif self.currentScreen == 1:
			self.play.Update(self)
			
		elif self.currentScreen == 2:
			self.creditsScreen.Update(self)
			
		elif self.currentScreen == 3:
			self.matchEnd.Update(self)
			
	def Render(self, screen):
		if self.currentScreen == 0:
			self.menu.Render(screen)
			
		elif self.currentScreen == 1:
			self.play.Render(screen)
			
		elif self.currentScreen == 2:
			self.creditsScreen.Render(screen)
			
		elif self.currentScreen == 3:
			self.matchEnd.Render(screen, self.play)
	
class Enemy(object):
	def __init__(self):
		self.x = SCREEN_WIDTH - 75 - PADDLE_WIDTH
		self.y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
		self.width = PADDLE_WIDTH
		self.height = PADDLE_HEIGHT
		self.vy = 0
		self.vx = 0
		self.speed = 10
		self.maxX = SCREEN_WIDTH - 75 - PADDLE_WIDTH - 25
		self.minX = SCREEN_WIDTH - 25
		self.score = 0
		
	def Update(self, ball):
		self.Move(ball)
		self.AI(ball)
		self.CheckBounds()
		
	def Move(self, ball):
		self.x += self.vx
		self.y += self.vy
		
	def Render(self, screen):
		py.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
		
	def CheckBounds(self):
		if self.y < 0:
			self.y = 0
		if self.y + self.height > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.height
			
		if self.x + self.width > self.minX:
			self.x = self.minX - self.width
		if self.x < self.maxX:
			self.x = self.maxX
			
	def AI(self, ball):
		if ball.x < self.x + self.width:
			self.CatchBall(ball)
			
		if self.DistanceToBall(ball) < 20:
			self.Hit(ball)
		else:
			self.Return()

	def Hit(self, ball):
		self.vx = -5
		
	def Return(self):
		self.vx = 5
		
	def CatchBall(self, ball):
		if self.y > ball.y + ball.radius:
			self.vy = -self.speed
		elif self.y + self.height < ball.y - ball.radius:
			self.vy = self.speed
		else:
			self.vy = 0
		
	def DistanceToBall(self, ball):
		mx = ball.x - self.x
		mx = mx ** 2
		
		padMiddle = self.y + (self.height / 2)
		my = ball.y - padMiddle
		my = my ** 2
		
		distance = int(sqrt(mx + my))
		
		return distance
		
	def Restart(self):
		self.x = SCREEN_WIDTH - 75 - PADDLE_WIDTH
		self.y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
	
	def RestartAll(self):
		self.Restart()
		self.score = 0

class UserInterface(object):
	def __init__(self):
		self.font = py.font.SysFont("Comic Sans MS", 15)
		self.playerScore = ""
		self.enemyScore = ""
		
		
	def Render(self, screen):
		self.DrawMiddleLine(screen)
		self.DrawScore(screen)
		
	def Update(self, player, enemy):
		self.playerScore = "Player score: "+str(player.score)
		self.enemyScore = "Enemy Score: "+str(enemy.score)
		
	def DrawMiddleLine(self, screen):
		for i in range(int(SCREEN_HEIGHT / 15)):
			py.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH / 2 - 2, i * 15, 4, 10))
			
	def DrawScore(self, screen):
		playerScoreLabel = self.font.render(self.playerScore, 1, (255, 255, 255))
		enemyScoreLabel = self.font.render(self.enemyScore, 1, (255, 255, 255))
		screen.blit(playerScoreLabel, (40, 0))
		screen.blit(enemyScoreLabel, (480, 0))

class CollisionsManager(object):
	
	def CheckAll(self, player, enemy, ball):
		self.Update(player, ball)
		self.Update(enemy, ball)
		
		if ball.x - ball.radius <= 0 or ball.x + ball.radius >= SCREEN_WIDTH:
			if ball.x < SCREEN_WIDTH / 2:
				enemy.score += 1
			else:
				player.score += 1
			ball.Restart()
			player.Restart()
			enemy.Restart()
		
	def Update(self, player, ball):
		if self.CheckPaddleBall(player, ball):
			if player.x < SCREEN_WIDTH / 2: #IT'S THE PLAYER
				ball.x = player.x + player.width + ball.radius
			else: #It's the enemy
				ball.x = player.x - ball.radius
			ball.vx *= -1
			
			if player.vy < 0:
				if ball.vy > 0:
					ball.vy *= -1
			elif player.vy > 0:
				if ball.vy < 0:
					ball.vy *= -1
					
			if player.vx > 0:
				if ball.vx > 0:
					ball.vx += 1
				if ball.vx < 0:
					ball.vx -= 1
					
			elif player.vx <= 0:
				if ball.vx > 0 and abs(ball.vx) > ball.minVx:
					ball.vx -= 1
				elif ball.vx < 0 and abs(ball.vx) > ball.minVx:
					ball.vx += 1
		
	def CheckPaddleBall(self, pad, ball):
		if (pad.x > ball.x + ball.radius or pad.y > ball.y + ball.radius or pad.x + pad.width < ball.x - ball.radius or pad.y + pad.height < ball.y - ball.radius):
			return False
		else:
			return True

class Ball(object):
	
	def __init__(self):
		self.radius = 6
		self.x = SCREEN_WIDTH / 2 - self.radius / 2
		self.y = SCREEN_HEIGHT / 2 - self.radius / 2
		self.vx = 5
		self.vy = 5
		self.minVx = 5
		
	def Render(self, render):
		py.draw.circle(render, (255, 255, 255), (self.x, self.y), self.radius)
		
	def Update(self):
		self.Move()
		self.CheckBounds()
		
	def Move(self):
		self.x += self.vx
		self.y += self.vy
		
	def CheckBounds(self):
		if self.x - self.radius < 0:
			self.x = 0 + self.radius
			self.vx *= -1
			
		if self.x + self.radius > SCREEN_WIDTH:
			self.x = SCREEN_WIDTH - self.radius
			self.vx *= -1
			
		if self.y - self.radius < 0:
			self.y = 0 + self.radius
			self.vy *= -1
			
		if self.y + self.radius > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.radius
			self.vy *= -1
			
	def Restart(self):
		self.x = SCREEN_WIDTH / 2 - self.radius / 2
		self.y = SCREEN_HEIGHT / 2 - self.radius / 2
		self.vx = self.minVx
			
			
class Player(object):
	
	def __init__(self):
		self.x = 75
		self.y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
		self.width = PADDLE_WIDTH
		self.height = PADDLE_HEIGHT
		self.speed = 10
		self.vy = 0
		self.vx = 0
		self.score = 0
		
	def Render(self, screen):
		py.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
	
	def Update(self):
		self.Controls()
		self.Move()
		self.CheckBounds()
	
	def Move(self):
		self.y += self.vy
		self.x += self.vx
		
	def Controls(self):
		key = py.key.get_pressed()
		
		if key[K_UP]:
			self.vy = -self.speed
		elif key[K_DOWN]:
			self.vy = self.speed
		else:
			self.vy = 0
			
		if key[K_RIGHT]:
			self.vx = 5
		elif key[K_LEFT]:
			self.vx = -5
		else:
			self.vx = 0
			
	def CheckBounds(self):
		if self.y < 0:
			self.y = 0
		if self.y + self.height > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.height
			
		if self.x > 100:
			self.x = 100
		if self.x < 0:
			self.x = 0
	
	def Restart(self):
		self.x = 75
		self.y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
		
	def RestartAll(self):
		self.Restart()
		self.score = 0
		
def main():
	py.init()
	screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	py.display.set_caption("Pong")
	
	clear = (0, 0, 0)
	exit = False
	fps = py.time.Clock()
	
	screensManager = ScreensManager()
	

	
	while not exit:
		for event in py.event.get():
			if event.type == QUIT:
				exit = True
		
		screen.fill(clear)
		#---------------------
		
		screensManager.Render(screen)
		screensManager.Update()

		#----------------------
		py.display.update()
		fps.tick(60)
	return 0

if __name__ == "__main__":
	main()
