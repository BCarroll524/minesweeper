from Tkinter import Tk, W, E
from ttk import Frame, Button, Entry, Style
import random

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

def callback(x, y):
    loc = str(x)
    loc += ','
    loc += str(y)
    pos = helper(x, y)
    loc += ' - '
    loc += str(pos)
    print(loc)
    # find button in list
    # through helper
    buttons[pos].configure(text='@')
    buttons[pos].configure(state='disabled')

def helper(x, y):
	return y + (x*8)

def createBoard():
	count = 10
	while count > 0:
		xVal = random.randint(0,7)
		yVal = random.randint(0,7)
		if xVal != yVal:
			if array[xVal][yVal] == 0:
				array[xVal][yVal] = '#'
				count -= 1
	for x in range(0, len(array)):
		print(array[x])

def checkBombs(x, y):
	if array[x][y] == '#':
		return
	count = 0

	# clean up, make smaller helper functions to reduce code copy

	if x==0 and y==0:
		if array[x][y+1] == '#':
			count += 1
		if array[x+1][y] == '#':
			count += 1
		if array[x+1][y+1] == '#':
			count += 1

	elif x==0 and y==7:
		if array[x][y-1] == '#':
			count += 1
		if array[x+1][y] == '#':
			count += 1
		if array[x+1][y-1] == '#':
			count += 1

	elif x==7 and y==0:
		if array[x-1][y] == '#':
			count += 1
		if array[x][y+1] == '#':
			count += 1
		if array[x-1][y+1] == '#':
			count += 1

	elif x==7 and y==7:
		if array[x-1][y] == '#':
			count += 1
		if array[x][y-1] == '#':
			count += 1
		if array[x-1][y-1] == '#':
			count += 1

	elif x==0 or x==7:
		if array[x][y+1] == '#':
			count += 1
		if array[x][y-1] == '#':
			count += 1
		if x==0:
			if array[x+1][y-1] == '#':
				count += 1
			if array[x+1][y] == '#':
				count += 1
			if array[x+1][y+1] == '#':
				count += 1
		else:
			if array[x-1][y-1] == '#':
				count += 1
			if array[x-1][y] == '#':
				count += 1
			if array[x-1][y+1] == '#':
				count += 1

	elif y==0 or y==7:
		if array[x-1][y] == '#':
			count += 1
		if array[x+1][y] == '#':
			count += 1
		if y==0:
			if array[x-1][y+1] == '#':
				count += 1
			if array[x][y+1] == '#':
				count += 1
			if array[x+1][y+1] == '#':
				count += 1
		else:
			if array[x-1][y-1] == '#':
				count += 1
			if array[x][y-1] == '#':
				count += 1
			if array[x+1][y-1] == '#':
				count += 1

	else:
		if array[x-1][y-1] == '#':
			count +=1
		if array[x-1][y] == '#':
			count +=1
		if array[x-1][y+1] == '#':
			count +=1
		if array[x][y-1] == '#':
			count +=1
		if array[x][y+1] == '#':
			count +=1
		if array[x+1][y-1] == '#':
			count +=1
		if array[x+1][y] == '#':
			count +=1
		if array[x+1][y+1] == '#':
			count +=1
	array[x][y] = count


createBoard()
for x in range(0,8):
	for y in range(0,8):
		checkBombs(x,y)
print '\nGrid\n'
for x in range(0, len(array)):
		print(array[x])
root = Tk()
buttons = []
for x in range(0,8):
	for y in range(0,8):
		button = Button(root, width=1, command=lambda x=x, y=y: callback(x,y) )
		button.grid(row=x, column=y)
		buttons.append(button)

print(len(buttons))
root.mainloop()


# def main():
  
#     root = Tk()
#     app = Example(root)
#     root.mainloop()  


# if __name__ == '__main__':
#     main()  