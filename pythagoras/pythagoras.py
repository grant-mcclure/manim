from manim import *

class Introduction(Scene):
    def construct(self):
        title = Text('Pythagoras Theorem')
        self.play(Write(title))
        self.wait(2)

        subtitle = Text('The required knowledge for SQA National 5', font_size=40).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait(2)

        self.play(FadeOut(subtitle,title))