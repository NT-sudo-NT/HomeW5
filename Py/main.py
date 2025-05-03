import sqlite3
import tkinter as tk
from tkinter import Canvas

# Функции работы с базой данных
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def add_note_to_db(note, category, conn):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (text, category) VALUES (?, ?)', (note, category))
    conn.commit()

def update_note_in_db(note_id, new_content, new_category, conn):
    cursor = conn.cursor()
    cursor.execute('UPDATE notes SET text = ?, category = ? WHERE id = ?', (new_content, new_category, note_id))
    conn.commit()

def delete_note_from_db(note_id, conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()

# Функции для кнопок
def add_note():
    note = note_entry.get()
    category = category_entry.get()
    if note and category:
        add_note_to_db(note, category, conn)
        note_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        refresh_notes_display()

def update_note():
    note_id = note_id_entry.get()
    new_content = note_entry.get()
    new_category = category_entry.get()
    if note_id.isdigit() and new_content and new_category:
        update_note_in_db(int(note_id), new_content, new_category, conn)
        note_id_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        refresh_notes_display()

def delete_note():
    note_id = note_id_entry.get()
    if note_id.isdigit():
        delete_note_from_db(int(note_id), conn)
        note_id_entry.delete(0, tk.END)
        refresh_notes_display()

def show_all_notes():
    refresh_notes_display()  # Обновляем отображение заметок

# Функция для обновления отображения заметок в интерфейсе
def refresh_notes_display():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    
    # Очищаем предыдущие заметки в интерфейсе
    for widget in canvas.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_y() < 100:
            widget.destroy()

    # Отображаем все заметки
    y_position = 95
    for note in notes:
        note_id, text, category = note
        canvas.create_text(50, y_position, font="Arial 16", text=str(note_id))
        canvas.create_text(180, y_position, font="Arial 16", text=text)
        canvas.create_text(345, y_position, font="Arial 16", text=category)
        y_position += 35

# Инициализация базы данных
conn = init_db()

# Создание основного окна
root = tk.Tk()
root.title("Заметки")
root.geometry("640x480")

canvas = Canvas(bg="white", width=640, height=480)
canvas.pack(anchor=tk.CENTER, expand=1)

# Создание интерфейса
canvas.create_rectangle(10, 10, 630, 470)
canvas.create_text(50, 50, font="Arial 16", text="ID")
canvas.create_line(100, 50, 100, 470)
canvas.create_rectangle(10, 10, 100, 80)
canvas.create_text(150, 50, font="Arial 16", text="NOTE")
canvas.create_rectangle(100, 10, 280, 80)
canvas.create_line(280, 50, 280, 470)
canvas.create_text(330, 50, font="Arial 16", text="Категория")
canvas.create_rectangle(280, 10, 420, 80)
canvas.create_rectangle(280, 10, 630, 80)

# Поля для ввода заметки и категории
note_id_entry = tk.Entry(root, width=22)
note_id_entry.place(x=421, y=201)

note_entry = tk.Entry(root, width=22)
note_entry.place(x=421, y=223)

category_entry = tk.Entry(root, width=22)
category_entry.place(x=421, y=245)

# Кнопки управления
canvas.create_rectangle(420, 10, 630, 45)
canvas.create_text(475, 30, font="Arial 16", text="Удаление")
canvas.create_rectangle(420, 10, 630, 115)
canvas.create_text(485, 65, font="Arial 16", text="Добавление")
canvas.create_rectangle(420, 10, 630, 200)
canvas.create_text(480, 100, font="Arial 16", text="Изменение")
canvas.create_text(493, 135, font="Arial 16", text="Отображение")
canvas.create_line(420, 80, 420, 470)
btn_delete = tk.Button(root, text="Удаление", command=delete_note)
btn_delete.place(x=420, y=10, width=210, height=35)

btn_add = tk.Button(root, text="Добавление", command=add_note)
btn_add.place(x=420, y=45, width=210, height=35)

btn_update = tk.Button(root, text="Изменение", command=update_note)
btn_update.place(x=420, y=80, width=210, height=35)

btn_show_all = tk.Button(root, text="Отображение", command=show_all_notes)
btn_show_all.place(x=420, y=115, width=210, height=35)

# Запуск основного цикла приложения
refresh_notes_display()  # Обновляем отображение заметок при старте
root.mainloop()

# Закрываем соединение с базой данных
conn.close()