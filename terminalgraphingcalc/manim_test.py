import manim as mn

class Test(mn.Scene):
    def construct(self):
        self.play(mn.Create(mn.Text("Hello, World!")))
        self.wait(1)
        self.play(mn.Create(mn.Text("Hello, World!")))