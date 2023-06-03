from ursina import Button, Text, Quad, color


class CheckBox(Button):
    def __init__(self, start_state=False, **kwargs):
        super().__init__(start_state=start_state, state=start_state, scale=Text.size, model=Quad(radius=.25))
        self.default_model = None

        for key, value in kwargs.items():
            setattr(self, key, value)

        if 'color' in kwargs:
            setattr(self, 'color', kwargs['color'])
        self.highlight_color = self.color.tint(.2)
        self.pressed_color = self.color.tint(-.2)
        self.highlight_scale = 1  # multiplier
        self.pressed_scale = 1  # multiplier
        self.collider = 'box'

        if CheckBox.default_model is None:
            if not 'model' in kwargs:
                self.model = Quad(radius=.25)
        else:
            self.model = CheckBox.default_model

    def on_click(self):
        self.state = not self.state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print(value)
        self.text = f' X'[int(value)]


if __name__ == '__main__':
    from ursina import Ursina, Slider
    app = Ursina()
    test = CheckBox(model='sphere', start_value=True, color=color.red, scale=.2)
    Slider(y=-.1)
    app.run()