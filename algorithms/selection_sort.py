from manim import *
from random import shuffle
class SelectionSort(Scene):
    def construct(self):
        array = [1,2,3,4,5,6,7]
        shuffle(array)

        group = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in array
        ])

        group.arrange(direction=RIGHT, buff= 1)
        group.move_to(ORIGIN)
        self.play(Create(group))
        self.wait(0.5)

        cells = list(group)
        n = len(array)
        minText = Text("Min", font_size=24, color=RED)
        currentText = Text("Current", font_size=24, color=YELLOW)

        for i in range(n):
            current = i
            min = i
            

            self.play(cells[current][0].animate.set_fill(YELLOW, opacity = 0.7))
            currentText.next_to(cells[current], DOWN)
            self.play(Write(currentText))

            for j in range(i+1, n):
                if(array[j] < array[min]):
                    min = j

            self.play(cells[min][0].animate.set_fill(RED, opacity = 0.7), run_time=0.5)


            minText.next_to(cells[min], UP)
            self.play(Write(minText), run_time=0.5)
            array[current], array[min] = array[min], array[current]

            cells[current], cells[min] = cells[min], cells[current]


            self.play(Swap(cells[min], cells[current]), run_time = 0.5)

            



                



                
        




