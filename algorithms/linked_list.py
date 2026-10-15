from manim import *


def pointer(label, color, side):
    """An arrow plus label that sits on `side` (UP or DOWN) of whatever it points at."""
    arrow = Arrow(side * 0.8, ORIGIN, buff=0, color=color)
    text = Text(label, font_size=24, color=color).next_to(arrow, side, buff=0.1)
    return VGroup(arrow, text)


class LinkedListTraversal(Scene):
    def construct(self):
        values = [3, 7, 12, 5, 9]

        title = Text("Linked List Traversal", font_size=40).to_edge(UP)
        complexity_label = Text("Time Complexity: O(n)", font_size=28).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        nodes = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in values
        ])
        null = Text("NULL", font_size=28)
        row = VGroup(*nodes, null).arrange(RIGHT, buff=1)
        row.move_to(ORIGIN)

        # each arrow runs from one node to the next; the last one points at NULL
        links = VGroup(*[
            Arrow(a.get_right(), b.get_left(), buff=0.1)
            for a, b in zip(row, row[1:])
        ])
        self.play(Create(nodes), Write(null))
        self.play(Create(links))

        head = pointer("head", BLUE, UP).next_to(nodes[0], UP, buff=0.1)
        curr = pointer("curr", YELLOW, DOWN).next_to(nodes[0], DOWN, buff=0.1)
        self.play(FadeIn(head))

        visited = Text("Visited:", font_size=28).to_edge(LEFT, buff=1).set_y(-2.6)
        self.play(Write(visited))

        last = visited
        for k, v in enumerate(values):
            if k == 0:
                self.play(FadeIn(curr))
            else:
                self.play(curr.animate.next_to(nodes[k], DOWN, buff=0.1))

            box = nodes[k][0]
            self.play(box.animate.set_fill(YELLOW, opacity=0.7), run_time=0.3)

            item = Text(str(v), font_size=28).next_to(last, RIGHT, buff=0.4)
            self.play(Write(item), box.animate.set_fill(GREEN, opacity=0.6), run_time=0.4)
            last = item

        # curr = curr.next is None, so the traversal is finished
        self.play(curr.animate.next_to(null, DOWN, buff=0.1))
        self.play(Indicate(null, color=RED))
        self.wait(1.5)
