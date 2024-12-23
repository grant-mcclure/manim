from manim import *
import math

class Introduction(Scene):
    def construct(self):
        # Title Animation
        title = Text("Statistics: Standard Deviation", font_size=60, color=BLUE)
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


class WordExplanationStandardDeviation(Scene):
    def construct(self):
        # Title
        title = Text("What is Standard Deviation?", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # First explanation line
        line1 = Text(
            "Standard Deviation is a measure of how spread out data is.",
            font_size=32,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(line1))
        self.wait(1)

        # Second explanation line
        line2 = Text(
            "It tells us how far data points are from the mean, on average.",
            font_size=32,
        ).next_to(line1, DOWN, buff=0.5)
        self.play(Write(line2))
        self.wait(1)

        # Third explanation line
        line3 = Text(
            "A small standard deviation means data is close to the mean.",
            font_size=32,
        ).next_to(line2, DOWN, buff=0.5)
        self.play(Write(line3))
        self.wait(1)

        # Fourth explanation line
        line4 = Text(
            "A large standard deviation means data is more spread out.",
            font_size=32,
        ).next_to(line3, DOWN, buff=0.5)
        self.play(Write(line4))
        self.wait(2)

        # Emphasis
        emphasis = Text(
            "Standard Deviation helps us understand how consistent data is!",
            font_size=36,
            color=YELLOW,
        ).to_edge(DOWN, buff=1)
        self.play(Write(emphasis))
        self.wait(3)

class StandardDeviation(Scene):
    def construct(self):
        axes = Axes(
            x_range= [-3,3],
            y_range = [0,.4, 0.1],
            x_length = 10,
            y_length= 4,
            axis_config={'color':WHITE},
            tips=False
        )
        title = Text('Visual Representation', font_size=50).to_edge(UL)
        self.play(Write(title))
        self.wait(2)


        lambda: axes.plot()
        self.add(axes)

        self.play(Create(axes))
        self.wait(4)

        ##formula gaussian distrubution
        def Gaussian_Distribution(x):
            return (1/(math.sqrt(2*PI))) *math.exp(-(x**2)/2)
        
        normal_curve = axes.plot(
            Gaussian_Distribution,
            x_range= [-3,3],
            color = BLUE
        )

        
        self.add(axes,normal_curve)
        self.play(Create(normal_curve))
        self.wait(4)

        x_axis_labels = axes.get_x_axis().add_labels(
            {
                -3: "-3 SD",
                -2: "-2 SD",
                -1: "-1 SD",
                0: "Mean",
                1: "1 SD",
                2: "2 SD",
                3: "3 SD",
            }
        )
        
        # Add and animate custom strings
        self.add(x_axis_labels)
        self.play(Create(x_axis_labels))
        self.wait(3)

        ##draw arrow to meet point
        mean = axes.c2p(0, 0)  # Mean at x = 0
        point_on_curve = axes.c2p(1, Gaussian_Distribution(1))  # Curve point at x = 1
        arrow = Arrow(mean, point_on_curve, buff=0, color=YELLOW)
        self.play(Create(arrow))
        self.wait(1)

        # Add a label for the arrow
        label = Text("Deviation", font_size=24).next_to(arrow, RIGHT +1)
        self.play(Write(label))
        self.wait(3)

        explanation = Text('The further away the data points are from the mean, the greater the standard deviation', font_size=20).next_to(axes, DOWN*3)
        self.play(Write(explanation))
        self.wait(4)

class NumericalExample(Scene):
    def construct(self):
        title = Text("Standard Deviation Question", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Split the question into multiple lines and center it
        question = VGroup(
            Text("Grant takes part in a dance show, and he gains scores from the judges.", font_size=25),
            Text("What is the Standard Deviation of the data?", font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, center=True).next_to(title, DOWN)

        self.play(Write(question))
        self.wait(3)

        # Display the scores
        question_numbers = MathTex("5", ",", "6", ",", "8", ",", "10", ",", "7", ",", "5").scale(1.2)
        question_numbers.next_to(question, DOWN, buff=0.5)

        self.play(Write(question_numbers))
        self.wait(2)

        self.play(FadeOut(question))
        self.wait(2)
       
        question_numbers.generate_target()
        question_numbers.target.to_edge(UL*2)
       
        self.play(FadeOut(title))

        self.play(MoveToTarget(question_numbers))
        self.wait(3)

        
        ##step 1 find the means
        mean_equation_1 = MathTex(
            r"\text{Mean} = \frac{\text{Sum of All Numbers}}{\text{Number of Data Points}}",
            font_size=36
        )
        self.play(Write(mean_equation_1))
        self.wait(2)

        mean_equation_1.generate_target()
        mean_equation_1.target.next_to(question_numbers, DOWN*1)
        self.play(MoveToTarget(mean_equation_1))
        self.wait(2)

        mean_equation_2 = MathTex(
            r"\text{Mean} = \frac{5+6+8+10+7+5}{6}",
            font_size=36
        )
        mean_equation_2.generate_target()
        mean_equation_2.target.next_to(mean_equation_1, DOWN*1)
        self.play(Write(mean_equation_2))
        self.play(MoveToTarget(mean_equation_2))
        self.wait(2)

        mean_equation_3 = MathTex(
            r"\text{Mean} = 7",
            font_size=36
        )

        mean_equation_3.generate_target()
        mean_equation_3.target.next_to(mean_equation_2, DOWN*2)
        self.play(Write(mean_equation_3))
        self.play(MoveToTarget(mean_equation_3))
        self.wait(2)

        mean_equation_4 = MathTex(
            r"\bar{x} = 7",
            font_size=36, color = YELLOW
        ).scale(1.2)

        mean_equation_4.generate_target()
        mean_equation_4.target.next_to(mean_equation_3, DOWN*2)
        self.play(Write(mean_equation_4))
        self.play(MoveToTarget(mean_equation_4))
        self.wait(2)

        #fadeout all other info
        self.play(FadeOut(mean_equation_1,mean_equation_2,mean_equation_3))

        ##move x bar next to numbers
        mean_equation_4.target.next_to(question_numbers, RIGHT*2)
        self.play(MoveToTarget(mean_equation_4))
        self.wait(2)

        x_position = [-5,1.8,0]


        ##draw lines on the table
        horizontal_line_1 = [-6,1.4,0]
        horizontal_line_2 = [4,1.4,0]

        vertical_line_1 = [-4, 2,0]
        vertical_line_1_end = [-4, -4,0]

        vertical_line_2 = [1, 2,0]
        vertical_line_2_end = [1, -4,0]

        self.play(Create(Line(horizontal_line_1,horizontal_line_2, color = RED)))
        self.play(Create(Line(vertical_line_1,vertical_line_1_end, color = RED)))
        self.play(Create(Line(vertical_line_2,vertical_line_2_end, color = RED)))


         # Write x
        x = MathTex("x").move_to(x_position)
        self.play(Write(x))

        # Arrange question numbers vertically below x
        question_numbers = VGroup(
            *[MathTex(num) for num in ["5", "6", "8", "10", "7", "5"]]
        ).arrange(DOWN, buff=0.6).next_to(x, DOWN, buff=0.5)
        self.play(Write(question_numbers))
        self.wait(2)

        # Write x - x̄ column header
        x_bar = MathTex(r"x - \bar{x}").next_to(x, RIGHT, buff=2)
        self.play(Write(x_bar))
        self.wait(1)

        # Add calculations aligned with each value in the x column
        x_minusxbar_values = [
            MathTex("5 - 7 = \mathbf{-2}"),
            MathTex("6 - 7 = \mathbf{-1}"),
            MathTex("8 - 7 = \mathbf{1}"),
            MathTex("10 - 7 = \mathbf{3}"),
            MathTex("7 - 7 = \mathbf{0}"),
            MathTex("5 - 7 = \mathbf{-2}"),
        ]

        # Ensure alignment for all rows
        for equation, value in zip(x_minusxbar_values, question_numbers):
            equation.next_to(value, RIGHT, buff=2)  # Align with corresponding value

        x_minusxbar_group = VGroup(*x_minusxbar_values)
        self.play(Write(x_minusxbar_group))
        self.wait(2)

        # Add a new column header
        new_column_header = MathTex(r"(x - \bar{x})^2").next_to(x_bar, RIGHT, buff=3)
        self.play(Write(new_column_header))
        self.wait(1)

        # Add calculations aligned with each value in the x column
        x_x_barsq = [
            MathTex("(-2)^2 = \mathbf{4}"),
            MathTex("(-1)^2 = \mathbf{1}"),
            MathTex("(1)^2 = \mathbf{1}"),
            MathTex("(3)^2 = \mathbf{9}"),
            MathTex("(0)^2 = \mathbf{0}"),
            MathTex("(-2)^2 = \mathbf{4}"),
        ]

        # Ensure alignment for all rows in the new column
        for equation, value in zip(x_x_barsq, question_numbers):
            equation.next_to(value, RIGHT, buff=6)  # Align with corresponding value

        new_column_group = VGroup(*x_x_barsq)
        self.play(Write(new_column_group))
        self.wait(10)

        sum_x_xbar_sq = MathTex(r'\sum (x - \bar{x})^2', font_size = 30, color = YELLOW).to_edge(RIGHT).shift(LEFT*0.5)
        self.play(Write(sum_x_xbar_sq))
        self.wait

        sum_x_xbar_sq2 = MathTex(r'= 4+1+1+9+0+4', font_size = 30, color = YELLOW).next_to(sum_x_xbar_sq, DOWN*2)
        self.play(Write(sum_x_xbar_sq2))
        self.wait(1)

        sum_x_xbar_sq3 = MathTex(r'= \mathbf{19}', font_size = 40, color = YELLOW).next_to(sum_x_xbar_sq2, DOWN*2)
        self.play(Write(sum_x_xbar_sq3))
        self.wait(1)

        sum_x_xbar_sq.generate_target()
        sum_x_xbar_sq.target.next_to(mean_equation_4, RIGHT*2)

        

        self.play(MoveToTarget(sum_x_xbar_sq))
        self.wait(1)
        sum_x_xbar_sq3.generate_target()
        sum_x_xbar_sq3.target.next_to(sum_x_xbar_sq, RIGHT)

        self.play(MoveToTarget(sum_x_xbar_sq3))
        self.wait(2)

        self.clear()
        self.wait()

        #do the formula
        std1 = MathTex(r"\text{Standard Deviation} = \sqrt{\frac{\sum (x-\bar{x})^2}{n-1}}", color = RED).to_edge(UP)
        self.play(Write(std1))
        self.wait(4)

        explanation = MathTex(r'\text{Where} \sum (x-\bar{x})^2 = 19, n = 6', color = YELLOW).next_to(std1, DOWN*2)
        self.play(Write(explanation))
        self.wait(4)

        std2 = MathTex(r"\text{StDev} = \sqrt{\frac{19}{6-1}}").next_to(explanation, DOWN*2)
        self.play(Write(std2))
        self.wait(2)

        std3 = MathTex(r"\mathbf{\text{StDev} = 3.8}",).next_to(std2, DOWN *2)
        self.play(Write(std3))
        self.wait(4)

class Summary(Scene):
    def construct(self):
        # Title
        title = Text("Summary of Standard Deviation", font_size=50, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Key Points Summary
        points = VGroup(
            Text("1. Standard Deviation measures the spread of data.", font_size=30),
            Text("2. It shows how far values deviate from the mean.", font_size=30),
            Text("3. Smaller values mean data is closer to the mean.", font_size=30),
            Text("4. Larger values mean data is more spread out.", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(points, shift=UP, lag_ratio=1))
        self.wait(2)


         #do the formula
        std1 = MathTex(r"\text{Standard Deviation} = \sqrt{\frac{\sum (x-\bar{x})^2}{n-1}}", color = YELLOW).next_to(points, DOWN*2)
        self.play(Write(std1))
        self.wait(4)


        # Emphasis Statement
        emphasis = Text(
            "Standard Deviation helps analyse data consistency!",
            font_size=30, color=ORANGE
        ).to_edge(DOWN, buff=1)
        self.play(Write(emphasis))
        self.wait(3)




        

