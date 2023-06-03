# ursina.more.ui
More UI for Ursina Engine
They are update very often.

# Example

### MessageBox

```py
from ursina import Ursina, Tooltip

app = Ursina()
b = MessageBox(messagebox_name='My Messagebox', text='hello world!', scale=(.8, .5), color=color.azure, text_origin=(-.36, .18))
b.tooltip = Tooltip("MessageBox")

app.run()
```

### CheckButton

```py
from ursina import Ursina, Slider
    
app = Ursina()

test = CheckBox(start_value=True, color=color.red, scale=.2)

app.run()
```
