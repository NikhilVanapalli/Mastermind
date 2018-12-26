import tkinter as tk
import random
import collections

class Mastermind:
	def __init__(self, parent):
		self.parent = parent
		self.canvas = tk.Canvas(parent)
		self.status = tk.Label(parent)
		self.draw_board()
	def draw_board(self, event=None):
		self.canvas.destroy()
		self.status.destroy()
		self.canvas = tk.Canvas(self.parent, width=1030, height=500)
		self.canvas.pack()
		#self.status.config(text='Begin!')
		self.bag = { 'r' : self.canvas.create_oval(960, 6, 1027, 68+3, fill='red', outline='red'),
					 'o' : self.canvas.create_oval(960, 73+3, 1027, 138+3, fill='orange', outline='orange'),
					 'y' : self.canvas.create_oval(960, 143+3, 1027, 208+3, fill='yellow', outline='yellow'),
					 'g' : self.canvas.create_oval(960, 215+3, 1027, 280+3, fill='green', outline='green'),
					 'b' : self.canvas.create_oval(960, 285+3, 1027, 350+3, fill='blue', outline='blue'),
					 'p' : self.canvas.create_oval(960, 355+3, 1027, 420+3, fill='purple', outline='purple'),
					 'i' : self.canvas.create_oval(960, 425+3, 1027, 492+3, fill='indigo', outline='indigo')
					}
		#self.status.config(text="Begin!!!")
		self.ids = {v:k for k,v in self.bag.items()}
		self.colors = {'r' : 'red', 'o' : 'orange', 'y' : 'yellow',
		               'g' : 'green', 'b' : 'blue', 'p' : 'purple',
		               'i' : 'indigo'}
		self.guesses = ['']
		self.status = tk.Label(self.parent)
		self.status.pack()
		self.canvas.bind('<1>', self.check)
		self.parent.bind('<Control-n>', self.draw_board)
		self.parent.bind('<Control-N>', self.draw_board)
		self.pattern = [random.choice('roygbp') for _ in range(4)]
		self.counted = collections.Counter(self.pattern)
	def check(self, event=None):
		id = self.canvas.find_withtag("current")[0]
		guess = self.ids[id]
		self.guesses[-1] += guess
		y_offset = (len(self.guesses[-1]) - 1) * 80 + 5
		x_offset = (len(self.guesses) - 1) * 80 + 5
		self.canvas.create_oval(x_offset, y_offset, x_offset+75, y_offset+75,
		                        fill=self.colors[guess], outline=self.colors[guess])
		if len(self.guesses[-1]) < 4:
			return
		guess_count = collections.Counter(self.guesses[-1])
		close = sum(min(self.counted[k], guess_count[k]) for k in self.counted)
		exact = sum(a==b for a,b in zip(self.pattern, self.guesses[-1]))
		close -= exact
		colors = exact*['white'] + close*['black']
		key_coordinates = [(x_offset+5, 320+15, x_offset+40-5, 360+5),
		                   (x_offset+5, 360+15, x_offset+40-5, 400+5),
		                   (x_offset+40+5, 320+15, x_offset+80-5, 360+5),
		                   (x_offset+40+5, 360+15, x_offset+80-5, 400+5)]
		for color, coord in zip(colors, key_coordinates):
			self.canvas.create_oval(coord, fill=color, outline=color)
		if exact == 4:
			self.status.config(text='You Win!!!')
			self.canvas.unbind('<1>')
		elif len(self.guesses) > 10:
			self.status.config(text='Out of Guesses. The correct answer is {}.'.format(
				               ''.join(self.pattern)))
			self.canvas.unbind('<1>')
		else:
			self.guesses.append('')
# 
# root = tk.Tk()
# game = Mastermind(root)
# root.mainloop()
