import customtkinter as ctk
from PIL import Image

class Menu():
    def __init__(self, app: ctk.CTk):
        self.__app = app
        self.__create_widgets()

    def __exit_game(self):
        self.__app.destroy()

    def __create_widgets(self):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure(0, weight=1)

        logo = ctk.CTkImage(Image.open("assets/logo.jpeg"), size=(1280, 720))
        self.__background_label = ctk.CTkLabel(self.__app, text="", image=logo)
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.__main_frame = ctk.CTkFrame(self.__app)
        self.__main_frame.pack(pady=200)

        font = ctk.CTkFont(family="Helvetica", size=25)
        font_button = ctk.CTkFont(family="Helvetica", size=35)

        self.__welcome_label = ctk.CTkLabel(self.__main_frame, font=font, pady=10)
        self.__welcome_label.grid(row=0, sticky="EW")

        self.__play_button = ctk.CTkButton(self.__main_frame, text="Play", width=280, height=56, font=font_button)
        self.__highscore_button = ctk.CTkButton(self.__main_frame, text="View Highscore", width=280, height=56, font=font_button)
        self.__exit_button = ctk.CTkButton(self.__main_frame, text="Exit Game", command=self.__exit_game, width=280, height=56, font=font_button)
        self.__play_button.grid(column=0, row=1, sticky="NSEW", padx=15, pady=15)
        self.__highscore_button.grid(column=0, row=2, sticky="NSEW", padx=15, pady=7)
        self.__exit_button.grid(column=0, row=3, sticky="NSEW", padx=15, pady=15)

    def set_welcome_label(self, name: str):
        self.__welcome_label.configure(text=f"Welcome {name}!")

    def set_button_commands(self, on_play: callable, on_highscore: callable):
        self.__play_button.configure(command=on_play)
        self.__highscore_button.configure(command=on_highscore)

    def destroy(self):
        self.__main_frame.destroy()
        self.__background_label.destroy()