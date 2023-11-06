from manim import *


class Img(Scene):
    def construct(self):
        plan = SVGMobject('./img/plain_template.svg').shift(LEFT*3).scale(3)

        self.play(Write(plan), rate_func=smooth, run_time=3)
        self.wait(0.5)
