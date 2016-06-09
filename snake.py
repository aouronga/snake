#Author: Aourongajab Abir
#Contact: www.aouronga.com    or fb.me/abir91
#About: This is my first developed game. I made this game for my BSc 4th semester Computational Geometry project.
#Kivy framework is required to run this game.
from kivy.app import App 
from kivy.uix.image import Image
from kivy.graphics import *
from random import randint
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from functools import partial
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from random import randint
from kivy.clock import Clock

class SnakeBoard(FloatLayout):
	def __init__(self,**kwargs):
		super(SnakeBoard,self).__init__(**kwargs)

		self.p1opacity = 1
		self.p2opacity = 0
		self.p1position = 0
		self.p2position = 0
		p1active = False
		p2active = False

		self.player1 = Label(text="Player1: ", color=[1,0,0,1], size_hint=(.1, .15),pos_hint={'x':0, 'y':.9})
		self.player1State = Label(text="It's Player1 turn!: ",opacity=self.p1opacity, color=[1,0,0,1], size_hint=(.1, .15),pos_hint={'x':0.05, 'y':.80}, font_size="20px")
		self.player1dice = Button(text='Player1', pos_hint={'x': 0, 'y':.70}, size_hint=(.08, .12), opacity=1, background_color= [1, 0, 0, 1])
		self.player1msg = Label(text="MSG",opacity=self.p1opacity, color=[1,0,0,1], size_hint=(.1, .15),pos_hint={'x':0.05, 'y':.85}, font_size="20px")

		self.player2 = Label(text="Player2: ", color=[0,1,0,1], size_hint=(.1, .15),pos_hint={'x':0, 'y':.6})
		self.player2State = Label(text="It's Player2 turn!: ",opacity=self.p2opacity, color=[0,1,0,1], size_hint=(.1, .15),pos_hint={'x':0.05, 'y':.50}, font_size="20px")
		self.player2dice = Button(text='Player2', pos_hint={'x': 0, 'y': .40}, size_hint=(.08, .12), opacity=1, background_color= [0, 1, 0, 1])
		self.player2msg = Label(text="MSG",opacity=self.p1opacity, color=[1,0,0,1], size_hint=(.1, .15),pos_hint={'x':0.05, 'y':.55}, font_size="20px")
		


		self.dice = Button(text=":  :", background_color=[1,0,1,1], size_hint=(.06,.07), pos_hint={'x':.07, 'y':.11}, font_size="40px", on_press=self.roll)
		self.about = Button(text="About Me", size_hint=(.18,.10), pos_hint={'x':0, 'y':0})
		self.board = Image(source="board.jpg", pos_hint={'x':.08, 'y':0}, size_hint=(1,1))


		self.add_widget(self.player1)
		self.add_widget(self.player1State)
		self.add_widget(self.player2)
		self.add_widget(self.player2State)
		self.add_widget(self.dice)
		self.add_widget(self.about)
		self.add_widget(self.board)
		self.add_widget(self.player1dice)
		self.add_widget(self.player2dice)
		self.add_widget(self.player1msg)
		self.add_widget(self.player2msg)


	def roll(self, instance, *argv):

		pos1 = {'x':.255, 'y':0.04}
		pos2 = {'x':.37, 'y':0.04}
		pos3 = {'x':.48, 'y':0.04}
		pos4 = {'x':.6, 'y':0.04}
		pos5 = {'x':.715, 'y':0.04}
		pos6 = {'x':.825, 'y':0.04}

		pos7 = {'x':.825, 'y':0.23}
		pos8 = {'x':.715, 'y':0.23}
		pos9 = {'x':.6, 'y':0.23}
		pos10 = {'x':.48, 'y':0.23}
		pos11 = {'x':.37, 'y':0.23}
		pos12 = {'x':.255, 'y':0.23}

		pos13 = {'x':.255, 'y':0.425}
		pos14 = {'x':.37, 'y':0.425}
		pos15 = {'x':.48, 'y':0.425}
		pos16 = {'x':.6, 'y':0.425}
		pos17 = {'x':.715, 'y':0.425}
		pos18 = {'x':.825, 'y':0.425}

		pos19 = {'x':.825, 'y':0.62}
		pos20= {'x':.715, 'y':0.62}
		pos21= {'x':.6, 'y':0.62}
		pos22 = {'x':.48, 'y':0.62}
		pos23 = {'x':.37, 'y':0.62}
		pos24 = {'x':.255, 'y':0.62}

		pos25 = {'x':.255, 'y':0.825}
		pos26 = {'x':.37, 'y':0.825}
		pos27 = {'x':.48, 'y':0.825}
		pos28 = {'x':.6, 'y':0.825}
		pos29 = {'x':.715, 'y':0.825}
		pos30 = {'x':.825, 'y':0.825}
		
		# pos = {1:pos1}

		# p1 = 0
		# p2 = 0

		ran = randint(1,6)

		if self.p1opacity == 1:

			self.player1State.opacity = 0
			self.player2State.opacity = 1
			self.p1opacity = 0

			self.p1position += ran
			if self.p1position <= 30:
				if self.p1position == 1:
					self.player1dice.pos_hint= pos1
				elif self.p1position == 2:
					self.player1dice.pos_hint= pos2

				elif self.p1position == 3:
					self.player1msg.text = "Awesome! It's a Ladder!"
					self.p1position = 22
					self.player1dice.pos_hint= pos22

				elif self.p1position == 4:
					self.player1dice.pos_hint= pos4
				elif self.p1position == 5:
					self.player1msg.text = "Awesome! It's a Ladder!"
					self.p1position = 8
					self.player1dice.pos_hint= pos8

				elif self.p1position == 6:
					self.player1dice.pos_hint= pos6
				
				elif self.p1position == 7:
					self.player1dice.pos_hint= pos7
				elif self.p1position == 8:
					self.player1dice.pos_hint= pos8
				elif self.p1position == 9:
					self.player1dice.pos_hint= pos9
				elif self.p1position == 10:
					self.player1dice.pos_hint= pos10
				elif self.p1position == 11:
					self.player1msg.text = "Awesome! It's a Ladder!"
					self.p1position = 26
					self.player1dice.pos_hint= pos26


				elif self.p1position == 12:
					self.player1dice.pos_hint= pos12

				elif self.p1position == 13:
					self.player1dice.pos_hint= pos13
				elif self.p1position == 14:
					self.player1dice.pos_hint= pos14
				elif self.p1position == 15:
					self.player1dice.pos_hint= pos15
				elif self.p1position == 16:
					self.player1dice.pos_hint= pos16
				elif self.p1position == 17:
					self.player1msg.text = "Awwe! Snake!"
					self.p1position = 4
					self.player1dice.pos_hint= pos4

				elif self.p1position == 18:
					self.player1dice.pos_hint= pos18

				elif self.p1position == 19:
					self.player1msg.text = "Awwe! Snake!"
					self.p1position = 7
					self.player1dice.pos_hint= pos7

				elif self.p1position == 20:
					self.player1msg.text = "Awesome! It's a Ladder!"
					self.p1position = 29
					self.player1dice.pos_hint= pos29


				elif self.p1position == 21:
					self.player1msg.text = "Awwe! Snake!"
					self.p1position = 9
					self.player1dice.pos_hint= pos9

				elif self.p1position == 22:
					self.player1dice.pos_hint= pos22
				elif self.p1position == 23:
					self.player1dice.pos_hint= pos23
				elif self.p1position == 24:
					self.player1dice.pos_hint= pos24

				elif self.p1position == 25:
					self.player1dice.pos_hint= pos25
				elif self.p1position == 26:
					self.player1dice.pos_hint= pos26
				elif self.p1position == 27:
					self.player1msg.text = "Awwe! Snake!"
					self.p1position = 1
					self.player1dice.pos_hint= pos1

				elif self.p1position == 28:
					self.player1dice.pos_hint= pos28
				elif self.p1position == 29:
					self.player1dice.pos_hint= pos29
				elif self.p1position == 30:
					self.player1dice.pos_hint= pos30
				elif self.p1position == 31:
					self.player1msg.text = "Player1 Won The Game!"

			print "Player1: "+ str(self.p1position)
		else:
			self.player2State.opacity = 0
			self.player1State.opacity = 1
			self.p1opacity = 1
			self.p2position += ran
			if self.p2position <= 30:
				if self.p2position == 1:
					self.player2dice.pos_hint= pos1
				elif self.p2position == 2:
					self.player2dice.pos_hint= pos2
				elif self.p2position == 3:
					self.player2msg.text = "Awesome! It's a Ladder!"
					self.p2position = 22
					self.player2dice.pos_hint= pos22

				elif self.p2position == 4:
					self.player2dice.pos_hint= pos4
				elif self.p2position == 5:
					self.player2msg.text = "Awesome! It's a Ladder!"
					self.p2position = 5
					self.player2dice.pos_hint= pos8

				elif self.p2position == 6:
					self.player2dice.pos_hint= pos6

				elif self.p2position == 7:
					self.player2dice.pos_hint= pos7
				elif self.p2position == 8:
					self.player2dice.pos_hint= pos8
				elif self.p2position == 9:
					self.player2dice.pos_hint= pos9
				elif self.p2position == 10:
					self.player2dice.pos_hint= pos10
				elif self.p2position == 11:
					self.player2msg.text = "Awesome! It's a Ladder!"
					self.p2position = 26
					self.player2dice.pos_hint= pos26

				elif self.p2position == 12:
					self.player2dice.pos_hint= pos12

				elif self.p2position == 13:
					self.player2dice.pos_hint= pos13
				elif self.p2position == 14:
					self.player2dice.pos_hint= pos14
				elif self.p2position == 15:
					self.player2dice.pos_hint= pos15
				elif self.p2position == 16:
					self.player2dice.pos_hint= pos16
				elif self.p2position == 17:
					self.player2msg.text = "Awwe! Snake!"
					self.p2position = 4
					self.player1dice.pos_hint= pos4
				elif self.p2position == 18:
					self.player2dice.pos_hint= pos18
				elif self.p2position == 19:
					self.player2msg.text = "Awwe! Snake!"
					self.p2position = 7
					self.player1dice.pos_hint= pos7
				elif self.p2position == 20:
					self.player2msg.text = "Awesome! It's a Ladder!"
					self.p2position = 29
					self.player2dice.pos_hint= pos29
				elif self.p2position == 21:
					self.player2msg.text = "Awwe! Snake!"
					self.p2position = 9
					self.player1dice.pos_hint= pos9
				elif self.p2position == 22:
					self.player2dice.pos_hint= pos22
				elif self.p2position == 23:
					self.player2dice.pos_hint= pos23
				elif self.p2position == 24:
					self.player2dice.pos_hint= pos24
				elif self.p2position == 25:
					self.player2dice.pos_hint= pos25
				elif self.p2position == 26:
					self.player2dice.pos_hint= pos26
				elif self.p2position == 27:
					self.player2msg.text = "Awwe! Snake!"
					self.p2position = 1
					self.player1dice.pos_hint= pos1
				elif self.p2position == 28:
					self.player2dice.pos_hint= pos28
				elif self.p2position == 29:
					self.player2dice.pos_hint= pos29
				elif self.p2position == 30:
					self.player2dice.pos_hint= pos30
				elif self.p2position == 31:
					self.player2msg.text = "Player2 Won The Game!"

			print "Player2: "+ str(self.p2position)


		self.dice.text = str(ran)

class SnakeApp(App):
	def build(self):
		return SnakeBoard()

if __name__ == '__main__':
	SnakeApp().run()