import tkinter as tk

def tikla1():
    print("button one clicked!")
    ticket1.config(text="button one  clicked!")
def tikla2():
    print("button two clicked")
    ticket2.config(text="button two clicked!")
def reset3():
    ticket1.config(text="this is one component!")
    ticket2.config(text="this is second component!")
def tikla4():
    text=input1.get()
    print("entered in the text box:", text)
    ticket2.config(text=text)
    ticket1.config(text=text)
    
def Add():
    number1=int(entry_number1.get())
    number2=int(entry_number2.get())
    conclusion=number1+number2
    conclusion_ticket.config(text=f"conclusion: {conclusion}")
    
def show_select():
    select=[]
    if var_python.get():
        select.append("Python")
    if var_cpp.get():
        select.append("C++")
    if var_java.get():
        select.append("Java")
        
    conclusion_ticket.config(text="selected: " +"," .join(conclusion_ticket))

def show_gender():
    selected=show_gender.get()
    if selected =="man":
        gender_label.config(text="selected gender: man")
    elif selected =="woman":
        gender_label.config(text="please selected you structure!")
        
    
window = tk.Tk()
window.title("Hello Tkinter!")
window.geometry("700x500")

ticket1=tk.Label(window, text="this is one component!")
ticket1.pack()

ticket2=tk.Label(window, text="this is second componet!")
ticket2.pack()


button1=tk.Button(window, text="click me one ", command=tikla1 ,bg="blue", fg="white")
button1.pack()
button2=tk.Button(window, text="click me second",command=tikla2)
button2.pack()
button3=tk.Button(window,text="reset", command=reset3)
button3.pack()
input1=tk.Entry(window)
input1.pack()
buton4=tk.Button(window, text="write the text", command=tikla4)
buton4.pack()

entry_number1=tk.Entry(window)
entry_number1.pack()

entry_number2=tk.Entry(window)
entry_number2.pack()

buton_addition=tk.Button(window, text="addition: ", command=Add,  bg="blue", fg="white")
buton_addition.pack()

conclusion_ticket=tk.Label(window, text="conclusion:", bg="red", fg="white")
conclusion_ticket.pack()
#Checbuttonlar için IntVar() tanımlıyoruz:
var_python=tk.IntVar
var_cpp=tk.IntVar
var_java=tk.IntVar
cb1=tk.Checkbutton(window, text="Python", variable=var_python)
cb2=tk.Checkbutton(window, text="c++", variable=var_cpp)
cb3=tk.Checkbutton(window, text="java", variable=var_java)
cb1.pack()
cb2.pack()
cb3.pack()
show_buton=tk.Button(window,text="show selected", command=show_select)
show_buton.pack()

#RadioButtonlar için StrinVar'lar kullanılır 
var_gender=tk.StringVar()
var_gender.set(None)
rb_man=tk.Radiobutton(window, text="man", variable=var_gender, value="man")
rb_woman=tk.Radiobutton(window, text="woman",variable=var_gender, value="woman")
rb_man.pack()
rb_woman.pack()

gender_buuton=tk.Button(window, text="show gender",command=show_gender)
gender_buuton.pack()

gender_label=tk.Label(window, text="")
window.mainloop()