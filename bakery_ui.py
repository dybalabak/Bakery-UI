import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        self.label1 = Label(window, text="샌드위치 (5000원)", font=("돋음", 16))
        self.label1.grid(column=0, row=0)
        self.input1 = Entry(window, width=10, borderwidth=2)
        self.input1.grid(column=1, row=0)
        self.label2 = Label(window, text="케이크 (20000원)", font=("돋음", 16))
        self.label2.grid(column=0, row=1)
        self.input2 = Entry(window, width=10, borderwidth=2)
        self.input2.grid(column=1, row=1)
        button = Button(window, text="주문하기", command= self.send_order)
        button.grid(column=1, row=2)
        window.geometry('350x200')

    def send_order(self):
        if self.input1.get().isdigit() and int(self.input1.get()) > 0 and self.input2.get().isdigit() and int(self.input2.get()) > 0:
            order_text = self.name + ": " + self.label1["text"] + " " + self.input1.get() + "개, " + self.label2["text"] + " " + self.input2.get() + "개"
            self.bakeryView.add_order(order_text)
        elif self.input1.get().isdigit() and int(self.input1.get()) > 0:
            order_text = self.name + ": " + self.label1["text"] + " " + self.input1.get() + "개"
            self.bakeryView.add_order(order_text)
        elif self.input2.get().isdigit() and int(self.input2.get()) > 0:
            order_text = self.name + ": " + self.label2["text"] + " " + self.input2.get() + "개"
            self.bakeryView.add_order(order_text)
        else:
            pass


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
