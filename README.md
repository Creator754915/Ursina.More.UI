# Ursina More UI
More UI for Ursina Engine.

They are update very often.

# Installation

```git clone https://github.com/Creator754915/Ursina.More.UI.git```

# Example

### MessageBox

```py
from ursina import Ursina, Tooltip
from Ursina.More.UI import MessageBox

app = Ursina()
messagebox = MessageBox(messagebox_name='My Messagebox', text='hello world!', scale=(.8, .5), color=color.azure, text_origin=(-.36, .18))
messagebox.tooltip = Tooltip("MessageBox")

app.run()
```

### RadioButton

```py
from ursina import Ursina, Slider
from Ursina.More.UI import RadioButton
    
app = Ursina()

radiobutton = RadioButton(color=color.black33, scale=(.25, .25))

app.run()
```

### CheckBox

```py
from ursina import Ursina, Slider
from Ursina.More.UI import CheckBox
    
app = Ursina()

checkbox = CheckBox(start_value=True, color=color.red, scale=.2)

app.run()
```

### Layout

```py
from ursina import Ursina, Slider
from Ursina.More.UI import Layout
    
app = Ursina()

layout = Layout(side="lEFT", color=color.gray)

app.run()
```
