import kivy, datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HeaderSection(BoxLayout):
    def __init__(self, top, bottom, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.top_label = Label(text=top)
        self.bottom_label = Label(text=bottom)
        self.add_widget(self.top_label)
        self.add_widget(self.bottom_label)


class Header(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = .05
        date = datetime.date.today()
        date_string = str(date.month) + ' ' + str(date.day) + ', ' + str(date.year)
        self.far_left = HeaderSection('Date ' + date_string, 'Transactions: 0')

        t = datetime.datetime.now()
        time_string = str(t.hour) + ':' + str(t.minute)+ ":" + str(t.second)
        self.middle_left = HeaderSection('Hi, John', time_string)

        self.add_widget(self.far_left)
        self.add_widget(self.middle_left)

    def update(self):
        date = datetime.date.today()
        date_string = str(date.month) + ' ' + str(date.day) + ', ' + str(date.year)
        self.far_left.top_label.text = date_string

        t = datetime.datetime.now()
        time_string = str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)
        self.middle_left.bottom_label.text = time_string