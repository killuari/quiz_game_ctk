import customtkinter as ctk
from highscore import Highscore
from menu import Menu

class GraphicsBasedGame():
    def __init__(self):
        ctk.set_appearance_mode("Dark")

        self.__app = ctk.CTk()
        self.__app.title("Quiz King")
        self.__app.minsize(1280, 720)
        self.__app.resizable(False, False)

        self.__highscore = Highscore("assets/highscore.json")
        self.__menu = Menu(self.__app)

        # self.__create_widgets()

    def __create_widgets(self):
        # self.__name_entry = ctk.CTkEntry(self.__app, placeholder_text="Please enter your name.")
        # self.__name_entry.grid(column=0, row=0, sticky="nsew")
        pass

    def __get_player_name(self):
        dialog = ctk.CTkInputDialog(text="Please enter your name", title="Quiz King")
        return dialog.get_input()

    def run(self):
        name = self.__get_player_name()
        self.__menu.set_welcome_label(name)
        self.__app.mainloop()