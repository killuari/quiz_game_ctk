import customtkinter as ctk
from PIL import Image
from highscore import Highscore

class Menu():
    def __init__(self, app: ctk.CTk):
        self.__app = app
        self.__create_widgets()

    def __exit_game(self):
        self.__app.destroy()

    def __create_widgets(self):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1), weight=1)

        logo = ctk.CTkImage(Image.open("assets/logo.jpeg"), size=(1280, 720))
        background_label = ctk.CTkLabel(self.__app, text="", image=logo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.__welcome_frame = ctk.CTkFrame(self.__app)
        self.__main_frame = ctk.CTkFrame(self.__app)
        self.__welcome_frame.grid(row=0, sticky="S")
        self.__main_frame.grid(row=1, sticky="N")

        self.__welcome_label = ctk.CTkLabel(self.__welcome_frame, width=300, height=40)
        self.__welcome_label.grid(sticky="EW")

        self.__play_button = ctk.CTkButton(self.__main_frame, text="Play", width=280, height=56)
        self.__highscore_button = ctk.CTkButton(self.__main_frame, text="View Highscore", width=280, height=56)
        self.__exit_button = ctk.CTkButton(self.__main_frame, text="Exit Game", command=self.__exit_game, width=280, height=56)
        self.__play_button.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        self.__highscore_button.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)
        self.__exit_button.grid(column=0, row=2, sticky="NSEW", padx=10, pady=10)

    def set_welcome_label(self, name: str):
        self.__welcome_label.configure(text=f"Welcome {name}!")

    def deactivate(self):
        self.__welcome_frame.configure(state="disabled")
        self.__main_frame.configure(state="disabled")