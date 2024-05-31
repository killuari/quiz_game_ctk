import customtkinter as ctk
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory
from question import Question
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
        self.__app.maxsize(1280, 720)
        self.__app.resizable(False, False)

        # Init Questions and Highscore
        self.__questions_from_file = QuestionsFromJsonFileFactory("assets/questions_with_variying_answers.json")
        self.__questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")
        self.__highscore = Highscore("assets/highscore.json")

        # Connect to Server
        self.__connected_to_server = True
        try:
            num = self.__questions_from_server.get_total_number_of_questions()
        except Exception:
            self.__connected_to_server = False
        else:
            if num == 0:
                self.__connected_to_server = False

    def run(self):
        self.__get_player()
        self.__draw_menu()
        self.__app.mainloop()

    def __get_player(self):
        dialog = ctk.CTkInputDialog(text="Please enter your name", title="Quiz King")
        name = dialog.get_input()

        self.__player = Player(name)

    def __game_loop(self):
        current_question_idx = 0

        if not self.__player.lives().is_game_over():
            current_question = self.__get_question(current_question_idx)
            self.__draw_question(current_question)

            if current_question_idx >= self.__get_total_number_of_questions():
                current_question_idx = 0

        print(f"{self.__player.name()}, you have achieved {self.__player.score().get()} points!")

        self.__highscore.update(self.__player.score())

    #----QuestionFactory Functions----
    def __get_question(self, index: int) -> Question:
        if self.__connected_to_server:
            question_from_server = self.__questions_from_server.get_question(index)
            if not question_from_server is None:
                return question_from_server
        return self.__questions_from_file.get_question(index)

    def __get_total_number_of_questions(self) -> int:
        if self.__connected_to_server:
            if self.__questions_from_server.get_total_number_of_questions() != 0:
                return self.__questions_from_server.get_total_number_of_questions()
        return self.__questions_from_file.get_total_number_of_questions()

    #----Button Event Functions----
    def __on_play_button_pressed(self):
        self.__menu.destroy()

        self.__game_loop()

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

    def __on_right_answer(self):
        print("right!")

    def __on_wrong_answer(self):
        print("wrong!")

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

        font = ctk.CTkFont(family="Helvetica", size=40)

        highscore_title = ctk.CTkLabel(self.__highscore_frame, text="------ Highscores ------", font=font)
        highscore_title.grid(sticky="S")
        self.__highscore_label = ctk.CTkLabel(self.__highscore_frame, text=str(self.__highscore), font=font)
        self.__highscore_label.grid(sticky="N")

        self.__back_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Back", width=280, height=56, command=self.__on_highscore_back_button_pressed)
        self.__reset_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Reset", width=280, height=56, command=self.__on_highscore_reset_button_pressed)
        self.__back_button.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        self.__reset_button.grid(column=1, row=0, sticky="NSEW", padx=10, pady=10)

    def __draw_question(self, question: Question):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1, 2), weight=1)

        self.__stats_frame = ctk.CTkFrame(self.__app, width=1200)
        self.__question_frame = ctk.CTkFrame(self.__app, width=1200)
        self.__question_buttons_frame = ctk.CTkFrame(self.__app)
        self.__stats_frame.grid(row=0, sticky="N")
        self.__question_frame.grid(row=1, sticky="NS")
        self.__question_buttons_frame.grid(row=2)

        font_title = ctk.CTkFont(family="Helvetica", size=40)
        font_question = ctk.CTkFont(family="Helvetica", size=30)
        font_stats = ctk.CTkFont(family="Helvetica", size=35)

        score_label = ctk.CTkLabel(self.__stats_frame, text=f"Score: {self.__player.score().get()}", font=font_stats)
        lives_label = ctk.CTkLabel(self.__stats_frame, text=f"Lives: {self.__player.lives().get()}", font=font_stats)

        self.__stats_frame.grid_columnconfigure((0, 1), weight=1)
        score_label.pack(side="left", padx=250)
        lives_label.pack(side="right", padx=250)

        question_title = ctk.CTkLabel(self.__question_frame, text="----- Question -----", font=font_title)
        question_title.grid(sticky="S")
        question_text = ctk.CTkLabel(self.__question_frame, text=question.get_question_text(), font=font_question, wraplength=1200)
        question_text.grid(sticky="NS")
        question_answers = ctk.CTkLabel(self.__question_frame, text=str(question), font=font_question)
        question_answers.grid(sticky="N")

        for idx, option in enumerate(question.get_options()):
            button_command = self.__on_right_answer if question.get_answers()[idx].is_correct() else self.__on_wrong_answer
            button = ctk.CTkButton(self.__question_buttons_frame, text=option.upper(), width=280, height=56, command=button_command)
            button.grid(column=idx%4, row=int(idx/4), sticky="NSEW", padx=10, pady=10)