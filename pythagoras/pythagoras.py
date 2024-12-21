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

class InitialExplanation(Scene):
    def construct(self):
        
        point_a = [-2, 0, 0]
        point_b = [3,0,0]
        point_c = [3,2,0]

        square_size = 0.5  # Size of the square outline
        square = Polygon(
            [3, 0, 0], [3 - square_size, 0, 0],
            [3 - square_size, square_size, 0], [3, square_size, 0],
            color=WHITE
        )

        base = Line(point_a, point_b, color = RED)
        height = Line(point_a, point_c, color = BLUE)
        hypotenuse = Line(point_b, point_c, color = GREEN)

        base_label = Text('a', font_size=30, color=RED_B).next_to(base, DOWN)
        height_label = Text('b', font_size=30, color=GREEN_B).next_to(height, RIGHT)
        hypotenuse_label = Text('c', font_size=30, color=BLUE_B).move_to(height.get_center() + UP*0.4)


        info_1 = Text('The Relationship between each of these lines can be represented by:', font_size=20).next_to(base, DOWN*3)
        theorem = Text('c^2 = a^2 + b^2', font_size=20).next_to(info_1, DOWN)
        info_2 = Text('Where a and b represent short sides', font_size=20).next_to(theorem, DOWN)
        info_3 = Text('c represents the longest side (Hypotenuse)', font_size=20).next_to(info_2, DOWN)


        self.play(Create(base), Write(base_label))
        self.wait(2)
        self.play(Create(height), Write(hypotenuse_label))
        self.wait(2)
        self.play(Create(hypotenuse), Write(height_label))
        self.play(Create(square))
        self.wait(1)
        self.play(Write(info_1))
        self.wait(1)
        self.play(Write(theorem))
        self.wait(1)
        self.play(Write(info_2))
        self.wait(1)
        self.play(Write(info_3))




        