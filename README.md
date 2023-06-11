# Ursina More UI
More UI for Ursina Engine
They are update very often.

# Installation

```pip install https://github.com/Creator754915/ursina.more.ui.git```

# Example

### MessageBox

```py
from ursina import Ursina, Tooltip
from ursina.more.ui import MessageBox

app = Ursina()
messagebox = MessageBox(messagebox_name='My Messagebox', text='hello world!', scale=(.8, .5), color=color.azure, text_origin=(-.36, .18))
messagebox.tooltip = Tooltip("MessageBox")

app.run()
```

### RadioButton

```py
from ursina import Ursina, Slider
from ursina.more.ui import RadioButton
    
app = Ursina()

radiobutton = RadioButton(color=color.black33, scale=(.25, .25))

app.run()
```

### CheckBox

```py
from ursina import Ursina, Slider
from ursina.more.ui import CheckBox
    
app = Ursina()

checkbox = CheckBox(start_value=True, color=color.red, scale=.2)

app.run()
```
