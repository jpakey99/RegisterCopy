import json

import kivy, datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import *
from header import Header


class MainSelectionScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = .9
        self.receipt_preview = ReceiptPreview()
        self.add_widget(self.receipt_preview)
        self.middle_column = MiddleColumn()
        self.add_widget(self.middle_column)
        self.order_buttons = SelectionButtons()
        self.add_widget(self.order_buttons)


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
            return self.return_value
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
            res = child.on_touch_up(touch)
            if res is not None:
                if 'tab' in res:
                    index = int(res.split('_')[1]) - 1
                    print(index, self.layouts)
                    self.layout = self.layouts[index]
                    self.change_layout()

    def change_layout(self):
        self.clear_widgets()
        for button in self.json_file[self.layout]:
            self.add_widget(MenuButtons(button))


class TransactionTotal(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = .3
        self.total = BoxLayout(orientation='vertical')
        self.change = BoxLayout(orientation='vertical')
        self.total.add_widget(Label(text="TOTAL"))
        self.transaction_total = Label(text="0.00")
        self.total.add_widget(self.transaction_total)
        self.change.add_widget(Label(text="CHANGE"))
        self.change_total = Label(text="0.00")
        self.change.add_widget(self.change_total)
        self.add_widget(self.total)
        self.add_widget(self.change)


class ItemsList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


class ReceiptPreview(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .4
        self.orientation = 'vertical'
        self.transaction_total = TransactionTotal()
        self.add_widget(ItemsList())
        self.add_widget(self.transaction_total)


class OrderButtons(Button):
    blue = 'background_images/blue_background.png'
    gray = 'background_images/gray_background.png'
    green = 'background_images/green_background.png'
    red = 'background_images/red_background.png'
    yellow = 'background_images/yellow_background.png'

    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
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


class MiddleColumn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .1
        self.orientation = 'vertical'
        with open('layouts/main_order_button_layout.json') as file:
            self.json_file = json.load(file)
        for button in self.json_file:
            self.add_widget(OrderButtons(button[2], text= button[0]))


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.header = Header()
        self.add_widget(self.header)
        self.add_widget(MainSelectionScreen())

    def update(self, _):
        self.header.update()


class RegisterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        tw_app = MainScreen()
        # tw_app.start_app()
        Clock.schedule_interval(tw_app.update, 1/30)
        return tw_app


if __name__ == '__main__':
    RegisterApp().run()