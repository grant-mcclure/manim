from manim import *


class Introduction(Scene):
    def construct(self):
        # Title Animation
        title = Text("Pythagoras' Theorem", font_size=60, color=BLUE)
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


class InitialExplanation(Scene):
    def construct(self):
        
        title = Text('Underlying Theory of Pythagoras theorem', font_size=40).to_corner(UL)
        self.play(Write(title))

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
        theorem = MathTex(r"c^2 = a^2 + b^2", font_size=40).next_to(info_1, DOWN)
        info_2 = Text('Where a and b represent short sides', font_size=20).next_to(theorem, DOWN)
        info_3 = Text('c, represents the longest side (Hypotenuse)', font_size=20).next_to(info_2, DOWN)


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
        self.wait(5)

        self.clear()
        self.wait(2)

class FirstExample(Scene):
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

        base_number = MathTex(r"3", font_size=40).move_to(base_label.get_center())
        height_number = MathTex(r"4", font_size=40).move_to(height_label.get_center())

        title = Text('Solving for the Hypotenuse', font_size=50).to_corner(UL)
        #place the info down
        info1 = Text('Lets solve the the Hypotenuse, using the formula from before', font_size=20).next_to(base, DOWN*3)
        theorem = MathTex(r"c^2 = a^2 + b^2", font_size=30).next_to(info1, DOWN)
        theorem_num = MathTex(r"c^2 = 3^2 + 4^2", font_size=30).next_to(theorem, DOWN)
        theorem_num3 = MathTex(r"c^2 = 25", font_size=30).next_to(theorem_num, DOWN)
        theorem_num4 = MathTex(r"c = \sqrt{25}", font_size=30).next_to(theorem_num3, DOWN)
        theorem_num5 = MathTex(r"c = 5", font_size=30).next_to(theorem_num4, DOWN)

        self.play(Create(title))
        
        self.play(Create(base), Write(base_label))
        self.wait(0)
        self.play(Create(height), Write(hypotenuse_label))
        self.wait(0)
        self.play(Create(hypotenuse), Write(height_label))
        self.play(Create(square))
        self.wait(4)

        self.play(FadeTransformPieces(base_label, base_number))
        self.wait(1)
        self.play(FadeTransformPieces(height_label, height_number))
        self.wait(5)
        
        #write information
        self.play(Create(info1))
        self.wait(2)
        self.play(Create(theorem))
        self.wait(2)
        self.play(Create(theorem_num))
        self.wait(2)
        self.play(Create(theorem_num3))
        self.wait(2)
        self.play(Create(theorem_num4))
        self.wait(2)
        self.play(Create(theorem_num5))
        self.wait(2)

class SecondExample(Scene):
    def construct(self):

        point_a = [-2, 1, 0]
        point_b = [3,1,0]
        point_c = [3,3,0]

        base = Line(point_a, point_b, color = RED)
        height = Line(point_a, point_c, color = BLUE)
        hypotenuse = Line(point_b, point_c, color = GREEN)

        base_label = Text('a', font_size=30, color=RED_B).next_to(base, DOWN)
        height_label = Text('b', font_size=30, color=GREEN_B).next_to(height, RIGHT)
        hypotenuse_label = Text('c', font_size=30, color=BLUE_B).move_to(height.get_center() + UP*0.4)

        base_number = MathTex(r"3", font_size=40).move_to(base_label.get_center())
        height_number = MathTex(r"4", font_size=40).move_to(height_label.get_center())

        title = Text('Solving for the a short side', font_size=50).to_corner(UL)

        theorem = MathTex("c^2", "=", "a^2", "+", "b^2", font_size=40).next_to(base,DOWN*3)
        theorem_rearranged = MathTex("c^2", "-" ,"a^2" ,"=", "b^2", font_size=40).next_to(theorem, DOWN)
        theorem_rearranged_2 = MathTex(r"b^2 = c^2 - a^2",font_size=40).next_to(theorem_rearranged, DOWN)

        self.play(Create(title))
        #draw triangle
        self.play(Create(base), Write(base_label))
        self.wait(0)
        self.play(Create(height), Write(hypotenuse_label))
        self.wait(0)
        self.play(Create(hypotenuse), Write(height_label))

        #maths
        self.wait(1)
        self.play(Create(theorem))

        a_squared = theorem[2]
        a_squared.generate_target()
        a_squared.target.move_to(theorem_rearranged[2].get_center())
        minus_a_squared = MathTex("- a^2", font_size=40).move_to(theorem[4].get_center())

        # Animate rearranging
        self.play(
            MoveToTarget(a_squared)
        )

        # Transform to the rearranged equation and clean up
        self.play(Transform(theorem, theorem_rearranged))
        self.wait(1)

        self.play(Transform(theorem_rearranged, theorem_rearranged_2))
        self.wait(1)

        self.play(FadeOut(theorem, run_time = 1))
        
        ##move the theorem rearraged up
        self.play(theorem_rearranged_2.animate.next_to(base, DOWN*3))
        self.play(FadeOut(theorem_rearranged, run_time = 0.5))
        self.wait(1)

        ##animate numbers into triangle
        hypotenuse_number = MathTex(r"5", font_size=40).move_to(hypotenuse_label.get_center())

        base_number = MathTex(r"3", font_size=40).move_to(base_label.get_center())

        self.play(FadeTransformPieces(hypotenuse_label, hypotenuse_number))
        self.wait(1)
        self.play(FadeTransformPieces(base_label, base_number))
        self.wait(1)



        new_theorem_1 = MathTex("b^2 = 5^2 - 3^2", font_size = 40).next_to(theorem_rearranged_2, DOWN)
        self.play(Write(new_theorem_1))
        self.wait(2)

        new_theorem_2 = MathTex("b^2 = 25 - 9", font_size = 40).next_to(new_theorem_1, DOWN)
        self.play(Write(new_theorem_2))
        self.wait(1)
        new_theorem_3 = MathTex("b^2 = 16", font_size = 40).next_to(new_theorem_2, DOWN)
        self.play(Write(new_theorem_3))
        self.wait(1)
        new_theorem_4 = MathTex("b = \sqrt{16}", font_size = 40).next_to(new_theorem_3, DOWN)
        self.play(Write(new_theorem_4))
        self.wait(2)
        new_theorem_5 = MathTex("b = 4", font_size = 40).next_to(new_theorem_4, DOWN)
        self.play(Write(new_theorem_5))
        self.wait(5)
        self.clear()
        self.wait(2)

class ConversePythagoras(Scene):
    def construct(self):
        point_a = [2, -2, 0]
        point_b = [5,-2,0]
        point_c = [5,1,0]

        base = Line(point_a, point_b, color = RED)
        height = Line(point_a, point_c, color = BLUE)
        hypotenuse = Line(point_b, point_c, color = GREEN)

        base_label = Text('a', font_size=30, color=RED_B).next_to(base, DOWN)
        height_label = Text('b', font_size=30, color=GREEN_B).next_to(height, RIGHT)
        hypotenuse_label = Text('c', font_size=30, color=BLUE_B).move_to(height.get_center() + UP*0.4)

        base_number = MathTex(r"3", font_size=40).move_to(base_label.get_center())
        height_number = MathTex(r"4", font_size=40).move_to(height_label.get_center())
        hypotenuse_number = MathTex(r"5", font_size=40).move_to(hypotenuse_label.get_center())

        title = Text("Converse of Pythagoras", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        subtitle = Text('What if we wanted to prove a triangle is right angled?', font_size = 30).next_to(title, DOWN*2)
        self.play(Write(subtitle))
        self.wait(1)



    #draw triangle
        self.play(Create(base), Write(base_label))
        self.wait(0)
        self.play(Create(height), Write(hypotenuse_label))
        self.wait(0)
        self.play(Create(hypotenuse), Write(height_label))


        theorem =  MathTex("c^2", "=", "a^2", "+", "b^2", font_size=40).to_edge(LEFT).shift(0.5)
        self.play(Create(theorem))

        # Access individual parts
        c_squared = theorem[0]  # "c^2"
        equals = theorem[1]     # "="
        a_squared = theorem[2]  # "a^2"
        plus = theorem[3]       # "+"
        b_squared = theorem[4]  # "b^2"

        # Step 1: Highlight c^2
        self.play(c_squared.animate.set_color(BLUE).scale(1.2))
        self.wait(1)

        # Step 2: Highlight the right side
        group_right = VGroup(a_squared, plus, b_squared)
        self.play(group_right.animate.set_color(RED).scale(1.1))
        self.wait(1)

        # Step 3: Split terms
        a_squared_target = a_squared.copy().shift(RIGHT*2)
        b_squared_target = b_squared.copy().shift(RIGHT*2.5)
        plus_target = plus.copy().shift(RIGHT*2.25)

        self.play(
            a_squared.animate.move_to(a_squared_target),
            b_squared.animate.move_to(b_squared_target),
            plus_target.animate.move_to(plus_target),
            FadeOut(equals),
            FadeOut(plus)
            
        )
        self.wait(1)


    ## add labels to triangle
        self.play(Transform(hypotenuse_label, hypotenuse_number))
        self.play(Transform(base_label, base_number))
        self.play(Transform(height_label, height_number))
        self.wait(1)

        ##animate the c squared
        c_squared_solved = MathTex("c^2 = 5^2", font_size =40, color= BLUE).next_to(c_squared, DOWN*2)
        c_squared_solved_2 = MathTex("= 25", font_size =40, color= BLUE).next_to(c_squared_solved, DOWN*2)

        self.play(Create(c_squared_solved))
        self.wait(1)
        self.play(Create(c_squared_solved_2))

        ##animate a squared
        a_squared_solved = MathTex("= 3^2 + 4^2", font_size =40, color= RED).next_to(a_squared_target, DOWN*2)
        a_squared_solved_2 = MathTex("= 25", font_size =40, color= RED).next_to(a_squared_solved, DOWN*2)

        self.play(Create(a_squared_solved))
        self.wait(1)
        self.play(Create(a_squared_solved_2))

        end = MathTex(r"\text{Since } c^2 = a^2 + b^2, \text{ then we can say the triangle is right-angled.}", font_size=30).to_corner(DL)

        self.play(Write(end))
        self.wait(10)
        self.clear()
        self.wait(3)


class Summary(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras' Theorem - Summary", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Key Point 1: Theorem Statement
        theorem = MathTex(
            r"c^2 = a^2 + b^2",
            font_size=40,
            color=BLUE
        ).next_to(title, DOWN*2)
        theorem_text = Text(
            "The square of the hypotenuse is equal to\nthe sum of the squares of the other two sides.",
            font_size=30,
        ).next_to(theorem, DOWN)
        self.play(Write(theorem))
        self.play(FadeIn(theorem_text))
        self.wait(2)


        # Key Point 3: Converse
        converse_title = Text(
            "Converse of Pythagoras",
            font_size=40,
            color=RED
        ).next_to(theorem_text, DOWN*2)
        converse_text = Text(
            "If the square of the longest side equals\nthe sum of the squares of the other two sides,\nthe triangle is a right triangle.",
            font_size=30,
        ).next_to(converse_title, DOWN)
        self.play(Write(converse_title))
        self.play(FadeIn(converse_text))
        self.wait(3)

        # Ending Note
        end_note = Text(
            "Pythagoras' theorem is a key concept in geometry\nand has applications in various fields like engineering,\nphysics, and architecture.",
            font_size=30,
        ).to_edge(DOWN)
        self.play(FadeIn(end_note))
        self.wait(4)

        # Fade Out Everything
        self.play(FadeOut(title, theorem, theorem_text, converse_title, converse_text, end_note))
        self.wait(1)


