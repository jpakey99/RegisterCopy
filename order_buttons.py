from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import json


class MenuButtons(Button):
    blue = 'background_images/blue_background.png'
    gray = 'background_images/gray_background.png'
    green = 'background_images/green_background.png'
    red = 'background_images/red_background.png'
    yellow = 'background_images/yellow_background.png'

    def __init__(self, button_info, **kwargs):
        super().__init__(**kwargs)
        print(button_info)
        color = button_info[2]
        self.return_value = button_info[3]
        self.text = button_info[0]
        if color == 'blue':
            self.background_down = self.blue
            self.background_normal = self.blue
        elif color == 'red':
            self.background_down = self.red
            self.background_normal = self.red
        elif color == 'gray':
            self.background_down = self.gray
            self.background_normal = self.gray
        elif color == 'green':
            self.background_down = self.green
            self.background_normal = self.green
        elif color == 'yellow':
            self.background_down = self.yellow
            self.background_normal = self.yellow

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            return self.text, self.return_value
        return None


class SelectionButtons(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .4
        self.rows, self.cols = 10,4
        with open('layouts/pretzel_tab.json') as file:
            self.json_file = json.load(file)
        self.layouts, self.layout = [], 0
        for layout in self.json_file.keys():
            self.layouts.append(layout)
        self.layout = self.layouts[0]
        for button in self.json_file[self.layout]:
            self.add_widget(MenuButtons(button))

    def on_touch_up(self, touch):
        for child in self.children:
            tres = child.on_touch_up(touch)
            if tres is not None:
                res = tres[1]
                if isinstance(res, str) and 'tab' in res:
                    index = int(res.split('_')[1]) - 1
                    print(index, self.layouts)
                    self.layout = self.layouts[index]
                    self.change_layout()
                else:
                    return tres

    def change_layout(self):
        self.clear_widgets()
        for button in self.json_file[self.layout]:
            self.add_widget(MenuButtons(button))