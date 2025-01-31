from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self. window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score:",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        tick = PhotoImage(file="images/true.png")
        cross = PhotoImage(file="images/false.png")

        self.tick_button = Button(image=tick,highlightthickness=0,command=self.true_pressed)
        self.cross_button = Button(image=cross, highlightthickness=0,command=self.false_pressed)
        self.tick_button.grid(row=2,column=0)
        self.cross_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Quiz finished!")
            #self.tick_button.destroy()
            #self.cross_button.destroy()
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
    def true_pressed(self):
        self.change_colour(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.change_colour(self.quiz.check_answer("False"))

    def change_colour(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
