from tkinter import *
from PyHook3 import HookManager, HookConstants
from tkinter.messagebox import showinfo
from random import randint


class App:
    def __init__(self, root):
        #tutaj tworzą się wszystkie widgety
        #tutaj tworzymy fonta dla wszystkich label w __init__, można zmienić na globalną później w sumie
        font_name = 'times'
        font_size = 40
        label_font = '{0} {1}'.format(font_name, font_size)

        #HookManager odpowiada za zbieranie eventów z klawiatury gdy aplikacja jest w tle
        self.my_hook_manager = HookManager()
        self.my_hook_manager.KeyUp = self.on_keyboard_event
        self.my_hook_manager.HookKeyboard()

        #sekcja tworzenia widgetów dla gospodarzy
        gospodarze_name_string = 'Gospodarze   '
        gospodarze_name = StringVar()
        self.gospodarze_score_str = StringVar()
        self.gospodarze_score_int = 0
        gospodarze_name.set(gospodarze_name_string)
        self.gospodarze_score_str.set(str(self.gospodarze_score_int))

        gospodarze_name_label = Label(root, textvariable=gospodarze_name, font=label_font)
        gospodarze_score_label = Label(root, textvariable=self.gospodarze_score_str, font=label_font)

        gospodarze_name_label.grid(column=0, row=0)
        gospodarze_score_label.grid(column=1, row=0)

        #separator musi mieć swój własny widget, tak chyba jest najwygodniej
        separetor_raw_string = '  -  '
        separator_tk_string = StringVar()
        separator_tk_string.set(separetor_raw_string)
        separator_label = Label(root, textvariable=separator_tk_string, font=label_font)
        separator_label.grid(column=3, row=0)

        #sekcja tworzenia widgetów dla gości
        goscie_name_string = '   Goście'
        goscie_name = StringVar()
        self.goscie_score_str = StringVar()
        self.goscie_score_int = 0
        goscie_name.set(goscie_name_string)
        self.goscie_score_str.set(str(self.goscie_score_int))

        goscie_name_label = Label(root, textvariable=goscie_name, font=label_font)
        goscie_score_label = Label(root, textvariable=self.goscie_score_str, font=label_font)

        goscie_score_label.grid(column=4, row=0)
        goscie_name_label.grid(column=5, row=0)

    def add_point_to_gospodarze(self):
        self.gospodarze_score_int += 1
        self.gospodarze_score_str.set(str(self.gospodarze_score_int))

    def add_point_to_goscie(self):
        self.goscie_score_int += 1
        self.goscie_score_str.set(str(self.goscie_score_int))

    def popup_window(self, message):
        #tworzy nowe okienko które nie wyświetla wiadomości bo nie
        popup = Tk()
        answer_string_tk = StringVar()
        answer_string_tk.set(message)
        answer_label = Label(popup, textvariable=answer_string_tk, font='times 40')
        answer_label.pack()
        popup.after(2000, lambda: popup.destroy())
        popup.mainloop()

    def check_if_cat(self):
        #losowanie czy kot czy nie, losowanie działa, string się tworzy ale nwm dlaczego nie wyświetla się w okienku
        random_number = randint(1, 1000)

        if random_number <= 666:
            answer_string_raw = 'To jest kot'
        else:
            answer_string_raw = 'To nie jest kot'
        print(answer_string_raw)

        self.popup_window(answer_string_raw)

    def on_keyboard_event(self, event):
        #hookmanager i jego eventy, te printy są dla debugowania, żeby wiedzieć jakie przyciski mają KeyId
        print('MessageName:', event.MessageName)
        print('Ascii:', repr(event.Ascii), repr(chr(event.Ascii)))
        print('Key:', repr(event.Key))
        print('KeyID:', repr(event.KeyID))
        print( 'ScanCode:', repr(event.ScanCode))
        print('---')

        try:
            # strzałka w lewo
            if event.KeyID == 37:
                self.add_point_to_gospodarze()
            #strzałka w prawo
            if event.KeyID == 39:
                self.add_point_to_goscie()
            #strzałka w górę
            if event.KeyID == 38:
                self.check_if_cat()
        finally:
            return True


root = Tk()
app = App(root)
root.mainloop()



