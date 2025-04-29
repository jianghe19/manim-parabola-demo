Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from manim import *
... 
... class ParabolaProblemScene(Scene):
...     def construct(self):
...         # ——— 场景 1：题目与抛物线方程求解 ———
...         title = Title("初三数学题：抛物线与直线的交点性质")
...         self.play(Write(title))
...         self.wait(1)
... 
...         eq0 = MathTex(r"y = x^2 + (2a-1)\,x + a^2 - \tfrac{25}{4}")
...         eq0.to_edge(UP)
...         self.play(Write(eq0))
...         self.wait(1)
... 
...         subs = MathTex(
...             r"3 = 3^2 + (2a-1)\cdot3 + a^2 - \tfrac{25}{4}"
...         ).next_to(eq0, DOWN, buff=1)
...         self.play(Write(subs))
...         self.wait(1)
... 
...         eq1 = MathTex(r"a^2 + 6a - \tfrac{13}{4} = 0").next_to(subs, DOWN, buff=0.5)
...         self.play(Transform(subs, eq1))
...         self.wait(1)
... 
...         sol = MathTex(r"a = \tfrac12").next_to(eq1, DOWN, buff=0.5)
...         self.play(Write(sol))
...         self.wait(1)
... 
...         parabola = MathTex(r"\Longrightarrow\;y = x^2 - 6").next_to(sol, DOWN, buff=0.8)
...         self.play(Write(parabola))
...         self.wait(2)
... 
...         # 清理，进入第二部分
...         self.play(
...             FadeOut(eq0), FadeOut(subs), FadeOut(sol), FadeOut(parabola)
        )
        self.wait(0.5)

        # ——— 场景 2：计算 AC·BD ———
        part2 = Text("第二部分：计算 $AC\\times BD$", font_size=36).to_edge(UP)
        self.play(Write(part2))
        self.wait(1)

        line = MathTex(r"y = x").next_to(part2, DOWN, buff=1)
        self.play(Write(line))
        self.wait(1)

        solve_inter = MathTex(
            r"x = x^2 - 6 \;\Longrightarrow\; x^2 - x - 6 = 0 \;\Longrightarrow\; x = 3,\,-2"
        ).next_to(line, DOWN, buff=0.8)
        self.play(Write(solve_inter))
        self.wait(1)

        pts = MathTex(r"A(3,3),\quad B(-2,-2)").next_to(solve_inter, DOWN, buff=0.8)
        self.play(Write(pts))
        self.wait(1)

        # 绘制坐标系并标点
        axes = NumberPlane(x_range=[-5,5,1], y_range=[-8,5,1]).shift(DOWN*0.5)
        self.play(Create(axes))
        self.wait(0.5)

        A_dot = Dot(axes.c2p(3, 3), color=YELLOW)
        A_label = MathTex("A(3,3)").next_to(A_dot, UR)
        B_dot = Dot(axes.c2p(-2, -2), color=YELLOW)
        B_label = MathTex("B(-2,-2)").next_to(B_dot, DL)
        self.play(FadeIn(A_dot, A_label), FadeIn(B_dot, B_label))
        self.wait(1)

        # 垂线
        C_dot = Dot(axes.c2p(0, 3), color=GREEN)
        C_label = MathTex("C(0,3)").next_to(C_dot, LEFT)
        D_dot = Dot(axes.c2p(0, -2), color=GREEN)
        D_label = MathTex("D(0,-2)").next_to(D_dot, LEFT)
        AC_line = Line(A_dot.get_center(), C_dot.get_center(), stroke_width=2)
        BD_line = Line(B_dot.get_center(), D_dot.get_center(), stroke_width=2)
        self.play(Create(AC_line), FadeIn(C_dot, C_label))
        self.wait(0.8)
        self.play(Create(BD_line), FadeIn(D_dot, D_label))
        self.wait(1)

        AC_val = MathTex(r"AC = 3").to_edge(DOWN).shift(LEFT*2)
        BD_val = MathTex(r"BD = 2").to_edge(DOWN).shift(RIGHT*2)
        self.play(Write(AC_val), Write(BD_val))
        self.wait(0.8)

        prod = MathTex(r"AC \times BD = 6").to_edge(DOWN)
        self.play(Write(prod))
        self.wait(2)

        # 清理，进入第三部分
        self.play(
            FadeOut(axes),
            FadeOut(A_dot), FadeOut(B_dot), FadeOut(A_label), FadeOut(B_label),
            FadeOut(C_dot), FadeOut(D_dot), FadeOut(C_label), FadeOut(D_label),
            FadeOut(AC_line), FadeOut(BD_line),
            FadeOut(AC_val), FadeOut(BD_val), FadeOut(prod),
            FadeOut(part2)
        )
        self.wait(0.5)

        # ——— 场景 3：交点距离与 m 的范围 ———
        part3 = Text("第三部分：直线与抛物线交点距离", font_size=36).to_edge(UP)
        self.play(Write(part3))
        self.wait(1)

        eq2 = MathTex(
            r"x^2 - 6 = -x + m \;\Longrightarrow\; x^2 + x - (m+6) = 0"
        ).next_to(part3, DOWN, buff=1)
        self.play(Write(eq2))
        self.wait(1)

        disc = MathTex(
            r"\Delta = 1 + 4(m+6)>0 \;\Longrightarrow\; m > -\tfrac{25}{4}"
        ).next_to(eq2, DOWN, buff=0.8)
        self.play(Write(disc))
        self.wait(1)

        dist = MathTex(
            r"d = \sqrt{2\,(x_1-x_2)^2} = \sqrt{2(4m+25)}"
        ).next_to(disc, DOWN, buff=0.8)
        self.play(Write(dist))
        self.wait(2)

        # 结束
        self.play(FadeOut(part3), FadeOut(eq2), FadeOut(disc), FadeOut(dist))
        bye = Text("—— 完 ——", font_size=48)
        self.play(Write(bye))
        self.wait(2)
