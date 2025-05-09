from tkinter import *

root = Tk()
root.title("Tk")
root.geometry("640x480")

canvas = Canvas(bg="white", width=640, height=480)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_rectangle(10, 10, 630, 470)
canvas.create_text(50, 50, font = "Arial 16", text = "ID")
canvas.create_line(100, 50, 100, 470)
canvas.create_rectangle(10, 10, 100, 80)
canvas.create_text(150, 50, font = "Arial 16", text = "NOTE")
canvas.create_rectangle(100, 10, 280, 80)
# canvas.create_line(280, 50, 280, 470)
# canvas.create_line(100, 105, 100, 470)
# canvas.create_line(100, 140, 100, 470)
# canvas.create_line(100, 175, 100, 470)
# canvas.create_line(100, 210, 100, 470)
canvas.create_text(330, 50, font = "Arial 16", text = "Prioritet")
canvas.create_rectangle(280, 10, 420, 80)
canvas.create_rectangle(280, 10, 630, 80)

canvas.create_rectangle(10, 80, 100, 150)
canvas.create_text(50, 117, font = "Arial 16", text = "1")
canvas.create_rectangle(10, 80, 100, 150)
canvas.create_text(180, 117, font = "Arial 16", text = "Текст заметки")
canvas.create_rectangle(100, 80, 280, 150)
canvas.create_text(345, 117, font = "Arial 16", text = "2")
canvas.create_rectangle(280, 80, 420, 150)
canvas.create_rectangle(280, 80, 630, 150)

canvas.create_rectangle(420, 10, 630, 45)
canvas.create_text(475, 30, font = "Arial 16", text = "Удаление")
canvas.create_rectangle(420, 10, 630, 115)
canvas.create_text(485, 65, font = "Arial 16", text = "Добавление")
canvas.create_rectangle(420, 10, 630, 200)
canvas.create_text(480, 100, font = "Arial 16", text = "Изменение")
canvas.create_text(493, 135, font = "Arial 16", text = "Отображение")
canvas.create_line(420, 80, 420, 470)
root.mainloop()