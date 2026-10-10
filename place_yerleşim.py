import tkinter as tk

root=tk.Tk()
root.title("Place Kullanimi")
root.geometry("400x300")

label1=tk.Label(root, text="Mutlak değişim (x=50,y=50)", bg="lightblue")
label1.place(x=50,y=50)

label2=tk.Label(root, text="Mutlak yerleşim x=150,y=70", bg="pink")
label2.place(x=60,y=70)

label3=tk.Label(root, text="Göreceli yerleşim (relx=0.5 rely=0.8)", bg="yellow")
label3.place(relx=0.5, rely=0.8, anchor="center")

label4=tk.Label(root,text="Göreceli yükeklik genişlik", bg="green")
label4.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)

root.mainloop()