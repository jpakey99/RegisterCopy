import kivy, datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import *


class Header(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = .1
        self.far_left = BoxLayout(orientation = 'vertical')
        date = datetime.date.today()
        date_string = str(date.month) + ' ' + str(date.day) + ', ' + str(date.year)
        self.far_left.add_widget(Label(text='Date ' + date_string))
        self.far_left.add_widget(Label(text='Transactions: 0'))

        self.middle_left = BoxLayout(orientation = 'vertical')
        t = datetime.datetime.now()
        time_string = str(t.hour) + ':' + str(t.minute) + str(t.second)
        self.middle_left.add_widget(Label(text='Hi, John'))
        self.middle_left.add_widget(Label(text=time_string))

        self.add_widget(self.far_left)
        self.add_widget(self.middle_left)


class MainSelectionScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = .9
        self.add_widget(Label(text='Selection area'))


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Header())
        self.add_widget(MainSelectionScreen())

    def update(self, _):
        pass


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