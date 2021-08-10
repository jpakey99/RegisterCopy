import kivy, datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
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
        self.add_widget(Label(text='Selection area'))


class ReceiptPreview(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .4


class OrderButtons(Button):
    pass


class MiddleColumn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .1
        self.orientation = 'vertical'


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