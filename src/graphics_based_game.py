import customtkinter as ctk

class GraphicsBasedGame():
    def __init__(self):
        ctk.set_appearance_mode("Dark")
        self.__app = ctk.CTk()
        self.__app.title("Quiz King")

        # self.__create_widgets()

    def __create_widgets(self):
        # self.__name_entry = ctk.CTkEntry(self.__app, placeholder_text="Please enter your name.")
        # self.__name_entry.grid(column=0, row=0, sticky="nsew")
        pass

    def __get_player_name(self):
        dialog = ctk.CTkInputDialog(text="Please enter your name", title="Name")
        return dialog.get_input()  # waits for input

    def run(self):
        name = self.__get_player_name()
        self.__app.mainloop()