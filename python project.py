from tkinter import*
import random
project=Tk()
def game():
	sub=Tk()
	sub.title("ROCK,PAPER,SCISSOR GAME")
	label7=Label(sub,text=("Select your choice"))
	label7.pack()
	def paper():
		words=("Rock","Paper","Scissors")
		c=str(random.choice(words))
		label2=Label(sub,text=("Opponent: "+random.choice(words)))
		label2.pack()
		label4=Label(sub,text=("Your choice: Paper"))
		label4.pack()
		if c=="Rock":
			label8=Label(sub,text=("You Won"))
			label8.pack()
		elif c=="Paper":
			label9=Label(sub,text=("Its a Tie"))
			label9.pack()
		elif c=="Scissors":
			label10=Label(sub,text=("You Lose"))
			label10.pack()
	def rock():
		words=("Rock","Paper","Scissors")
		c=random.choice(words)
		label1=Label(sub,text=("Opponent: "+random.choice(words)))
		label1.pack()
		label5=Label(sub,text="Your choice: Rock")
		label5.pack()
		if c=="Rock":
			label8=Label(sub,text=("Its a Tie"))
			label8.pack()
		elif c=="Paper":
			label9=Label(sub,text=("You Lose"))
			label9.pack()
		elif c=="Scissors":
			label10=Label(sub,text=("You Won"))
			label10.pack()
	def scissors():
		words=("Rock","Paper","Scissors")
		c=random.choice(words)
		label3=Label(sub,text=("Opponent: "+random.choice(words)))
		label3.pack()
		label6=Label(sub,text=("Your choice: Scissors"))
		label6.pack()
		if c=="Rock":
			label8=Label(sub,text=("You Lose"))
			label8.pack()
		elif c=="Paper":
			label9=Label(sub,text=("You Won"))
			label9.pack()
		elif c=="Scissors":
			label10=Label(sub,text=("Its a Tie"))
			label10.pack()
	button1=Button(sub,text="Rock",command=rock)
	button1.pack()
	button2=Button(sub,text="Paper",command=paper)
	button2.pack()
	button3=Button(sub,text="Scissors",command=scissors)
	button3.pack()
	sub.mainloop()
def cal():
	   main=Tk()
	   main.title("CALCULATOR")
	   e = Entry(main)
	   e.grid(row=0,column=0,columnspan=4)
	   def zero():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q + "0")
	   def one():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"1")
	   def two():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"2")
	   def three():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"3")
	   def four():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"4")
	   def five():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"5")
	   def six():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"6")
	   def seven():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"7")
	   def eight():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"8")
	   def nine():
	   	q=e.get()
	   	e.delete(0,END)
	   	e.insert(0,q+"9")
	   def add():
	   	global c
	   	global b
	   	b="+"
	   	c=int(e.get())
	   	e.delete(0,END)
	   def sub():
	   	global c
	   	global b
	   	b="-"
	   	c=int(e.get())
	   	e.delete(0,END)
	   def multiply():
	   		global c
	   		global b
	   		b ="*"
	   		c=int(e.get())
	   		e.delete(0,END)
	   def divide():
	   	global c
	   	global b
	   	b="/"
	   	c=int(e.get())
	   	e.delete(0,END)
	   def clear():
	   		e.delete(0,END)
	   def equal():
	   	a=int(e.get())
	   	e.delete(0,END)
	   	if b=="+":
	   		e.insert(0,c+a)
	   	if b=="-":
	   			e.insert(0,c-a)
	   	if b=="*":
	   		e.insert(0,c*a)
	   	if b=="/":
	   		e.insert(0,c/a)
	   button0=Button(main,text=("0"),command=zero)
	   button0.grid(row=4,column=0)
	   button1=Button(main,text=("1"),command=one)
	   button1.grid(row=1,column=0)
	   button2=Button(main,text=("2"),command=two)
	   button2.grid(row=1,column=1)
	   button3=Button(main,text=("3"),command=three)
	   button3.grid(row=1,column=2)
	   button4=Button(main,text=("4"),command=four)
	   button4.grid(row=2,column=0)
	   button5=Button(main,text=("5"),command=five)
	   button5.grid(row=2,column=1)
	   button6=Button(main,text=("6"),command=six)
	   button6.grid(row=2,column=2)
	   button7=Button(main,text=("7"),command=seven)
	   button7.grid(row=3,column=0)
	   button8=Button(main,text=("8"),command=eight)
	   button8.grid(row=3,column=1)
	   button9=Button(main,text=("9"),command=nine)
	   button9.grid(row=3,column=2)
	   buttonadd=Button(main,text=("+"),command=add)
	   buttonadd.grid(row=1,column=4)
	   buttonsub=Button(main,text=("-"),command=sub)
	   buttonsub.grid(row=2,column=4)
	   buttonmultiply=Button(main,text=("*"),command=multiply)
	   buttonmultiply.grid(row=3,column=4)
	   buttondivide=Button(main,text=("/"),command=divide)
	   buttondivide.grid(row=4,column=4)
	   buttonclear=Button(main,text=("Clear"),command=clear)
	   buttonclear.grid(row=4,column=2)
	   buttonequal=Button(main,text=("Equal"),command=equal)
	   buttonequal.grid(row=4,column=1)
	   main.mainloop()
gamebutton=Button(project,text=("ROCK,PAPER,SCISSORS GAME"),command=game)
gamebutton.pack()
calbutton=Button(project,text=("CALCULATOR"),command=cal)
calbutton.pack()
project.mainloop()