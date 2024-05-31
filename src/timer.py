import customtkinter as ctk

class QuestionTimer():
    def __init__(self, on_timer_timeout: callable, timer_label: ctk.CTkLabel, seconds: int = 30):
        self.__timer_label = timer_label
        self.__question_timer(seconds)
        self.__on_timer_timeout = on_timer_timeout

    def __question_timer(self, seconds: int = 30):
        self.__timer_label.configure(text=f"{seconds}s")
        if seconds > 0:
            if seconds <= 5:
                self.__timer_label.configure(text_color="red")
            seconds -= 1
            self.__timer_label.after(1000, self.__question_timer, seconds)
        else:
            self.__timer_label.configure(text_color="white")
            self.__on_timer_timeout()