import tkinter as tk

def insert_all(v,result_Entry):
    global expression 
    result_Entry.insert(len(result_Entry.get()),v)
    expression = result_Entry.get()

def equallto():
    global expression
    r = str(eval(str(expression))) 
    result_Entry.delete(0,tk.END)
    result_Entry.insert(0,r)

def clear():
    result_Entry.delete(0,tk.END)
def backspace():
    a = result_Entry.get()
    result_Entry.delete(0, tk.END)
    result_Entry.insert(0, a[:-1])
def percentage():
    global expression
    b = result_Entry.get()
    r = str(((eval(str(b))))/100)

    result_Entry.delete(0,tk.END)
    result_Entry.insert(0,r)
    expression = r

root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False, False)
root.configure(bg="#2C3E50")

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

result_Entry=tk.Entry(root)
result_Entry.grid(row=0,column=0,columnspan=4,sticky="nsew")

b_7=tk.Button(root,text="7",command=lambda: insert_all("7",result_Entry))
b_7.grid(row=2,column=0,sticky="nsew")
b_4=tk.Button(root,text="4",command=lambda: insert_all("4",result_Entry))
b_4.grid(row=3,column=0,sticky="nsew")
b_1=tk.Button(root,text="1",command=lambda: insert_all("1",result_Entry))
b_1.grid(row=4,column=0,sticky="nsew")
b_Delete=tk.Button(root,text="Delete",command=clear)
b_Delete.grid(row=1,column=1,columnspan=2,sticky="nsew")
b_8=tk.Button(root,text="8",command=lambda: insert_all("8",result_Entry))
b_8.grid(row=2,column=1,sticky="nsew")
b_5=tk.Button(root,text="5",command=lambda: insert_all("5",result_Entry))
b_5.grid(row=3,column=1,sticky="nsew")
b_2=tk.Button(root,text="2",command=lambda: insert_all("2",result_Entry))
b_2.grid(row=4,column=1,sticky="nsew")
b_0=tk.Button(root,text="0",command=lambda: insert_all("0",result_Entry))
b_0.grid(row=5,column=1,sticky="nsew")
b_9=tk.Button(root,text="9",command=lambda: insert_all("9",result_Entry))
b_9.grid(row=2,column=2,sticky="nsew")
b_6=tk.Button(root,text="6",command=lambda: insert_all("6",result_Entry))
b_6.grid(row=3,column=2,sticky="nsew")
b_3=tk.Button(root,text="3",command=lambda: insert_all("3",result_Entry))
b_3.grid(row=4,column=2,sticky="nsew")

b_dot=tk.Button(root,text=".",command=lambda: insert_all(".",result_Entry))
b_dot.grid(row=5,column=2,sticky="nsew")

b_pm=tk.Button(root,text="%",command=percentage)
b_pm.grid(row=5,column=0,sticky="nsew")

b__=tk.Button(root,text="⌫",command=backspace)
b__.grid(row=1,column=0,sticky="nsew")

b_equallto=tk.Button(root,text="=",command=equallto)
b_equallto.grid(row=5,column=3,sticky="nsew")
b_divide=tk.Button(root,text="/",command=lambda: insert_all("/",result_Entry))
b_divide.grid(row=1,column=3,sticky="nsew")
b_multiply=tk.Button(root,text="x",command=lambda: insert_all("*",result_Entry))
b_multiply.grid(row=2,column=3,sticky="nsew")
b_subtract=tk.Button(root,text="-",command=lambda: insert_all("-",result_Entry))
b_subtract.grid(row=3,column=3,sticky="nsew")
b_add=tk.Button(root,text="+",command=lambda: insert_all("+",result_Entry))
b_add.grid(row=4,column=3,sticky="nsew")

root.mainloop()