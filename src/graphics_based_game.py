import customtkinter as ctk
from highscore import Highscore
from menu import Menu
from player import Player

class GraphicsBasedGame():
    def __init__(self):
        # Init App
        ctk.set_appearance_mode("Dark")
        self.__app = ctk.CTk()
        self.__app.title("Quiz King")
        self.__app.minsize(1280, 720)
        self.__app.resizable(False, False)

        self.__highscore = Highscore("assets/highscore.json")

    def __get_player(self):
        dialog = ctk.CTkInputDialog(text="Please enter your name", title="Quiz King")
        name = dialog.get_input()

        self.__player = Player(name)
    
    #----Button Event Functions----
    def __on_play_button_pressed(self):
        self.__menu.destroy()

    def __on_highscore_button_pressed(self):
        self.__menu.destroy()
        self.__draw_highscores()

    def __on_highscore_back_button_pressed(self):
        self.__highscore_frame.destroy()
        self.__highscore_buttons_frame.destroy()
        
        self.__draw_menu()

    def __on_highscore_reset_button_pressed(self):
        self.__highscore_frame.destroy()
        self.__highscore_buttons_frame.destroy()

        self.__highscore.reset()
        self.__draw_highscores()

    #----Draw Functions----
    def __draw_menu(self):
        self.__menu = Menu(self.__app)
        self.__menu.set_welcome_label(self.__player.name())
        self.__menu.set_button_commands(self.__on_play_button_pressed, self.__on_highscore_button_pressed)

    def __draw_highscores(self):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1), weight=1)

        self.__highscore_frame = ctk.CTkFrame(self.__app, width=600, height=200)
        self.__highscore_buttons_frame = ctk.CTkFrame(self.__app)
        self.__highscore_frame.grid(row=0, sticky="S")
        self.__highscore_buttons_frame.grid(row=1)

        highscore_font = ctk.CTkFont(family="Helvetica", size=40)

        highscore_title = ctk.CTkLabel(self.__highscore_frame, text="------ Highscores ------", font=highscore_font)
        highscore_title.grid(sticky="S")
        self.__highscore_label = ctk.CTkLabel(self.__highscore_frame, text=str(self.__highscore), font=highscore_font)
        self.__highscore_label.grid(sticky="N")

        self.__back_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Back", width=280, height=56, command=self.__on_highscore_back_button_pressed)
        self.__reset_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Reset", width=280, height=56, command=self.__on_highscore_reset_button_pressed)
        self.__back_button.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        self.__reset_button.grid(column=1, row=0, sticky="NSEW", padx=10, pady=10)

    def run(self):
        self.__get_player()
        self.__draw_menu()
        self.__app.mainloop()