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

class SnakeBoard(BoxLayout):
	def player(self):
		player_info = BoxLayout(orientation='vertical', size_hint=(.4,1), pos=(100,50))
		player1 = Label(text="Player1: ", color=[1,0,0,1])
		player1_score = 0
		print "player1"+ str(player1_score)
		player_info.add_widget(player1)

		player2 = Label(text="Player2: ", color=[0,1,0,1])
		player2_score = 0
		player_info.add_widget(player2)
		return player_info

	def animate(self, instance, *args):
		animation = Animation(pos=(0, 0), t='out_bounce')
		animation += Animation(pos=(0, 110), t='out_bounce')
		ran = randint(1,6)
		# self.leftside.animate_dice = Button(text=str(ran), size_hint=(None, None), font_size="40px")
		self.dice(ran)
		

		animation.start(instance)
		# return 0
	def popp(self, *argv):
		print 567890
		popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400))
		return popup

	def leftside(self, *kwargs):
		# ran = list(kwargs)
		# if ran:
		# 	val += ran[0]
		# else:

		val = randint(1,6)
		layout = BoxLayout(orientation='vertical', size_hint=(.4,1))
		btn1 = self.player()
		# random = randint(1,6)
		animate_dice = Button(text=str(val), size_hint=(None, None), font_size="40px")
		animate_dice.bind(on_press=self.animate)
		btn2 = Button(text='About Me', size_hint=(1.2,.2), pos_hint={'x':0, 'y':0.05}, background_color=[1,1,0,1], on_press=self.popp)
		
		layout.add_widget(btn1)
		layout.add_widget(animate_dice)
		# layout.add_widget(animate_dice)
		layout.add_widget(btn2)
		return layout

	def dice(self, *argv):
		d = list(argv)
		pos1 = {'x':.45, 'y':0.05}
		pos2 = {'x':.61, 'y':0.05}
		pos3 = {'x':.77, 'y':0.05}
		pos4 = {'x':.93, 'y':0.05}
		pos5 = {'x':1.1, 'y':0.05}
		pos6 = {'x':1.25, 'y':0.05}

		pos7 = {'x':1.25, 'y':0.25}
		pos8 = {'x':1.1, 'y':0.25}
		pos9 = {'x':.93, 'y':0.25}
		pos10= {'x':.77, 'y':0.25}
		pos11= {'x':.61, 'y':0.25}
		pos12= {'x':.45, 'y':0.25}
		
		pos13= {'x':.45, 'y':0.45}
		pos14= {'x':.61, 'y':0.45}
		pos15= {'x':.77, 'y':0.45}
		pos16= {'x':.93, 'y':0.45}
		pos17= {'x':1.1, 'y':0.45}
		pos18= {'x':1.25, 'y':0.45}
		
		pos19= {'x':1.25, 'y':0.65}
		pos20= {'x':1.1, 'y':0.65}
		pos21= {'x':.93, 'y':0.65}
		pos22= {'x':.77, 'y':0.65}
		pos23= {'x':.61, 'y':0.65}
		pos24= {'x':.45, 'y':0.65}

		pos25= {'x':.45, 'y':0.85}
		pos26= {'x':.61, 'y':0.85}
		pos27= {'x':.77, 'y':0.85}
		pos28= {'x':.93, 'y':0.85}
		pos29= {'x':1.1, 'y':0.85}
		pos30= {'x':1.25, 'y':0.85}


		layout = FloatLayout()
		# button = Button(text='Hello', size_hint=(.1, .1),pos_hint={'x':.45, 'y':0.05})

		#Testing purpose
		pos = pos9
		if d:
			if d[0] == 1:
				pos = pos1
			elif d[0] == 2:
				pos = pos2
			else:
				pos = pos3
		print pos
		# random = randint(25,30)
		# if random == 25:
		# 	pos = pos25
		# elif random == 26:
		# 	pos = pos26
		# elif random == 27:
		# 	pos = pos27
		# elif random == pos28:
		# 	pos = pos28
		# elif random == pos29:
		# 	pos = pos29
		# else:
		# 	pos = pos30
		# def __init__(self)
		button = Button(text='DICE', size_hint=(.1, .1),pos_hint=pos, background_color= [0, 0, 1, 1])
		def update(self):
			print 42424

		# button.bind(on_press=self.animate)
		# button = Button(text='Hello', size_hint=(.1, .1),pos_hint={'x':.45, 'y':0.05})
		# button = Line(circle=(150, 150, 50))
		layout.add_widget(button)
		return layout

	def board(self):
		layout = FloatLayout()

		b = Image(source="board.jpg", pos_hint={'x':0, 'y':0})
		layout.add_widget(b)
		dice = self.dice()
		layout.add_widget(dice)
		return layout

	# def on_touch_down(self, touch):
	#     if 'angle' in touch.profile:
	#         print('The touch angle is', touch.a)


	def __init__(self, **kwargs):
		super(SnakeBoard,self).__init__(**kwargs)
		# self.on_touch_down
		self.cols = 2

		self.add_widget(self.leftside())
		self.add_widget(self.board())

		# self.add_widget(Image(source="board.jpg"))

class SnakeApp(App):
	def build(self):
		return SnakeBoard()

if __name__ == '__main__':
	SnakeApp().run()