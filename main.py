from json import load
from pynput.keyboard import Key, Controller as Controller_Keyboard
from pynput.mouse import Button, Controller as Controller_Mouse
from random import uniform
from time import sleep

keys = [
    'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
    'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
    'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
    'insert', 'left', 'menu', 'pause', 'right', 'shift', 'space', 'tab', 'up'
]


class ScriptsRobot:
    def __init__(self, script_name):
        self.script_name = script_name
        self.keyboard = Controller_Keyboard()
        self.mouse = Controller_Mouse()
        self.action_mapper = {
            'Pressed': self.pressed_keys,
            'Press': self.press_key,
            'Set text': self.set_text,
            'Wait': self.wait,
            'Set mouse position': self.set_mouse_position,
            'Press mouse button': self.press_mouse_button,
            'Double click mouse button': self.double_click_mouse_button,
        }
        self.script = self.open_script()

    @staticmethod
    def valid_key(key):
        if key in keys:
            return True

    @staticmethod
    def wait(wait: float = .25):
        sleep(uniform(0.75 * wait, 1.5 * wait))

    def open_script(self):
        script = []
        with open(f'scripts/{self.script_name}.json') as file:
            data = load(file)
            for entity in data:
                for item in entity.items():
                    script.append(item)

        return script

    def pressed_keys(self, keys_list):
        first_key, second_key = keys_list
        key = getattr(Key, second_key) if len(second_key) > 1 else second_key
        with self.keyboard.pressed(getattr(Key, first_key, 'esc')):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def press_key(self, key):
        new_key = getattr(Key, key) if len(key) > 1 else key
        self.keyboard.press(new_key)
        self.keyboard.release(new_key)

    def set_text(self, text):
        self.keyboard.type(text)

    def set_mouse_position(self, coordinates):
        self.mouse.position = (coordinates['x'], coordinates['y'])

    def press_mouse_button(self, click):
        self.mouse.press(getattr(Button, click, 'left'))
        self.mouse.release(getattr(Button, click, 'left'))

    def double_click_mouse_button(self, click):
        self.mouse.click(getattr(Button, click, 'left'), 2)

    def action(self):
        for i in self.script:
            self.action_mapper.get(i[0])(i[1])


test_class = ScriptsRobot("Pajacyk")
test_class.action()
