from pynput import mouse
import json
from time import sleep


class Auditor:
    def __init__(self, script_name):
        self.script_name: str = script_name
        self.script: list = []
        self.listener()

    def save_script(self):
        with open(f'./scripts/{self.script_name}.json', 'w', encoding='utf-8') as f:
            json.dump(self.script, f, ensure_ascii=False, indent=4)
        print(f'Save to file: ./scripts/{self.script_name}.json')

    def listener(self):
        with mouse.Listener(
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()

    def on_click(self, x, y, button, press):
        self.script.append({
            "Set mouse position": {"x": x, "y": y},
            "Wait": 0.1
        })
        self.script.append({
            "Press mouse button": button.name,
            "Wait": 0.5
        })

        if len(self.script) > 20:
            self.save_script()

    def on_scroll(self, x, y, dx, dy):
        self.script.append({
            "Scroll": -1 if dy < 0 else 1,
            "Wait": 0.5
        })


test_class = Auditor('test')


# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:


# from pynput import keyboard
#
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#
# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
#
# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
