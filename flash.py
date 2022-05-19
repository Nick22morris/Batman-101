from venv import create

from matplotlib.pyplot import draw
from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


class intro(Scene):
    def construct(self):
        # Intro Build
        text = Text("Batman 101", font="American Typewriter", font_size=90)
        difference = Text("Would the Flash be faster on a bike?",
                          font="American Typewriter", font_size=24,
                          t2c={"Flash": RED, "faster": RED, "bike": BLUE})

        # Intro Play
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(5)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))


class energy_text(Scene):
    def construct(self):
        # Build Screen 1
        fonts = Text(
            "Let's start by determining how much energy The Flash uses", font="American Typewriter",
            t2c={"energy": BLUE, "The Flash": RED}
        )
        fonts.set_width(FRAME_WIDTH - 1)

        # Build Screen 2
        stat_title = Text(
            "Flash Stats", font="American Typewriter", font_size=90)
        stat_speed = Text("According to Google, he runs at 2,532 Miles Per Hour or 1,132 Meters Per Second",
                          font="American Typewriter", font_size=24,
                          t2c={"Google": BLUE, "2,532 Miles Per Hour": RED, "1,132 Meters Per Second": RED})
        stat_weight = Text("According to Google, he weighs 195 pounds or 88 kilograms",
                           font="American Typewriter", font_size=24,
                           t2c={"Google": BLUE, "195 pounds": GREEN, "88 kilograms": GREEN})

        # Play Screen 1
        self.play(Write(fonts))
        self.wait(5)
        self.play(FadeOut(fonts, shift=DOWN))

        # Play Screen 2
        VGroup(stat_title, stat_speed, stat_weight).arrange(DOWN, buff=1)
        self.play(Write(stat_title))
        self.play(FadeIn(stat_speed, UP))
        self.play(FadeIn(stat_weight, UP))
        self.wait(5)
        self.play(FadeOut(stat_title), FadeOut(
            stat_speed, shift=DOWN), FadeOut(stat_weight, shift=DOWN))


class standard_energy_eq(Scene):
    def construct(self):
        # Energy Equation Build
        to_isolate = ["K", "=", r"\frac {1}{2}", "*", "m/s", "kg"]
        v = Text("v = 1132 m/s", font="American Typewriter", font_size=24)
        v.to_corner(UL)
        m = Text("m = 88 kg", font="American Typewriter", font_size=24)
        m.to_corner(UL)
        m.shift(DOWN * 0.5)
        k = Tex(r"K = \frac {1}{2} * m * v^2", isolate=["v^2", *to_isolate])
        k2 = Tex(r"K = \frac {1}{2} * 88 kg * (1132 m/s)^2",
                 isolate=["v^2", *to_isolate])
        k3 = Tex(r"K = 56,382,656 J", isolate=["v^2", *to_isolate])

        # Equation Energy
        VGroup(k, k2, k3).arrange(DOWN)
        self.play(FadeIn(v, DOWN))
        self.play(FadeIn(m, DOWN))
        self.wait(3)
        self.play(Write(k))
        self.play(TransformMatchingTex(k.copy(), k2))
        self.wait(3)
        self.play(TransformMatchingTex(k2.copy(), k3))
        self.wait(5)
        self.play(FadeOut(v), FadeOut(m), FadeOut(k), FadeOut(k2))
        self.play(k3.center)
        self.wait(5)
        self.play(FadeOut(k3, shift=UP))


class circle_intro_text(Scene):
    def construct(self):
        # Circular Motion Text Build
        circle_message = Text("Let's take that energy and apply it \nto The Flash on a bike", font_size=90, t2c={
            "energy": GREEN, "The Flash": RED, "bike": BLUE})

        # Circular intro
        self.play(FadeIn(circle_message, DOWN))
        self.wait(2)
        self.play(
            circle_message.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(FadeOut(circle_message, UP))


class circle_graphic(Scene):
    def construct(self):
        # Object Build
        square = Square()
        circle = Circle()
        circle_full = Circle()
        circle_full.set_fill(RED, opacity=1)
        circle_full.set_stroke(RED, width=4)
        circle_full.to_edge(LEFT)
        circle_full.shift(UP * 2)
        circle.set_fill(BLUE, opacity=0.0)
        circle.set_stroke(BLUE_E, width=4)

        # Object Animation
        VGroup(square, circle).arrange(DOWN).to_edge(LEFT)
        self.play(ShowCreation(square))
        self.play(ShowCreation(circle))
        circle.save_state()
        self.play(square.animate.shift(RIGHT * 8),
                  circle.animate.shift(RIGHT * 8),
                  run_time=3)
        self.play(circle.animate.to_edge(LEFT))
        self.play(Uncreate(square))
        self.play(DrawBorderThenFill(circle_full))
        self.play(
            circle.animate.shift(RIGHT * 8),
            run_time=4,)
        self.play(
            circle_full.animate.shift(RIGHT * 8),
            run_time=2,)
        self.play(Uncreate(circle_full))
        self.play(circle.animate.center())
        self.wait()
        new_circle = Circle().scale(0.5)
        self.play(TransformFromCopy(circle, new_circle))

        line = always_redraw(
            lambda:
            Line(start=circle.get_top(), end=circle.get_center())
        )

        self.play(ShowCreation(line))
        self.play(circle.animate.scale(3))
        line2 = Line(start=circle.get_top(), end=circle.get_bottom())
        self.play(ShowCreation(line2))
        self.play(Uncreate(line))
        self.play(Rotate(line2))
        self.play(Uncreate(line2), Uncreate(circle), Uncreate(new_circle))
        self.wait()


class circle_eq(Scene):
    def construct(self):
        # Eq Build
        torque_eq_1 = Tex(r"\tau = \text{Frsin}\theta")
        torque_eq_2 = Tex(r"\tau = I\alpha")
        torque_eq_2_copy = torque_eq_2.copy()

        # Equation 1 Lines Build
        line_bottom = Line()
        line_up = Line(start=line_bottom.get_center(), end=UP)
        line_up.stretch(factor=2, dim=1)
        line_up.shift(UP * 0.5)
        line_bottom.shift(RIGHT)
        arc = CurvedArrow(
            start_point=line_bottom.get_right(), end_point=line_up.get_top())

        # Equation 2 Shape Build
        square = Square()
        circle = Circle()
        # line2.rotate(angle=1)

        # Object Animation
        VGroup(torque_eq_1, torque_eq_2).arrange(DOWN)
        self.play(ShowCreation(torque_eq_1))
        self.wait()
        self.play(ShowCreation(torque_eq_2))
        self.wait()
        self.play(Uncreate(torque_eq_2), torque_eq_1.animate.to_edge(UP))

        # Equation 1 Lines Play
        self.play(ShowCreation(line_bottom), ShowCreation(line_up))
        self.wait()
        self.play(ShowCreation(arc))
        self.wait()
        self.play(Uncreate(line_bottom), Uncreate(line_up), Uncreate(arc), Uncreate(
            torque_eq_1))

        # Equation 2 Shapes Play
        self.play(ShowCreation(torque_eq_2_copy))
        self.play(torque_eq_2_copy.animate.to_edge(UP))
        VGroup(circle, square).arrange(LEFT)
        self.play(ShowCreation(square))
        self.play(Rotate(square))
        self.play(ShowCreation(circle))
        line1 = Line(start=circle.get_top(), end=circle.get_bottom())
        line2 = Line(start=circle.get_top(), end=circle.get_bottom())
        self.play(Rotate(line2))
        self.play(ShowCreation(line1))
        self.wait()


class circle_math(Scene):
    def construct(self):
        # Circle Equation Build
        to_isolate = ["K", "=", "1/2", "I", "w", "^2", "m", "v", "+"]
        v_circle = Text(
            "v = 1132 m/s", font="American Typewriter", font_size=24)
        v_circle.to_corner(UL)
        m_circle = Text("m = 88 kg", font="American Typewriter", font_size=24)
        m_circle.to_corner(UL)
        m_circle.shift(DOWN * 0.5)
        k_circle = Text("K = 56,382,656 J",
                        font="American Typewriter", font_size=24)
        k_circle.to_corner(UL)
        k_circle.shift(DOWN)
        size = 24
        motion_equation_1 = Tex(
            "K",
            "= ",
            r"\frac {1}{2} mv^2",
            "+",
            r"\frac {1}{2} Iw^2",
            "+",
            r"\frac {1}{2} Iw^2",
            "+",
            r"\frac {1}{2} Iw^2")
        #  isolate=["v^2", *to_isolate], font_size=size
        brace1 = Brace(mobject=motion_equation_1[2], direction=UP, buff=0.2)
        brace_text1 = brace1.get_text("Translation", font_size=20)
        brace2 = Brace(mobject=motion_equation_1[4], direction=UP, buff=0.2)
        brace_text2 = brace2.get_text("Wheel 1", font_size=20)
        brace3 = Brace(mobject=motion_equation_1[6], direction=UP, buff=0.2)
        brace_text3 = brace3.get_text("Wheel 2", font_size=20)
        brace4 = Brace(mobject=motion_equation_1[8], direction=UP, buff=0.2)
        brace_text4 = brace4.get_text("Pedal", font_size=20)
        motion_equation_2 = Tex(
            r"K = \frac {1}{2} mv^2 + \frac {1}{2} I(v/r)^2 + \frac {1}{2} I(v/r)^2 + \frac {1}{2} I(v/r)^2",
            isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_8 = Tex(
            r"K = \frac {1}{2} mv^2 + \frac {1}{2} (mr^2)(v/r)^2 + \frac {1}{2} (mr^2)(v/r)^2 + \frac {1}{2} (\frac {1}{3}mr^2)(v/r)^2",
            isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_3 = Tex(
            r"K = \frac {1}{2} (96)v^2 + \frac {1}{2} mv^2 + \frac {1}{2} mv^2 + \frac {1}{6} mv^2",
            isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_4 = Tex(
            r"K = 48v^2 + \frac {1}{2} (1.4 kg)v^2 + \frac {1}{2} (1.4 kg)v^2 + \frac {1}{2} (0.2 kg)v^2",
            isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_5 = Tex(
            r"K = 50.83v^2",
            isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_6 = Tex(r"\sqrt{\frac {k}{50.83}} = v",
                                isolate=["v^2", *to_isolate], font_size=size)
        motion_equation_7 = Text(
            "v = 1645.23 (m/s) or 3680 (mph)",
            isolate=["v^2", *to_isolate], font_size=size)

        # Circle Equation Play
        equation_group = VGroup(motion_equation_2, motion_equation_8,
                                motion_equation_3, motion_equation_4, motion_equation_5,
                                motion_equation_6, motion_equation_7).arrange(DOWN)
        self.play(FadeIn(v_circle, DOWN))
        self.play(FadeIn(m_circle, DOWN))
        self.play(FadeIn(k_circle, DOWN))
        self.wait(3)
        self.play(Write(motion_equation_1))

        self.play(ShowCreation(brace1), ShowCreation(brace2),
                  ShowCreation(brace3), ShowCreation(brace4),
                  ShowCreation(brace_text1), ShowCreation(brace_text2),
                  ShowCreation(brace_text3), ShowCreation(brace_text4),)
        self.wait(10)

        self.play(motion_equation_1.animate.to_edge(UP))
        self.play(Uncreate(brace1), Uncreate(brace2), Uncreate(brace3), Uncreate(brace4), Uncreate(
            brace_text1), Uncreate(brace_text2), Uncreate(brace_text3), Uncreate(brace_text4))
        self.play(TransformMatchingTex(
            motion_equation_1.copy(), motion_equation_2))
        self.wait(3)
        self.play(TransformMatchingTex(
            motion_equation_2.copy(), motion_equation_8))
        self.wait(3)
        self.play(TransformMatchingTex(
            motion_equation_8.copy(), motion_equation_3))
        self.wait(5)
        self.play(TransformMatchingTex(
            motion_equation_3.copy(), motion_equation_4))
        self.wait(5)
        self.play(TransformMatchingTex(
            motion_equation_4.copy(), motion_equation_5))
        self.wait(5)
        self.play(TransformMatchingTex(
            motion_equation_5.copy(), motion_equation_6))
        self.wait(5)
        self.play(Write(motion_equation_7))
        self.wait(5)

        self.play(FadeOut(v_circle), FadeOut(m_circle), FadeOut(k_circle), FadeOut(
            motion_equation_1), FadeOut(motion_equation_2),  FadeOut(motion_equation_3), FadeOut(motion_equation_4),  FadeOut(
            motion_equation_5), FadeOut(motion_equation_6), FadeOut(motion_equation_8))
        self.play(motion_equation_7.center)
        self.wait(5)
        self.play(FadeOut(motion_equation_7, shift=UP))

        self.wait()

class why_wheels_win(Scene):
    def construct(self):
        torque_eq_1 = Tex(r"\tau = \text{Frsin}\theta")
        torque_eq_2 = Tex(r"\tau = I\alpha")
        message = Text("Why is this more effecient?")
        VGroup(message, torque_eq_1, torque_eq_2).arrange(DOWN)
        square = Square()
        circle = Circle()
        VGroup(square, circle).arrange(RIGHT)
        line1 = Line(start=circle.get_top(), end=circle.get_bottom())
        line2 = Line(start=circle.get_left(), end=circle.get_right())


        self.play(ShowCreation(message))
        self.wait()
        self.play(ShowCreation(torque_eq_1))
        self.wait()
        self.play(ShowCreation(torque_eq_2))
        self.wait()
        self.play(Uncreate(torque_eq_1), Uncreate(message), torque_eq_2.animate.to_edge(UP))
        self.play(ShowCreation(circle), ShowCreation(square))
        self.wait()
        self.play(ShowCreation(line1), ShowCreation(line2))
        self.play(Rotate(line1, 10),Rotate(line2, 10), run_time=10)
        self.wait()
        self.play(square.animate.shift(LEFT * 2))
        self.wait()
        self.play(Uncreate(circle), Uncreate(square), Uncreate(line1), Uncreate(line2), Uncreate(torque_eq_2))
        self.wait()
