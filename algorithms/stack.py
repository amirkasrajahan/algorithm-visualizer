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

class evalRPN(Scene):
    def construct(self):
        tokens = ["4", "13", "5", "/", "+"]
        operations = ['+', '-', '/', '*']

        group = VGroup(*[
            VGroup(Square(side_length=0.8), Text(str(token), font_size=30))
            for token in tokens
        ])

        frame = stack_frame(5).move_to(RIGHT * 3)
        self.play(Create(frame))
        self.wait(0.5)

        group.arrange(RIGHT).move_to(LEFT * 3)
        self.play(Create(group))
        self.wait(0.5)

        cells = list(group)
        n = len(tokens)
        current = pointer("Current", BLUE, DOWN).next_to(cells[0], DOWN, buff=0.1)
        self.play(FadeIn(current))

        # twin lists: stack[k] is the token in slot k, boxes[k] is the box drawn there
        stack = []
        boxes = []

        for i in range(n):
            self.play(current.animate.next_to(cells[i], DOWN, buff=0.1), run_time=0.3)

            # a new box starts on top of its token, then slides to the next free slot
            box = make_box(tokens[i]).move_to(cells[i])
            self.play(box.animate.move_to(slot(frame, len(stack))))
            stack.append(tokens[i])
            boxes.append(box)

        self.wait(0.5)

        # test: remove the top two, the way an operator will (pop from both lists)
        for _ in range(2):
            stack.pop()
            self.play(FadeOut(boxes.pop()))

        self.wait(1)


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


class StackPop(Scene):
    def construct(self):
        title = Text("Stack: Pop", font_size=40).to_edge(UP)
        complexity_label = Text("pop: O(1)", font_size=28).to_edge(DOWN)
        lifo = Text("Last In,\nFirst Out", font_size=28, color=YELLOW).move_to(LEFT * 4.5)
        self.play(Write(title), Write(complexity_label), Write(lifo))

        frame = stack_frame(5).move_to(DOWN * 0.5)
        self.play(Create(frame))

        values = [4, 8, 15, 23]
        boxes = [make_box(v).move_to(slot(frame, k)) for k, v in enumerate(values)]
        top = pointer("top", BLUE, RIGHT).next_to(boxes[-1], RIGHT, buff=0.1)
        self.play(*[FadeIn(b) for b in boxes], FadeIn(top))

        for _ in range(2):
            popped = values.pop()
            box = boxes.pop()
            op = Text(f"pop() -> {popped}", font_size=32, color=YELLOW).move_to(RIGHT * 4.5 + UP * 1.5)
            self.play(Write(op), box[0].animate.set_fill(YELLOW, opacity=0.6), run_time=0.6)

            # the top box lifts out and `top` drops to the new top
            new_top = slot(frame, len(boxes) - 1) + RIGHT * 0.7
            self.play(
                box.animate.move_to(frame.get_top() + UP * 0.6),
                top.animate.next_to(new_top, RIGHT, buff=0.1),
            )
            self.play(box.animate.move_to(RIGHT * 4.5 + UP * 0.2))
            self.play(FadeOut(box), FadeOut(op), run_time=0.5)

        self.play(Indicate(boxes[-1]))
        self.wait(1.5)


class ValidParentheses(Scene):
    s = "{[()]}"

    def construct(self):
        s = self.s
        pairs = {")": "(", "]": "[", "}": "{"}

        title = Text("Valid Parentheses", font_size=40).to_edge(UP)
        complexity_label = Text("Time: O(n)   Space: O(n)", font_size=28).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        chars = VGroup(*[Text(c, font_size=48) for c in s]).arrange(RIGHT, buff=0.5)
        chars.move_to(UP * 2.2)
        frame = stack_frame(4).move_to(DOWN * 0.8)
        self.play(Write(chars), Create(frame))

        side = LEFT * 4.3 + DOWN * 0.8
        stack = []  # (opening char, its box, its index in s)
        failed = False
        for i, ch in enumerate(s):
            self.play(chars[i].animate.set_color(YELLOW), run_time=0.3)

            if ch not in pairs:
                box = make_box(ch, 40).move_to(slot(frame, len(stack)))
                op = Text(f"push '{ch}'", font_size=28, color=YELLOW).move_to(side)
                self.play(Write(op), FadeIn(box, shift=DOWN * 0.5))
                stack.append((ch, box, i))
                self.play(FadeOut(op), run_time=0.3)
            elif stack and stack[-1][0] == pairs[ch]:
                open_ch, box, j = stack.pop()
                op = Text(f"'{ch}' matches '{open_ch}'", font_size=28, color=GREEN).move_to(side)
                self.play(Write(op), box[0].animate.set_fill(GREEN, opacity=0.6))
                self.play(box.animate.shift(RIGHT * 3))
                self.play(
                    FadeOut(box), FadeOut(op),
                    chars[i].animate.set_color(GREEN), chars[j].animate.set_color(GREEN),
                )
            else:
                reason = f"'{ch}' does not match '{stack[-1][0]}'" if stack else f"nothing to match '{ch}'"
                op = Text(reason, font_size=28, color=RED).move_to(side)
                shake = [chars[i].animate.set_color(RED), Write(op)]
                if stack:
                    shake.append(stack[-1][1][0].animate.set_fill(RED, opacity=0.6))
                self.play(*shake)
                failed = True
                break

        # valid only if no mismatch happened and nothing is left unclosed
        valid = not failed and not stack
        verdict = Text("Valid" if valid else "Invalid", font_size=44, color=GREEN if valid else RED)
        verdict.move_to(RIGHT * 4.2 + DOWN * 0.8)
        self.play(Write(verdict))
        if not failed:
            note = Text("stack is empty" if not stack else "stack is not empty", font_size=28)
            self.play(Write(note.next_to(verdict, DOWN)))
        self.wait(1.5)


class InvalidParentheses(ValidParentheses):
    s = "([)]"
