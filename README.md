# Ursina More UI
More UI for Ursina Engine.

They are update very often.

# Installation

```git clone https://github.com/Creator754915/Ursina.More.UI.git```

# Documentation

### Messagebox(Entity)

## Models

## Maths

## UI
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

**.origin_z** = 0

### ClickPanel(Button)

**.scale** = (0.3, 0.5)

**.radius** = 0.01

**.color** = color.black66

**.visible** = False

**.position** = (999, 999)

**.key_control** = True *#Active control + **key_bind***

**.key_bind** = "right mouse"

**.button_text** = "Button1"

**.button2_text** = "Button2"

**.button3_text** = "Button3"

**.button4_text** = "Button4"

**.button5_text** =" Button5"

**.button6_text** = "Button6"

****kwargs**:

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

layout = Layout(side="LEFT", color=color.gray)

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


