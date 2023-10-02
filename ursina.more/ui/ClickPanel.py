from ursina import *


class ClickPanel(Button):
    def __init__(self, scale=(0.3, 0.5), radius=0.01, color=color.black33, visible=False, **kwargs):
        super().__init__(paren=camera.ui, model=Quad(radius=radius), scale=scale, color=color, visible=visible, z=0)

        if 'color' in kwargs:
            setattr(self, 'color', kwargs['color'])
        self.highlight_color = self.color.tint(.01)
        self.pressed_color = self.color.tint(-.2)
        self.highlight_scale = 1
        self.pressed_scale = 1

        scale_btn = (1, 0.12)

        # for i in range(5):
        # c += .14
        # duplicate(self.button, origin=(0, -11.5), text=f"Button{i}", y=-c)
        self.button = Button(parent=self, text="Button1", radius=radius, scale=scale_btn, y=0.4, origin=(0, 0), z=-1,
                             highlight_color=color.tint(.05))
        self.button2 = Button(parent=self, text="Button2", radius=radius, scale=scale_btn, y=0.26, z=-1,
                              highlight_color=color.tint(.05))
        self.button3 = Button(parent=self, text="Button3", radius=radius, scale=scale_btn, y=0.12, z=-1,
                              highlight_color=color.tint(.05))
        self.button4 = Button(parent=self, text="Button4", radius=radius, scale=scale_btn, y=-0.02, z=-1,
                              highlight_color=color.tint(.05))
        self.button5 = Button(parent=self, text="Button5", radius=radius, scale=scale_btn, y=-0.16, z=-1,
                              highlight_color=color.tint(.05))
        self.button6 = Button(parent=self, text="Button6", radius=radius, scale=scale_btn, y=-0.3, z=-1,
                              highlight_color=color.tint(.05))

    def input(self, key):
        if held_keys["right mouse"]:
            if self.visible is False:
                self.visible = True
                self.position = mouse.x, mouse.y
            else:
                self.visible = False


if __name__ == "__main__":
    app = Ursina()
    window.borderless = False
    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    ClickPanel()

    app.run()
