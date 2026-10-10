import tkinter as tk

root=tk.Tk()
root.title("TKİNTER CANVAS-FOTOĞRAF YÜKLKEME ")
root.geometry("200x200")
#canvas oluşturuyoruz 
canvas=tk.Canvas(root, width=200, height=200,bg="white")
canvas.pack()
#png veya gif dosyalarını kullanabiliriz 
resim=tk.PhotoImage(file="ferrari2.png")

canvas.create_image(0,0 ,anchor=tk.NW, image=resim)




root.mainloop()