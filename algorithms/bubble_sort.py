import random

from manim import *


class BubbleSort(Scene):
    def construct(self):
        values = [1, 3, 7, 12, 15, 17, 19, 20, 25, 35]
        random.shuffle(values)

        title = Text("Bubble Sort", font_size=40).to_edge(UP)
        complexity_label = Text("Time Complexity: O(n²)", font_size=28).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        group = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in values
        ])
        group.arrange(RIGHT, buff=0.15)
        group.move_to(ORIGIN)
        self.play(Create(group))
        self.wait(0.3)

        # plain list mirrors `values`: cells[k] is always the box showing values[k]
        cells = list(group)
        n = len(values)

        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                left, right = cells[j], cells[j + 1]
                self.play(
                    left[0].animate.set_fill(YELLOW, opacity=0.7),
                    right[0].animate.set_fill(YELLOW, opacity=0.7),
                    run_time=0.2,
                )

                if values[j] > values[j + 1]:
                    swapped = True
                    self.play(Swap(left, right), run_time=0.5)
                    values[j], values[j + 1] = values[j + 1], values[j]
                    cells[j], cells[j + 1] = cells[j + 1], cells[j]

                self.play(
                    left[0].animate.set_fill(WHITE, opacity=0),
                    right[0].animate.set_fill(WHITE, opacity=0),
                    run_time=0.15,
                )

            # last cell of this pass is now in its final place
            self.play(cells[n - 1 - i][0].animate.set_fill(GREEN, opacity=0.6), run_time=0.3)
            if not swapped:
                break

        self.play(
            AnimationGroup(*[c[0].animate.set_fill(GREEN, opacity=0.6) for c in cells], lag_ratio=0.1)
        )
        self.wait(2)
