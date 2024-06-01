import customtkinter as ctk

class Difficulty():
    def __init__(self, app: ctk.CTk, on_difficulty_selected: callable):
        self.__app = app
        self.__difficulty : str = "Medium"
        self.__create_widgets()
        self.__on_difficulty_selected: callable = on_difficulty_selected

    def __on_dropdown_pressed(self, difficulty: str):
        self.__difficulty = difficulty

    def __on_start_button_pressed(self):
        self.__destroy()
        self.__on_difficulty_selected(self.__difficulty)

    def __create_widgets(self):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure(0, weight=1)

        self.__main_frame = ctk.CTkFrame(self.__app)
        self.__main_frame.pack(pady=200)

        font_title = ctk.CTkFont(family="Helvetica", size=40)
        font_dropdown = ctk.CTkFont(family="Helvetica", size=30)
        font_text = ctk.CTkFont(family="Helvetica", size=25)

        self.__difficulty_title = ctk.CTkLabel(self.__main_frame, text="----- Difficulty -----", font=font_title)
        self.__difficulty_title.grid(row=0, sticky="EW")
        difficulty_text = ctk.CTkLabel(self.__main_frame, text="Select difficulty for your questions", font=font_text)
        difficulty_text.grid(row=1, sticky="EW", pady=10)

        self.__difficulty_dropdown = ctk.CTkOptionMenu(self.__main_frame, values=["Easy", "Medium", "Hard"], dropdown_font=font_text, font=font_dropdown, command=self.__on_dropdown_pressed)
        self.__difficulty_dropdown.grid(pady=15)
        self.__difficulty_dropdown.set("Medium")
        start_button = ctk.CTkButton(self.__main_frame, text="Start Game", font=font_title, command=self.__on_start_button_pressed)
        start_button.grid(sticky="EW", pady=20, padx=10)

    def __destroy(self):
        self.__main_frame.destroy()