import customtkinter as ctk
from PIL import Image

class Menu():
    def __init__(self, app: ctk.CTk):
        self.__create_widgets(app)

    def __play(self):
        print("play")

    def __view_highscore(self):
        print("highscore")

    def __exit_game(self):
        print("exit game")

    def __create_widgets(self, app: ctk.CTk):
        app.grid_columnconfigure(0, weight=1)
        app.grid_rowconfigure((0, 1), weight=1)

        logo = ctk.CTkImage(Image.open("assets/logo.jpeg"), size=(1280, 720))
        background_label = ctk.CTkLabel(app, text="", image=logo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.__welcome_frame = ctk.CTkFrame(app)
        self.__main_frame = ctk.CTkFrame(app)

        self.__welcome_frame.grid(row=0, sticky="S")
        self.__main_frame.grid(row=1, sticky="N")

        self.__welcome_label = ctk.CTkLabel(self.__welcome_frame, width=300, height=40)
        self.__welcome_label.grid(sticky="EW")

        self.__play_button = ctk.CTkButton(self.__main_frame, text="Play", command=self.__play, width=280, height=56)
        self.__highscore_button = ctk.CTkButton(self.__main_frame, text="View Highscore", command=self.__view_highscore, width=280, height=56)
        self.__exit_button = ctk.CTkButton(self.__main_frame, text="Exit Game", command=self.__exit_game, width=280, height=56)

        self.__play_button.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        self.__highscore_button.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)
        self.__exit_button.grid(column=0, row=2, sticky="NSEW", padx=10, pady=10)

    def set_welcome_label(self, name: str):
        self.__welcome_label.configure(text=f"Welcome {name}!")