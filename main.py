def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a3():
    basic.show_icon(IconNames.SILLY)
    basic.show_icon(IconNames.SURPRISED)
input.on_button_pressed(Button.AB, on_button_pressed_a3)