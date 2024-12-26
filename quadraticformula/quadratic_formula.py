from manim import *
import math

class Introduction(Scene):
    def construct(self):
        # Title Animation
        title = Text("The Quadratic Formula", font_size=60, color=BLUE)
        underline = Line(LEFT, RIGHT, color=BLUE).scale(2).next_to(title, DOWN, buff=0.2)
        self.play(Write(title))
        self.play(GrowFromCenter(underline))
        self.wait(1)

        # Subtitle Animation
        subtitle = Text(
            "The required theory for National 5 Mathematics",
            font_size=30,
            color=WHITE
        ).next_to(underline, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)

        name = Text('Made by Grant McClure', font_size=30).next_to(subtitle, DOWN*2)

        self.play(Write(name))

        # Fade Out Everything
        self.play(FadeOut(title, underline, subtitle,name))

class Explanation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3,3,1],
            y_range= [-2,2,1],
            x_length=6,
            y_length=10,
        )

        title = Text('Visual Representation', font_size=50).to_edge(UL)
        self.play(Write(title))
        self.wait(2)

        lambda: axes.plot()
        self.add(axes)
        self.play(Create(axes))

        self.play(FadeOut(title))

        def trinomial(x):
            return x**2 - (1)
        
        trinomial_plot = axes.plot(
            trinomial,
            x_range=[-3,3],
            color = BLUE
        )
        self.add(trinomial_plot)
        self.play(Create(trinomial_plot))
        self.wait(2)

        root1 = axes.c2p(-1,0)
        root2 = axes.c2p(1,0)

        dot1 = Dot(point=root1, color=RED )
        dot2 = Dot(point=root2, color=YELLOW)

        self.play(Create(dot1))
        self.play(Create(dot2))
        self.wait(5)

        label1 = MathTex(r'x_1', color = RED).next_to(dot1, LEFT *1.5).shift(DOWN*0.5).scale(1.2)
        label2 = MathTex(r'x_2', color = YELLOW).next_to(dot2, RIGHT *1.5).shift(DOWN*0.5).scale(1.2)

        self.play(Create(label1))
        self.wait(2)
        self.play(Create(label2))
        self.wait(1)




class QuadraticFormula(Scene):
    def construct(self):
        # Write the question
        question = VGroup(
            MathTex(r"\text{What are the roots of the function:}", font_size=30),
            MathTex(r"2x^2 + 3x - 4", font_size=36),
            MathTex(r"\text{Give your answer to two decimal places.}", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)

        # Define the quadratic formula
        formula1 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color=YELLOW).next_to(question, DOWN, buff=0.5)

        # Display the question
        self.play(Write(question))
        self.wait(9)

        # Display the formula
        self.play(Create(formula1))
        self.wait(5)

        # Display coefficients
        coefficients = VGroup(
            MathTex(r'a = 2'),
            MathTex(r'b = 3'),
            MathTex(r'c = -4'),
        ).arrange(DOWN, aligned_edge=RIGHT).to_corner(UR)

        self.play(Write(coefficients))
        self.wait(4)

        # Create the next formula line of working
        formula2 = MathTex(r"x = \frac{-3 \pm \sqrt{3^2 - (4 \cdot 2 \cdot (-4))}}{2 \cdot 2}", color=YELLOW).next_to(formula1, DOWN, buff=0.5)

        # Transform formula1 into the updated formula2
        self.play(Transform(formula1, formula2))
        self.wait(3)

        # Fade out the question
        self.play(FadeOut(question))
        self.wait(1)

        # Move formula1 (now showing formula2) to the top of the page
        formula1.generate_target()
        formula1.target.to_edge(UP)
        self.play(MoveToTarget(formula1))
        self.wait(2)

        # Add the next line of working below the updated formula
        formula3 = MathTex(r"x = \frac{-3 \pm \sqrt{9 - (-32)}}{4}", color=YELLOW).next_to(formula1, DOWN, buff=0.5)
        self.play(Write(formula3))
        self.wait(6)

        formula4 = MathTex(r"x = \frac{-3 \pm \sqrt{41}}{4}", color=YELLOW).next_to(formula3, DOWN, buff=0.5)
        self.play(Write(formula4))
        self.wait(5)

        formula5 = MathTex(r"x_1 = \frac{-3 + \sqrt{41}}{4}, \ \ \ \ \  x_2 =  \frac{-3 - \sqrt{41}}{4}", color=YELLOW).next_to(formula4, DOWN, buff=0.5)
        self.play(Write(formula5))
        self.wait(3)


        formula6 = MathTex(r"x_1 = 0.85, \, x_2 = -2.35", color=RED).next_to(formula5, DOWN, buff=0.5)
        self.play(Create(formula6))
        self.wait(8)

        

