from Tkinter import *
from ttk import Frame, Button, Entry, Style, Label
import tkMessageBox
import random
import sys

#EVENTUALLY CHANGE TO CLASS


# class Example(Frame, object):
  
#     def __init__(self, master):
#         super(Example, self).__init__(master)   
         
#         self.initUI()

        
#     def initUI(self):
      
#         self.master.title("Minesweeper")
        
#         Style().configure("TButton", padding=(0, 0, 0, 0), 
#             font='serif 10')

#         width = 8
#         height = 8
#         bomb = 10
#         for x in range(0, width):
#         	for y in range(0, height):
#         		button = Button(self, width=1, command=callback)
#         		button.grid(row=x, column=y)

#         array = [[0 for x in range(width)] for y in range(height)]
#         for x in range(0, len(array)):
#         	print(array[x])
        
#         self.pack()

array = [[0 for x in range(8)] for y in range(8)]
flagBool = False
firstMove = True
buttons = []
bombs = 10
counter = 0
endTimer = False

def callback(x, y):

    global flagBool, firstMove, bombs
    pos = helper(x, y)
    # check if flagging is turned on
    if flagBool:
    	if str(buttons[pos]['text']) != '?':
    		buttons[pos].configure(text='?')
    		bombs -= 1
    		bombsLeft.configure(text=str(bombs))
    	else:
    		buttons[pos].configure(text='')
    		bombs += 1
    		bombsLeft.configure(text=str(bombs))
    elif str(buttons[pos]['text']) != '?':
    	# check to see if first move, else play normally
	    if firstMove:
	    	firstMove = False
	    	startTimer(timer)
	    	createBoard(x,y)
	    	checkBombs()
	    	for a in range(0, len(array)):
	    		print(array[a])
	    	move(x,y,pos)
	    else:
	    	move(x,y,pos)
	    gameOver()

def gameOver():
	count = 0
	global endTimer
	for button in buttons:
		if str(button['state']) == 'normal':
			count += 1
	if count == 10:
		tkMessageBox.showinfo('Congratulations!!', 'You have uncovered all of the mines!')
		endTimer = True
		return True
	return False

def endGame():
	global endTimer
	endTimer = True
	for x in range(0, len(array)):
		for y in range(0, len(array[x])):
			if array[x][y] == '#':
				buttons[helper(x,y)].configure(text='#', state='disabled')

def move(x, y, pos):
	if array[x][y] == '#':
		# found bomb, game over display message box
		endGame()
		tkMessageBox.showerror("Gameover", "Oh no, you selected a bomb! Try again")
		newGame()
	elif array[x][y] == 0:
		# need to open up all neighbors that are 0
		buttons[pos].configure(text=str(array[x][y]), state='disabled')
		checkNeighbors(x,y)
	else:
		buttons[pos].configure(text=str(array[x][y]), state='disabled')


def checkNeighbors(x,y):
	locs = getNeighbors(x,y)
	for loc in locs:
		print(loc)
		# get position of button
		pos = 'checking: ('
		pos += str(loc.get('x'))
		pos += ','
		pos += str(loc.get('y'))
		pos += ')'
		print(pos)
		index = helper(loc.get('x'), loc.get('y'))
		print (buttons[index]['state'])
		if str(buttons[index]['state']) == 'normal':
			print 'state was normal'
			if loc.get('val') != 0:
				print 'Value WAS NOT zero'
				buttons[index].configure(text=str(loc.get('val')), state='disabled')
			else:
				print 'Value WAS zero'
				buttons[index].configure(text=str(loc.get('val')), state='disabled')
				checkNeighbors(loc.get('x'), loc.get('y'))


def helper(x, y):
	pos = x*8
	pos += y
	return pos

def createBoard(x, y):
	count = 10
	while count > 0:
		xVal = random.randint(0,7)
		yVal = random.randint(0,7)
		if xVal != x and yVal != y:
			if array[xVal][yVal] == 0:
				array[xVal][yVal] = '#'
				count -= 1

def getNeighbors(x, y):
	# create list of dic object that are the neighbor coordinates
	locs = []
	for a in range(-1,2):
		if (x-1 >= 0) and (y+a >= 0) and (y+a <= 7):
			# neighbors on the row above
			locs.append({
				'x' : (x-1),
				'y' : (y+a),
				'val' : array[x-1][y+a]
				})
		
		if (y+a >= 0) and (y+a <= 7):
			# neighbors in same row
			if a != 0:
				locs.append({
					'x' : (x),
					'y' : (y+a),
					'val' : array[x][y+a]
					})

		if (x+1 <= 7) and (y+a >= 0) and (y+a <= 7):
			# neighbors on row below
			locs.append({
				'x' : (x+1),
				'y' : (y+a),
				'val' : array[x+1][y+a]
				})
	return locs

	

# fix, try to get rid of duplicate code
def checkBombs():
	for x in range(0,8):
		for y in range(0,8):
			if array[x][y] != '#':

				locs = getNeighbors(x,y)
				count = 0
				for loc in locs:
					if loc.get('val') == '#':
						count += 1

				array[x][y] = count

def setFlag():
	print 'set flag'
	global flagBool
	flagBool = not flagBool
	if flagBool:
		flag.configure(text='unflag')
	else:
		flag.configure(text='flag')

def startTimer(timer):
	counter = 0
	def count():
		global counter
		counter += 1
		timer.configure(text=str(counter))
		timer.after(1000, count)
	count()

def newGame():
	print 'new game'
	global array, buttons, firstMove, counter
	counter = 0
	array = [[0 for x in range(8)] for y in range(8)]
	firstMove = True
	for button in buttons:
		button.configure(text='', state='normal')


root = Tk()

menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="New Game", command=newGame)
menu.add_separator()
menu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=menu)

root.config(menu=menubar)

for x in range(0,8):
	for y in range(0,8):
		button = Button(root, width=1, command=lambda x=x, y=y: callback(x,y) )
		button.grid(row=x, column=y)
		buttons.append(button)

bombsLeft = Button(root, width=5, text=str(bombs))
bombsLeft.grid(row=8, column=0, columnspan=2)
timer = Label(root, foreground='red', text='timer')
timer.grid(row=8, column=3, columnspan=2)
flag = Button(root, width=5, text='flag', command=lambda : setFlag())
flag.grid(row=8, column=6, columnspan=2)


root.mainloop()


# def main():
  
#     root = Tk()
#     app = Example(root)
#     root.mainloop()  


# if __name__ == '__main__':
#     main()  

