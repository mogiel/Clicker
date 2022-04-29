"""module for automating tasks using external scripts. Single and multiple scripts"""
# system module
from json import load
from random import uniform
from time import sleep
from typing import TypedDict, Optional
# external module
from pynput.keyboard import Key, Controller as Controller_Keyboard
from pynput.mouse import Button, Controller as Controller_Mouse

# all keyboard key for validation
keyboard_keys = [e.name for e in Key]
# all mouse button for validation
mouse_button: list[str] = [e.name for e in Button]


class SetMouse(TypedDict):
    """Interface for set mouse position"""
    x: int
    y: int


class MoveMouse(TypedDict):
    """Interface for move mouse"""
    dx: int
    dy: int
    click: Optional[str]


class ScriptsRobot:
    """Automate your mouse and keyboard by passing action scripts from a json file"""
    def __init__(self, script_list: list[str]):
        """
        :param script_list: list of filenames with scripts
        :type script_list: [str,...]
        :rtype: object
        """
        self.script_list = script_list
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
            'Move mouse': self.move_mouse,
            'Press and move': self.press_and_move,
            'Scroll': self.scroll,
        }
        self.scripts = self.open_script()
        self.script_correct = True

    @staticmethod
    def valid_key(key: str):
        """validator if the key is correct

        :param: name of key
        :rtype: str
        """
        if key in keyboard_keys or len(key) == 1:
            return key
        return None

    @staticmethod
    def wait(wait: float = .25):
        """random stop script

        :type wait: float
        """
        sleep(uniform(0.75 * wait, 1.5 * wait))

    def script_stop(self):
        """script termination in case of error

        :rtype: bool"""
        self.script_correct = False

    def open_script(self):
        """opening a .json file with a script. write activities to the list

        :rtype: [object]"""
        script = []
        for script_name in self.script_list:
            with open(f'scripts/{script_name}.json', encoding='utf-8') as file:
                data = load(file)
                for entity in data:
                    for item in entity.items():
                        script.append(item)

        return script

    def pressed_keys(self, keys: list[str]):
        """pressing two keys

        :type keys: list[str]
        """
        first_key, second_key = keys
        try:
            first_key = self.valid_key(first_key)
            second_key = self.valid_key(second_key)
            key = getattr(Key, second_key) if len(second_key) > 1 else second_key
            with self.keyboard.pressed(getattr(Key, first_key, 'esc')):
                self.keyboard.press(key)
                self.keyboard.release(key)
        except TypeError:
            self.script_stop()
            print("Script error")

    def press_key(self, key: list[keyboard_keys] | str):
        """pressing one key"""
        try:
            new_key = getattr(Key, key) if len(key) > 1 else key
            self.keyboard.press(new_key)
            self.keyboard.release(new_key)
        except TypeError:
            self.script_stop()
            print("Script error")

    def set_text(self, text: str):
        """text introduction

        :type text: str
        """
        new_list = list(text)
        while new_list:
            self.keyboard.type(new_list.pop(0))
            self.wait(0.05)

    def set_mouse_position(self, coordinates: SetMouse):
        """set the position of the mouse

        :param coordinates: {"x": int, "y": int}
        :type coordinates: dict
        """
        self.mouse.position = (coordinates['x'], coordinates['y'])

    def press_mouse_button(self, click: mouse_button):
        """pressing the mouse button

        :param click: mou """
        self.mouse.press(getattr(Button, click, 'left'))
        self.mouse.release(getattr(Button, click, 'left'))

    def move_mouse(self, coordinates: MoveMouse):
        """move the mouse

        :param coordinates: {"dx": int, "dy": int}
        """
        self.mouse.move(coordinates['dx'], coordinates['dy'])

    def double_click_mouse_button(self, click: mouse_button):
        """double click the mouse

        :param click: mouse_button
        :return:
        """
        self.mouse.click(getattr(Button, click, 'left'), 2)

    def scroll(self, steps: int):
        """scroll mouse

        :type steps: int
        """
        self.mouse.scroll(0, steps)

    def press_and_move(self, action: MoveMouse):
        """press the button and move

        :param action: {"dx": int, "dy": int, "click": mouse_button}
        :type action: MoveMouse
        """
        self.mouse.press(getattr(Button, action['click'], 'left'))
        self.mouse.move(action['dx'], action['dy'])
        self.mouse.release(getattr(Button, action['click'], 'left'))

    def action(self):
        """run the script"""
        for script in self.scripts:
            if self.script_correct:
                self.action_mapper.get(script[0])(script[1])


if __name__ == "__main__":
    test_class = ScriptsRobot(["Open_Word"])
    test_class.action()
