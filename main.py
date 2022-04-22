import json
from random import uniform

from pynput.keyboard import Key, Controller
from time import sleep

print(uniform(0.1, 0.8))


# match key:
#     case 'alt': Key.alt;
#     case 'backspace': Key.backspace;
#     case 'cmd': Key.cmd
#     case 'ctrl': Key.ctrl
#     case 'delete': Key.delete
#     case 'down': Key.down
#     case 'end': Key.end
#     case 'enter': Key.enter
#     case 'esc': Key.esc
#     case 'f1': Key.f1
#     case 'f10': Key.f10
#     case 'f11': Key.f11
#     case 'f12': Key.f12
#     case 'f13': Key.f13
#     case 'f14': Key.f14
#     case 'f15': Key.f15
#     case 'f16': Key.f16
#     case 'f17': Key.f17
#     case 'f18': Key.f18
#     case 'f19': Key.f19
#     case 'f2': Key.f2
#     case 'f20': Key.f20
#     case 'f3': Key.f3
#     case 'f4': Key.f4
#     case 'f5': Key.f5
#     case 'f6': Key.f6
#     case 'f7': Key.f7
#     case 'f8': Key.f8
#     case 'f9': Key.f9
#     case 'home': Key.home
#     case 'insert': Key.insert
#     case 'left': Key.left
#     case 'menu': Key.menu
#     case 'pause': Key.pause
#     case 'right': Key.right
#     case 'shift': Key.shift
#     case 'space': Key.space
#     case 'tab': Key.tab;
#     case 'up': Key.up;


class ScriptsRobot:
    def __init__(self, script_name):
        self.script_name = script_name
        self.keyboard = Controller()

        self.script = self.open_script()

    def open_script(self):
        script = []
        with open(f'scripts/{self.script_name}.json') as file:
            data = json.load(file)
            for entity in data:
                for item in entity.items():
                    script.append(item)

        return script

    def pressed_keys(self, first_key, second_key):
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

    def wait(self, min_wait: float = .25, max_wait: float = 2):
        sleep(uniform(min_wait, max_wait))

#
# test_class = ScriptsRobot('Open_Word')
#
# test_class.pressed_keys('cmd', 'm')

# with keyboard.pressed(Key.cmd):
#     keyboard.press('s')
#     keyboard.release('s')
#
#
# sleep(1)
#
# keyboard.type('Google chrome')
# sleep(0.5)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# sleep(1)
# keyboard.type('unreal3')
# sleep(1)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# self.action_mapper = {
#     'Set mouse position': lambda a, b: a + b,
#     'Move mouse position': lambda a, b: a + b,
#     'Set wait': lambda a, b: a - b,
# }
