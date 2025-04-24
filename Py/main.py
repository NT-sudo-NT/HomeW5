from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("640x480")

canvas = Canvas(bg="white", width=640, height=480)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_rectangle(10, 10, 630, 470)
canvas.create_rectangle(10, 10, 100, 80)
canvas.create_rectangle(100, 10, 280, 80)
canvas.create_rectangle(280, 10, 420, 80)
canvas.create_rectangle(280, 10, 630, 80)

canvas.create_rectangle(10, 80, 100, 150)
canvas.create_rectangle(10, 80, 100, 150)
canvas.create_rectangle(100, 80, 280, 150)
canvas.create_rectangle(280, 80, 420, 150)
canvas.create_rectangle(280, 80, 630, 150)

canvas.create_rectangle(280, 50, 630, 10)

# canvas.create_rectangle(10, 80, 100, 150)
# canvas.create_rectangle(100, 80, 280, 150)
# canvas.create_rectangle(280, 80, 420, 150)
# canvas.create_rectangle(280, 80, 630, 150)
root.mainloop()