"""
Идея: создать небольшое оконное приложение с помощью tkinter для работы с БД PostreSQL.
Функционал оконного приложения:
    - Возможность отправлять БД CRUD запросы
    - Визуализация запросов SELECT
    - Возможность выбора запроса из уже созданных запросов
    - Отображение статуса запроса (OK - выполнен, FAIL - не выполнен)
    - Дополнительная проверка с помощью всплывающего окна при отправке запросов UPDATE, CREATE, INSERT, DELETE
    - Возможность отправлять БД запросы помимо созданных заранее с помощью текстового окна *код запроса*
"""

from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

import psycopg2


def select_bd(text):
    with con:
        with con.cursor() as a:
            a.execute(text)

            rows = a.fetchall()
            output = []
            for row in rows:
                output.append(list(map(
                    lambda item: item.rstrip() if type(item) == str else item,
                    row)
                ))
            return output, a.description


def change_bd(text):
    with con:
        with con.cursor() as a:
            a.execute(text)
            if messagebox.askquestion("askquestion", "Are you sure?") == 'no':
                con.rollback()
            else:
                con.commit()


def callbackFunc(event):
    txt.delete(1.0, END)
    with path.joinpath(x.get() + '.txt').open() as file:
        text = file.read().split('----')[0]
        txt.insert(INSERT, text)


def click_chg():
    try:
        change_bd(txt.get(1.0, END).rstrip())
        txt_status.delete(1.0, END)
        txt_status.insert(INSERT, 'OK')
    except Exception:
        txt_status.delete(1.0, END)
        txt_status.insert(INSERT, 'FAIL')
        print(Exception)
        return


def click():
    for i in trv.get_children():
        trv.delete(i)
    try:
        result, columns = select_bd(txt.get(1.0, END).rstrip())
        txt_status.delete(1.0, END)
        txt_status.insert(INSERT, 'OK')
    except Exception:
        txt_status.delete(1.0, END)
        txt_status.insert(INSERT, 'FAIL')
        return
    num = ['#' + str(i) for i in range(1, len(columns) + 1)]
    trv.config(columns=num)
    for i, j in zip(num, columns):
        trv.heading(i, text=j[0])
        trv.column(i, width=100, stretch=False)
    for item in result:
        trv.insert('', END, values=item)


con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwerty123456",
    host="127.0.0.1",
    port="5432"
)

path = Path('/Postgre_Project/Postgre_SQL')  # Путь к папке с SQL запросами
sql_querys = list(map(lambda a: a.name.split('.')[0], Path().glob("**/Postgre_SQL/*")))

window = Tk()
window.geometry('1470x600')
window.title('Select request')

x_lbl_cmbox_btn = 850

lbl = Label(window, text="Выберите запрос из списка", font=("Arial Bold", 16))
lbl.place(x=x_lbl_cmbox_btn, y=450)

x = StringVar()
cmbox = Combobox(window, values=sql_querys, state='readonly', width=55, height=20, textvariable=x)
cmbox.place(x=x_lbl_cmbox_btn, y=480)
cmbox.bind("<<ComboboxSelected>>", callbackFunc)

btn = Button(window, text='Показать\nрезультат запроса', bd=5, width=17, height=2, command=click,
             font=("Arial Bold", 12))
btn.place(x=x_lbl_cmbox_btn, y=514)

btn_chg = Button(window, text='Внести\nизменения в БД', bd=5, width=17, height=2, command=click_chg,
                 font=("Arial Bold", 12))
btn_chg.place(x=x_lbl_cmbox_btn + 185, y=514)

txt = Text(window, width=102, height=36)
txt.place(x=5, y=5)

tree_frame = Frame(window)
tree_frame.pack()

gorizscrlbar = Scrollbar(window, orient="horizontal")
trv = Treeview(window, show="headings", height=20, columns=('#1', '#2', '#3'), selectmode='browse',
               yscrollcommand=gorizscrlbar.set)
gorizscrlbar.place(x=850, y=432, width=603)
gorizscrlbar.config(command=trv.xview)
trv.place(x=850, y=5)

txt_status = Text(window, width=4, height=1, font=("Arial Bold", 44))
txt_status.place(x=x_lbl_cmbox_btn + 435, y=485)

window.mainloop()
