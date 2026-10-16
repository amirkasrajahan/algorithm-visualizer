from linked_list import pointer
from manim import *

BOX_H = 0.9


def stack_frame(capacity):
    """Open-top container sized for `capacity` boxes."""
    w, h = 1.8, BOX_H * capacity + 0.2
    return VMobject().set_points_as_corners([
        [-w / 2, h / 2, 0], [-w / 2, -h / 2, 0], [w / 2, -h / 2, 0], [w / 2, h / 2, 0],
    ])


def slot(frame, k):
    """Centre of the k-th box position, counting from the bottom of the frame."""
    return frame.get_bottom() + UP * (0.1 + BOX_H * (k + 0.5))


def make_box(label, font_size=32):
    return VGroup(Rectangle(width=1.4, height=BOX_H - 0.1), Text(str(label), font_size=font_size))


class StackPush(Scene):
    def construct(self):
        title = Text("Stack: Push", font_size=40).to_edge(UP)
        complexity_label = Text("push: O(1)", font_size=28).to_edge(DOWN)
        lifo = Text("Last In,\nFirst Out", font_size=28, color=YELLOW).move_to(LEFT * 4.5)
        self.play(Write(title), Write(complexity_label), Write(lifo))

        frame = stack_frame(5).move_to(DOWN * 0.5)
        self.play(Create(frame))

        # boxes[k] is the box sitting in slot k
        boxes = [make_box(v).move_to(slot(frame, k)) for k, v in enumerate([4, 8])]
        top = pointer("top", BLUE, RIGHT).next_to(boxes[-1], RIGHT, buff=0.1)
        self.play(*[FadeIn(b) for b in boxes], FadeIn(top))

        for v in [15, 23]:
            k = len(boxes)
            op = Text(f"push({v})", font_size=32, color=YELLOW).move_to(RIGHT * 4.5 + UP * 1.5)
            new = make_box(v).move_to(frame.get_top() + UP * 0.6)
            self.play(Write(op), FadeIn(new))

            # the new box drops in and `top` moves up to it
            self.play(
                new.animate.move_to(slot(frame, k)),
                top.animate.next_to(slot(frame, k) + RIGHT * 0.7, RIGHT, buff=0.1),
            )
            boxes.append(new)
            self.play(FadeOut(op), run_time=0.4)

        self.play(Indicate(boxes[-1]))
        self.wait(1.5)
