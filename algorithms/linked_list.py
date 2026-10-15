from manim import *


def pointer(label, color, side):
    """An arrow plus label that sits on `side` (UP or DOWN) of whatever it points at."""
    arrow = Arrow(side * 0.8, ORIGIN, buff=0, color=color)
    text = Text(label, font_size=24, color=color).next_to(arrow, side, buff=0.1)
    return VGroup(arrow, text)


def make_list(values):
    """Nodes, a NULL terminator, and the arrows between them, centred on screen."""
    nodes = VGroup(*[
        VGroup(Square(side_length=1), Text(str(v), font_size=36))
        for v in values
    ])
    null = Text("NULL", font_size=28)
    row = VGroup(*nodes, null).arrange(RIGHT, buff=1).move_to(ORIGIN)
    # each arrow runs from one node to the next; the last one points at NULL
    links = VGroup(*[
        Arrow(a.get_right(), b.get_left(), buff=0.1)
        for a, b in zip(row, row[1:])
    ])
    return nodes, null, links


class LinkedListTraversal(Scene):
    def construct(self):
        values = [3, 7, 12, 5, 9]

        title = Text("Linked List Traversal", font_size=40).to_edge(UP)
        complexity_label = Text("Time Complexity: O(n)", font_size=28).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        nodes, null, links = make_list(values)
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


class LinkedListInsertion(Scene):
    def construct(self):
        values = [3, 7, 12, 9]
        new_value = 10
        after = 1  # insert after values[after], i.e. after the node holding 7

        title = Text("Linked List Insertion", font_size=40).to_edge(UP)
        complexity_label = Text(
            "Time Complexity: O(n) to find, O(1) to link", font_size=28
        ).to_edge(DOWN)
        self.play(Write(title), Write(complexity_label))

        nodes, null, links = make_list(values)
        self.play(Create(nodes), Write(null))
        self.play(Create(links))

        head = pointer("head", BLUE, UP).next_to(nodes[0], UP, buff=0.1)
        curr = pointer("curr", YELLOW, DOWN).next_to(nodes[0], DOWN, buff=0.1)
        self.play(FadeIn(head), FadeIn(curr))

        caption = Text(f"Insert {new_value} after {values[after]}", font_size=28, color=YELLOW)
        caption.set_y(-2.7)
        self.play(Write(caption))

        def say(message, *animations, run_time=1):
            nonlocal caption
            new_caption = Text(message, font_size=28, color=YELLOW).move_to(caption)
            self.play(FadeTransform(caption, new_caption), *animations, run_time=run_time)
            caption = new_caption

        # walk curr to the node we insert after
        for k in range(1, after + 1):
            self.play(curr.animate.next_to(nodes[k], DOWN, buff=0.1))
        self.play(nodes[after][0].animate.set_fill(YELLOW, opacity=0.7), run_time=0.3)

        new = VGroup(Square(side_length=1, color=GREEN), Text(str(new_value), font_size=36))
        gap_centre = (nodes[after].get_center() + nodes[after + 1].get_center()) / 2
        new.move_to(gap_centre + UP * 2)
        say("Create the new node", FadeIn(new))

        # order matters: link the new node forward first, or the rest of the list is lost
        new_next = Arrow(new.get_bottom(), nodes[after + 1].get_top(), buff=0.1)
        say("1. new.next = curr.next", Create(new_next))

        reroute = Arrow(nodes[after].get_top(), new.get_left(), buff=0.1)
        say("2. curr.next = new", Transform(links[after], reroute))

        # re-space the list: build the final layout only to read its positions
        final_values = values[: after + 1] + [new_value] + values[after + 1:]
        final_nodes, final_null, final_links = make_list(final_values)

        moves = [new.animate.move_to(final_nodes[after + 1].get_center())]
        for k, node in enumerate(nodes):
            final_k = k if k <= after else k + 1
            moves.append(node.animate.move_to(final_nodes[final_k].get_center()))
        moves.append(null.animate.move_to(final_null.get_center()))

        arrows = [(links[k], final_links[k]) for k in range(after)]
        arrows += [(links[after], final_links[after]), (new_next, final_links[after + 1])]
        arrows += [(links[k], final_links[k + 1]) for k in range(after + 1, len(links))]
        moves += [Transform(old, final) for old, final in arrows]

        moves.append(head.animate.next_to(final_nodes[0], UP, buff=0.1))
        moves.append(curr.animate.next_to(final_nodes[after], DOWN, buff=0.1))
        say("Re-space the list", *moves, run_time=1.5)

        self.play(
            new[0].animate.set_fill(GREEN, opacity=0.6),
            nodes[after][0].animate.set_fill(WHITE, opacity=0),
        )
        say("Inserted: " + " -> ".join(map(str, final_values)), Indicate(new))
        self.wait(1.5)
