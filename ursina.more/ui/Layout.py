from ursina import *


class Layout(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=Quad(radius=.025), color=color.gray, **kwargs)
        self.color = self.color.tint(.2)
        self.scale = (8, 8)

        if "side" in kwargs:
            print(kwargs['side'])
            if kwargs["side"] == "TOP":
                self.position = (0, 5)
            elif kwargs["side"] == "LEFT":
                self.position = (-8, 0)
            elif kwargs["side"] == "BOTTOM":
                self.position = (0, -5)
            elif kwargs["side"] == "RIGHT":
                self.position = (8, 0)
            else:
                self.position = (0, 0)


if __name__ == "__main__":
    app = Ursina()

    layout = Layout(side="LEFT")

    app.run()
