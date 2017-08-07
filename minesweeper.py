from Tkinter import Tk, W, E
from ttk import Frame, Button, Entry, Style, Label
import tkMessageBox
import random
import sys


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

def callback(x, y):
    loc = str(x)
    loc += ','
    loc += str(y)
    pos = helper(x, y)
    loc += ' - '
    loc += str(pos)
    print(loc)

    global firstMove
    if firstMove:
    	firstMove = False
    	createBoard(x,y)
    	checkBombs()
    	for x in range(0, len(array)):
    		print(array[x])

    global flagBool
    if flagBool:
    	if str(buttons[pos]['text']) != '?':
    		buttons[pos].configure(text='?')
    	else:
    		buttons[pos].configure(text='')
    elif str(buttons[pos]['text']) != '?':
    	getNeighbors(x,y)
    
    # find button in list
    # through helper

    #helper function for moves
    # checkMove(x,y,pos)

def checkMove(x, y, pos):
	if array[x][y] == '#':
		# found bomb, game over display message box
		tkMessageBox.showerror("Gameover", "Oh no, you selected a bomb! Try again")
	elif array[x][y] == 0:
		# need to open up all neighbors that are 0
		buttons[pos].configure(text='0')
		buttons[pos].configure(state='disabled')
		checkNeighbors(x,y, pos)
	else:
		buttons[pos].configure(text=str(array[x][y]))
		buttons[pos].configure(state='disabled')



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
	global flagBool
	flagBool = not flagBool
	if flagBool:
		flag.configure(text='unflag')
	else:
		flag.configure(text='flag')



# ******* Create grid ******** #

# createBoard()

# checkBombs()

# for x in range(0,8):
# 	for y in range(0,8):
# 		checkBombs(x,y)

root = Tk()
buttons = []
for x in range(0,8):
	for y in range(0,8):
		button = Button(root, width=1, command=lambda x=x, y=y: callback(x,y) )
		button.grid(row=x, column=y)
		buttons.append(button)

newGame = Button(root, width=5, text='new')
newGame.grid(row=8, column=0, columnspan=2)
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

# def checkNeighbors(x, y, pos):

# 	topLeft = helper(x-1,y-1)
# 	top = helper(x-1,y)
# 	topRight = helper(x-1,y+1)
# 	left = helper(x,y-1)
# 	right = helper(x,y+1)
# 	botLeft = helper(x+1,y-1)



# 	bot = helper(x+1,y)
# 	botRight = helper(x+1,y+1)
	
# 	if array[x-1][y-1] == 0 and str(buttons[topLeft]['state']) == 'normal':
# 		buttons[topLeft].configure(text='0', state='disabled')
# 		checkNeighbors(x-1, y-1, topLeft)
# 	# elif str(buttons[topLeft]['state']) == 'normal':
# 	# 	buttons[topLeft].configure(text=str(array[x-1][y-1]), state='disabled')

# 	if array[x-1][y] == 0 and str(buttons[top]['state']) == 'normal':
# 		buttons[top].configure(text='0', state='disabled')
# 		checkNeighbors(x-1, y, top)
# 	# elif str(buttons[top]['state']) == 'normal':
# 	# 	buttons[top].configure(text=str(array[x-1][y]), state='disabled')

# 	if array[x-1][y+1] == 0 and str(buttons[topRight]['state']) == 'normal':
# 		buttons[topRight].configure(text='0', state='disabled')
# 		checkNeighbors(x-1, y+1, topRight)
# 	# elif str(buttons[topRight]['state']) == 'normal':
# 	# 	buttons[topRight].configure(text=str(array[x-1][y+1]), state='disabled')

# 	if array[x][y-1] == 0 and str(buttons[left]['state']) == 'normal':
# 		buttons[left].configure(text='0', state='disabled')
# 		checkNeighbors(x, y-1, left)
# 	# elif str(buttons[left]['state']) == 'normal':
# 	# 	buttons[left].configure(text=str(array[x][y-1]), state='disabled')

# 	if array[x][y+1] == 0 and str(buttons[right]['state']) == 'normal':
# 		buttons[right].configure(text='0', state='disabled')
# 		checkNeighbors(x, y+1, right)
# 	# elif str(buttons[right]['state']) == 'normal':
# 	# 	buttons[right].configure(text=str(array[x][y+1]), state='disabled')

# 	if array[x+1][y-1] == 0 and str(buttons[botLeft]['state']) == 'normal':
# 		buttons[botLeft].configure(text='0', state='disabled')
# 		checkNeighbors(x+1, y-1, botLeft)
# 	# elif str(buttons[botLeft]['state']) == 'normal':
# 	# 	buttons[botLeft].configure(text=str(array[x+1][y-1]), state='disabled')

# 	if array[x+1][y] == 0 and str(buttons[bot]['state']) == 'normal':
# 		buttons[bot].configure(text='0', state='disabled')
# 		checkNeighbors(x+1, y, bot)
# 	# elif str(buttons[bot]['state']) == 'normal':
# 	# 	buttons[bot].configure(text=str(array[x+1][y]), state='disabled')

# 	if array[x+1][y+1] == 0 and str(buttons[botRight]['state']) == 'normal':
# 		buttons[botRight].configure(text='0', state='disabled')
# 		checkNeighbors(x+1, y+1, botRight)
# 	# elif str(buttons[botRight]['state']) == 'normal':
# 	# 	buttons[botRight].configure(text=str(array[x+1][y+1]), state='disabled')
