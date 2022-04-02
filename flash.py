from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


class play(Scene):
    def construct(self):
        # To run this scene properly, you should have "Consolas" font in your computer
        # for full usage, you can see https://github.com/3b1b/manim/pull/680

        # Intro Build
        text = Text("Batman 101", font="American Typewriter", font_size=90)
        difference = Text("Would the Flash be faster on a bike?",
                          font="American Typewriter", font_size=24,
                          t2c={"Flash": RED, "faster": RED, "bike": BLUE}
                          )
        # Energy Build
        fonts = Text(
            "Let's start by determining how much energy The Flash uses", font="American Typewriter",
            t2c={"energy": BLUE, "The Flash": RED}
        )
        fonts.set_width(FRAME_WIDTH - 1)

        # Speed Build
        stat_title = Text(
            "Flash Stats", font="American Typewriter", font_size=90)
        stat_speed = Text("According to Google, he runs at 2,532 Miles Per Hour or 1,132 Meters Per Second",
                          font="American Typewriter", font_size=24,
                          t2c={"Google": BLUE, "2,532 Miles Per Hour": RED, "1,132 Meters Per Second": RED})
        stat_weight = Text("According to Google, he weighs 195 pounds or 88 kilograms",
                           font="American Typewriter", font_size=24,
                           t2c={"Google": BLUE, "195 pounds": GREEN, "88 kilograms": GREEN})

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

        # Move to Circular Motion Build
        circle_message = Text("Let's take that energy and apply it \nto The Flash on a bike", font_size=90, t2c={
            "energy": GREEN, "The Flash": RED, "bike": BLUE})

        # Circle Buid
        circle1 = Circle()
        circle1.set_fill(BLUE, opacity=0.0)
        circle1.set_stroke(BLUE_E, width=4)
        circle2 = Circle()

        circle2.set_fill(BLUE, opacity=0.0)
        circle2.set_stroke(BLUE_E, width=4)
        square1 = Square()
        square2 = Square()

        line = always_redraw(lambda:
                             Line(start=circle1.get_center(),
                                  end=circle2.get_center())
                             )

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
        motion_equation_7 = Tex(
            "v = 1645.23 m/s (3680 mph)",
            isolate=["v^2", *to_isolate], font_size=size)

        # Plays

        # Intro Play
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(5)

        # Energy Play
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
        self.play(Write(fonts))
        self.wait(5)
        self.play(FadeOut(fonts, shift=DOWN))

        # Speed Play
        VGroup(stat_title, stat_speed, stat_weight).arrange(DOWN, buff=1)
        self.play(Write(stat_title))
        self.play(FadeIn(stat_speed, UP))
        self.play(FadeIn(stat_weight, UP))
        self.wait(5)
        self.play(FadeOut(stat_title), FadeOut(
            stat_speed, shift=DOWN), FadeOut(stat_weight, shift=DOWN))

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

        # Circular intro
        self.play(FadeIn(circle_message, DOWN))
        self.wait(2)
        self.play(
            circle_message.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(FadeOut(circle_message, UP))

        # Show torque
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
        self.play(TransformMatchingTex(
            motion_equation_6.copy(), motion_equation_7))
        self.wait(5)

        self.play(FadeOut(v_circle), FadeOut(m_circle), FadeOut(k_circle), FadeOut(
            motion_equation_1), FadeOut(motion_equation_2),  FadeOut(motion_equation_3), FadeOut(motion_equation_4),  FadeOut(
            motion_equation_5), FadeOut(motion_equation_6), FadeOut(motion_equation_8))
        self.play(motion_equation_7.center)
        self.wait(5)
        self.play(FadeOut(motion_equation_7, shift=UP))

        self.wait()

        # Outro
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(5)
