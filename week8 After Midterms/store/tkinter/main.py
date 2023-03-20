from tkinter import *
import tkinter as tk


# class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)

root = tk.Tk()

#Set y,x size for tk
root.geometry("800x500")

#Set title for GUI
root.title("Shop Database GUI")

#Label is just a text, pass first is the parent
label = tk.Label(root, text="Hello World!", font=("Arial, 18"))
label.pack(padx=20, pady=20)
#textbox~~ 
textbox = tk.Text(root,height=3 ,font=("Arial", 16))
textbox.pack(padx=10)
#Button~~
# button = tk.Button(root, text="Click Me", font=("Arial", 18))
# button.pack()

#Grid Layout for buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="View All Products", font=("Arial", 18))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="Add a Product", font=("Arial", 18))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="Update a Product", font=("Arial", 18))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="Delete Product", font=("Arial", 18))
btn3.grid(row=0,column=3,sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="Create an Order", font=("Arial", 18))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="View an Order", font=("Arial", 18))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="Delete an Order", font=("Arial", 18))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)
btn7 = tk.Button(buttonframe, text="Process an Order", font=("Arial", 18))
btn7.grid(row=1,column=3,sticky=tk.W+tk.E)
btn8 = tk.Button(buttonframe, text="View Pending Orders", font=("Arial", 18))
btn8.grid(row=2,column=0,sticky=tk.W+tk.E)
btn9 = tk.Button(buttonframe, text="View Processed Orders", font=("Arial", 18))
btn9.grid(row=2,column=1,sticky=tk.W+tk.E)
btn10 = tk.Button(buttonframe, text="View Products out of stock", font=("Arial", 18))
btn10.grid(row=2,column=2,sticky=tk.W+tk.E)
btn11 = tk.Button(buttonframe, text="Find Customer Order", font=("Arial", 18))
btn11.grid(row=2,column=3,sticky=tk.W+tk.E)
btn12 = tk.Button(buttonframe, text="View an Order", font=("Arial", 18))
btn12.grid(row=3,column=0,sticky=tk.W+tk.E)

buttonframe.pack()





# myentry = tk.Entry(root)



if __name__ == "__main__":
    root.mainloop()