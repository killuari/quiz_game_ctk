import customtkinter as ctk

class Difficulty():
    def __init__(self, app: ctk.CTk, on_dropdown_pressed: callable):
        self.__app = app
        self.__create_widgets()
        self.__difficulty_dropdown.configure(command=on_dropdown_pressed)

    def __create_widgets(self):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1), weight=1)

        self.__title_frame = ctk.CTkFrame(self.__app)
        self.__main_frame = ctk.CTkFrame(self.__app)
        self.__title_frame.grid(row=0, sticky="S")
        self.__main_frame.grid(row=1, sticky="N")

        font_title = ctk.CTkFont(family="Helvetica", size=40)
        font_dropdown = ctk.CTkFont(family="Helvetica", size=30)

        self.__difficulty_title = ctk.CTkLabel(self.__title_frame, text="----- Difficulty -----", font=font_title)
        self.__difficulty_title.grid(sticky="EW")

        self.__difficulty_dropdown = ctk.CTkOptionMenu(self.__main_frame, values=["Easy", "Medium", "Hard"], dropdown_font=font_dropdown)
        self.__difficulty_dropdown.grid(sticky="EW")

    def destroy(self):
        self.__title_frame.destroy()
        self.__main_frame.destroy()