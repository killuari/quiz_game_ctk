import customtkinter as ctk
from questions_from_json_file_factory import QuestionsFromJsonFileFactory
from questions_from_server_factory import QuestionsFromServerFactory
from question import Question
from highscore import Highscore
from menu import Menu
from player import Player
from timer import QuestionTimer
from difficulty import Difficulty
from report_question import ReportQuestion

class GraphicsBasedGame():
    def __init__(self):
        # Init App
        ctk.set_appearance_mode("Dark")
        self.__app = ctk.CTk()
        self.__app.title("Quiz King")
        self.__app.minsize(1280, 720)
        self.__app.maxsize(1400, 720)
        self.__app.resizable(False, False)

        # Init Questions and Highscore
        self.__questions_from_file = QuestionsFromJsonFileFactory("assets/questions_final.json")
        self.__questions_from_server = QuestionsFromServerFactory("http://127.0.0.1:5000", "abcd1234")
        self.__highscore = Highscore("assets/highscore.json")
        self.__report = ReportQuestion("http://127.0.0.1:5000", "abcd1234")
        self.__current_question_idx = 0
        self.__difficulty: int = None

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

    def __next_question(self):
        current_question = self.__get_question(self.__current_question_idx, self.__difficulty)
        if current_question is None:
            self.__on_end_button_pressed()
        else:
            self.__draw_question(current_question)
            QuestionTimer(self.__on_wrong_answer, self.__timer_label)

    #----QuestionFactory Functions----
    def __get_question(self, index: int, difficulty: int) -> Question:
        if self.__connected_to_server:
            question_from_server = self.__questions_from_server.get_question(index, difficulty)
            if not question_from_server is None:
                return question_from_server
        return self.__questions_from_file.get_question(index, difficulty)

    #----Button Event Functions----
    def __on_difficulty_selected(self, difficulty: str):
        difficulties = ["Easy", "Medium", "Hard"]
        self.__difficulty = difficulties.index(difficulty) + 1

        # Shuffle Questions
        self.__questions_from_file.reload_questions()
        self.__questions_from_server.reload_questions()

        self.__next_question()

    def __on_play_button_pressed(self):
        self.__menu.destroy()
        self.__player.reset()
        self.__current_question_idx = 0

        Difficulty(self.__app, self.__on_difficulty_selected, self.__draw_menu)

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
        match self.__difficulty:
            case 1: self.__player.score().add(20)
            case 2: self.__player.score().add(50)
            case 3: self.__player.score().add(100)

        self.__stats_frame.destroy()
        self.__question_frame.destroy()
        self.__question_buttons_frame.destroy()

        self.__current_question_idx += 1

        self.__next_question()

    def __on_wrong_answer(self):
        self.__player.lives().loose_a_life()

        self.__stats_frame.destroy()
        self.__question_frame.destroy()
        self.__question_buttons_frame.destroy()

        if self.__player.lives().is_game_over():
            self.__highscore.update(self.__player)
            self.__draw_highscores(new_score=self.__player.score().get())
        else:
            self.__next_question()

    def __on_end_button_pressed(self):
        self.__stats_frame.destroy()
        self.__question_frame.destroy()
        self.__question_buttons_frame.destroy()

        self.__highscore.update(self.__player)
        self.__draw_highscores(new_score=self.__player.score().get())

    #----Draw Functions----
    def __draw_menu(self):
        self.__menu = Menu(self.__app)
        self.__menu.set_welcome_label(self.__player.name())
        self.__menu.set_button_commands(self.__on_play_button_pressed, self.__on_highscore_button_pressed)

    def __draw_highscores(self, new_score: int = None):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1), weight=1)

        self.__highscore_frame = ctk.CTkFrame(self.__app, width=600, height=200)
        self.__highscore_buttons_frame = ctk.CTkFrame(self.__app)
        self.__highscore_frame.grid(row=0, sticky="S")
        self.__highscore_buttons_frame.grid(row=1)

        font = ctk.CTkFont(family="Helvetica", size=40)
        font_button = ctk.CTkFont(family="Helvetica", size=35)

        highscore_title = ctk.CTkLabel(self.__highscore_frame, text="", font=font)
        if new_score is not None:
            highscore_title.configure(text=f"You achieved {new_score} points!\n\n------ Highscores ------")
        else:
            highscore_title.configure(text=f"------ Highscores ------")
        highscore_title.grid(sticky="S")
        highscore_label = ctk.CTkLabel(self.__highscore_frame, text=str(self.__highscore), font=font)
        highscore_label.grid(sticky="N")

        back_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Back", width=280, height=56, font=font_button, command=self.__on_highscore_back_button_pressed)
        reset_button = ctk.CTkButton(self.__highscore_buttons_frame, text="Reset", width=280, height=56, font=font_button, command=self.__on_highscore_reset_button_pressed)
        back_button.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        reset_button.grid(column=1, row=0, sticky="NSEW", padx=10, pady=10)

    def __draw_question(self, question: Question):
        self.__app.grid_columnconfigure(0, weight=1)
        self.__app.grid_rowconfigure((0, 1, 2), weight=1)

        self.__stats_frame = ctk.CTkFrame(self.__app, width=1200)
        self.__question_frame = ctk.CTkFrame(self.__app, width=1200)
        self.__question_buttons_frame = ctk.CTkFrame(self.__app, width=1200)
        self.__stats_frame.grid(row=0, sticky="N")
        self.__question_frame.grid(row=1, sticky="NS")
        self.__question_buttons_frame.grid(row=2, sticky="S")

        self.__question_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.__answer_buttons_frame = ctk.CTkFrame(self.__question_frame)
        self.__answer_buttons_frame.grid(row=3, sticky="N", pady=15)

        font_title = ctk.CTkFont(family="Helvetica", size=40)
        font_question = ctk.CTkFont(family="Helvetica", size=30)
        font_stats = ctk.CTkFont(family="Helvetica", size=35)

        score_label = ctk.CTkLabel(self.__stats_frame, text=f"Score: {self.__player.score().get()}", font=font_stats, width=200)
        lives_label = ctk.CTkLabel(self.__stats_frame, text=f"Lives: {self.__player.lives().get()}", font=font_stats, width=200)
        self.__timer_label = ctk.CTkLabel(self.__stats_frame, text="", font=font_stats)

        self.__stats_frame.grid_columnconfigure((0, 1, 2), weight=1)
        score_label.grid(column=0, row=0, sticky="W", padx=10, pady=15)
        self.__timer_label.grid(column=1, row=0, sticky="EW", padx=200, pady=15)
        lives_label.grid(column=2, row=0, sticky="E", padx=10, pady=15)

        question_title = ctk.CTkLabel(self.__question_frame, text="----- Question -----", font=font_title)
        question_title.grid(row=0, sticky="N", pady=5)
        question_text = ctk.CTkLabel(self.__question_frame, text=question.get_question_text(), font=font_question, wraplength=1200)
        question_text.grid(row=1, sticky="N", padx=10, pady=5)
        if not question.get_image() is None:
            image_size = (800, 300) if len(question.get_answers()) <= 4 else (800, 250)
            image = ctk.CTkImage(question.get_image(), size=image_size)
            question_image = ctk.CTkLabel(self.__question_frame, text="", image=image, pady=15, padx=10)
            question_image.grid(row=2, sticky="N")

        for idx, answer in enumerate(question.get_answers()):
            button_command = self.__on_right_answer if question.get_answers()[idx].is_correct() else self.__on_wrong_answer
            # button_text = "".join([f"{char}\n" if idx%35==0 and idx!=0 else char for idx, char in enumerate(str(answer))])    (should wrap the length of the text on the button)
            button = ctk.CTkButton(self.__answer_buttons_frame, text=f"{question.get_options()[idx]}) {str(answer)}", width=270, height=50, font=font_question, command=button_command)
            button._text_label.configure(wraplength=400) # but this way is easier
            button.grid(column=idx%2, row=int(idx/2), sticky="NSEW", padx=10, pady=10)

        self.__question_buttons_frame.grid_columnconfigure((0, 1), weight=1)
        stop_button = button = ctk.CTkButton(self.__question_buttons_frame, text=f"End Game", width=370, height=40, font=font_question, command=self.__on_end_button_pressed, fg_color="#623838", hover_color="#432626")
        if self.__connected_to_server:
            report_button = ctk.CTkButton(self.__question_buttons_frame, command=lambda: self.__report.on_question_report(question), text=f"Report incorrect question", width=370, height=40, font=font_question, fg_color="#7E2626", hover_color="#571B1B")
        else:
            report_button = ctk.CTkButton(self.__question_buttons_frame, text=f"Not connected to Server", width=370, height=40, font=font_question, fg_color="#7E2626", hover_color="#571B1B")
        stop_button.grid(column=0, row=0, sticky="E", padx=25, pady=10)
        report_button.grid(column=1, row=0, sticky="W", padx=25, pady=10)