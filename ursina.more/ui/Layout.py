from ursina import *


class Layout(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=Quad(radius=.0), color=color.gray, **kwargs)
        self.color = self.color.tint(-.05)
        self.postion = (0, 5)
        self.scale = (10, 5)

        if "side" in kwargs:
            print(kwargs['side'])
            if kwargs["side"] == "TOP":
                self.position = (0, 5)
                self.scale = (15, 5)
            elif kwargs["side"] == "LEFT":
                self.position = (-8, 0)
                self.scale = (5, 10)
            elif kwargs["side"] == "BOTTOM":
                self.position = (0, -5)
                self.scale = (15, 5)
            elif kwargs["side"] == "RIGHT":
                self.position = (8, 0)
                self.scale = (5, 10)
            else:
                self.position = (0, 5)
                self.scale = (10, 5)


if __name__ == "__main__":
    app = Ursina()
    window.fullscreen = False
    window.borderless = False
    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    layout_top = Layout(side="TOP")

    layout_left = Layout(side="LEFT")

    layout_bottom = Layout(side="BOTTOM")
    
    layout_right = Layout(side="RIGHT")

    app.run()
