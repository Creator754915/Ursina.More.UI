from ursina import *


class CheckBox(Button):
    def __init__(self, start_state=False, **kwargs):
        super().__init__(start_state=start_state, state=start_state, scale=Text.size, model=Quad(radius=.25))
        self._state = self.state

        self.state = start_state

        for key, value in kwargs.items():
            setattr(self, key, value)

        # self.icon_entity.scale = self.scale

    def on_click(self):
        self.state = not self.state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print(value)
        if value:
            self.icon = f"../icons/checkbox.png"
            self.icon.visible = True
        else:
            self.icon.visible = False


if __name__ == '__main__':
    from ursina import *

    app = Ursina()
    CheckBox(scale=.1)
    # Slider(y=-.1)
    app.run()
