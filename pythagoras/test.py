from manim import *

class Test(Scene):
    def construct(self):
        text = MathTex(r"\frac{a}{b}", font_size=72)
        self.play(Write(text))
        self.wait(2)
