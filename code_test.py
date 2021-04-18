screen_height = 320
screen_width = 480

# ---------- Display Buttons ------------- #
# Default button styling:
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 80

# We want three buttons across the top of the screen
TAPS_HEIGHT = 40
TAPS_WIDTH = int(screen_width/3)
TAPS_Y = 0
 
# We want two big buttons at the bottom of the screen
BIG_BUTTON_HEIGHT = int(screen_height/3.2)
BIG_BUTTON_WIDTH = int(screen_width/2)
BIG_BUTTON_Y = int(screen_height-BIG_BUTTON_HEIGHT)

# This group will make it easy for us to read a button press later.
buttons = []
 
# Main User Interface Buttons
button_view1 = Button(x=0, y=0,
                      width=TAPS_WIDTH, height=TAPS_HEIGHT,
                      label="View1", label_font=font, label_color=0xff7e00,
                      fill_color=0x5c5b5c, outline_color=0x767676,
                      selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                      selected_label=0x525252)
buttons.append(button_view1)  # adding this button to the buttons group
 
button_view2 = Button(x=TAPS_WIDTH, y=0,
                      width=TAPS_WIDTH, height=TAPS_HEIGHT,
                      label="View2", label_font=font, label_color=0xff7e00,
                      fill_color=0x5c5b5c, outline_color=0x767676,
                      selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                      selected_label=0x525252)
buttons.append(button_view2)  # adding this button to the buttons group
 
button_view3 = Button(x=TAPS_WIDTH*2, y=0,
                      width=TAPS_WIDTH, height=TAPS_HEIGHT,
                      label="View3", label_font=font, label_color=0xff7e00,
                      fill_color=0x5c5b5c, outline_color=0x767676,
                      selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                      selected_label=0x525252)
buttons.append(button_view3)  # adding this button to the buttons group
 
button_switch = Button(x=0, y=BIG_BUTTON_Y,
                       width=BIG_BUTTON_WIDTH, height=BIG_BUTTON_HEIGHT,
                       label="Switch", label_font=font, label_color=0xff7e00,
                       fill_color=0x5c5b5c, outline_color=0x767676,
                       selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                       selected_label=0x525252)
buttons.append(button_switch)  # adding this button to the buttons group
 
button_2 = Button(x=BIG_BUTTON_WIDTH, y=BIG_BUTTON_Y,
                  width=BIG_BUTTON_WIDTH, height=BIG_BUTTON_HEIGHT,
                  label="Button", label_font=font, label_color=0xff7e00,
                  fill_color=0x5c5b5c, outline_color=0x767676,
                  selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                  selected_label=0x525252)
buttons.append(button_2)  # adding this button to the buttons group
 
# Add all of the main buttons to the spalsh Group
for b in buttons:
    splash.append(b.group)

    # Make a button to change the icon image on view2
button_icon = Button(x=150, y=60,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label="Icon", label_font=font, label_color=0xffffff,
                  fill_color=0x8900ff, outline_color=0xbc55fd,
                  selected_fill=0x5a5a5a, selected_outline=0xff6600,
                  selected_label=0x525252, style=Button.ROUNDRECT)
buttons.append(button_icon) # adding this button to the buttons group

# Add this button to view2 Group
view2.append(button_icon.group)

# Make a button to play a sound on view2
button_sound = Button(x=150, y=170,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label="Sound", label_font=font, label_color=0xffffff,
                  fill_color=0x8900ff, outline_color=0xbc55fd,
                  selected_fill=0x5a5a5a, selected_outline=0xff6600,
                  selected_label=0x525252, style=Button.ROUNDRECT)
buttons.append(button_sound) # adding this button to the buttons group

# Add this button to view2 Group
view3.append(button_sound.group)