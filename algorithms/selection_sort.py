from manim import *


class SelectionSort(Scene):
    def construct(self):
        array = [5, 2, 7, 1, 6, 3, 4]

        title = Text("Selection Sort", font_size=40).to_edge(UP)
        complexity_label = Text("Time Complexity: O(n²)", font_size=28).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        group = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in array
        ])
        group.arrange(direction=RIGHT, buff=0.6)
        group.move_to(ORIGIN)
        self.play(Create(group))
        self.wait(0.5)

        # cells[k] is always the box showing array[k]; swap both together
        cells = list(group)
        n = len(array)

        i_label = Text("i", font_size=24, color=BLUE).next_to(cells[0], DOWN, buff=0.15)
        j_label = Text("j", font_size=24, color=YELLOW)
        min_label = Text("min", font_size=24, color=RED).next_to(cells[0], UP, buff=0.15)
        self.play(FadeIn(i_label), FadeIn(min_label))

        def paint(i, j, low, done):
            """Fill animation for every box, computed from the current state."""
            anims = []
            for k, cell in enumerate(cells):
                if k < done:
                    fill = (GREEN, 0.6)
                elif k == low:
                    fill = (RED, 0.7)
                elif k == j:
                    fill = (YELLOW, 0.7)
                elif k == i:
                    fill = (BLUE, 0.5)
                else:
                    fill = (WHITE, 0)
                anims.append(cell[0].animate.set_fill(*fill))
            return anims

        for i in range(n - 1):
            low = i
            j_label.next_to(cells[i + 1], DOWN, buff=0.15)
            self.play(
                i_label.animate.next_to(cells[i], DOWN, buff=0.15),
                min_label.animate.next_to(cells[low], UP, buff=0.15),
                FadeIn(j_label),
                *paint(i, None, low, i),
                run_time=0.5,
            )

            for j in range(i + 1, n):
                self.play(
                    j_label.animate.next_to(cells[j], DOWN, buff=0.15),
                    *paint(i, j, low, i),
                    run_time=0.3,
                )
                if array[j] < array[low]:
                    low = j
                    self.play(
                        min_label.animate.next_to(cells[low], UP, buff=0.15),
                        *paint(i, j, low, i),
                        run_time=0.3,
                    )

            self.play(FadeOut(j_label), *paint(i, None, low, i), run_time=0.3)

            if low != i:
                self.play(
                    Swap(cells[i], cells[low]),
                    min_label.animate.next_to(cells[i], UP, buff=0.15),
                    run_time=0.6,
                )
                array[i], array[low] = array[low], array[i]
                cells[i], cells[low] = cells[low], cells[i]

            # position i is now final
            self.play(*paint(i, None, None, i + 1), run_time=0.4)

        self.play(*paint(None, None, None, n), FadeOut(i_label), FadeOut(min_label))
        self.wait(1.5)
