# Ursina More UI
More UI for Ursina Engine.

They are update very often.

# Installation

```git clone https://github.com/Creator754915/Ursina.More.UI.git```

# Documentation

### Messagebox(Entity)
**.messagebox_name** = 'My Messagebox'

**.text** = 'hello world!'

**.scale** = (.8, .5)

**.color** = color.azure

**.text_origin** = (-.36, .18)

### RadioButton(Button)
**.start_state** = False

**.state** = False

**.radius** = .5

**.scale** = (.25, .25)

**.color** = color.black33

**.origin_z** =0

## Examples

### MessageBox

```py
from ursina import *
from Ursina.More.UI import MessageBox

app = Ursina()
messagebox = MessageBox(messagebox_name='My Messagebox', text='hello world!', scale=(.8, .5), color=color.azure,
                        text_origin=(-.36, .18))
messagebox.tooltip = Tooltip("MessageBox")

app.run()
```

### RadioButton

```py
from ursina import *
from Ursina.More.UI import RadioButton
    
app = Ursina()

radiobutton = RadioButton(color=color.black33, scale=(.25, .25))

app.run()
```

### CheckBox

```py
from ursina import *
from Ursina.More.UI import CheckBox
    
app = Ursina()

checkbox = CheckBox(start_value=True, color=color.red, scale=.2)

app.run()
```

### Layout

```py
from ursina import *
from Ursina.More.UI import Layout
    
app = Ursina()

layout = Layout(side="lEFT", color=color.gray)

app.run()
```

### Background

```py
from ursina import *
from Ursina.More.UI import Background
app = Ursina()

Background(texture='sky_sunset')

app.run()

```

### ClickPanel

```py
from ursina import *
from Ursina.More.UI import ClickPanel
app = Ursina()

ClickPanel(key_control=False, key_bind="right mouse")

app.run()


