from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


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


class Item(BoxLayout):
    def __init__(self, item, **kwargs):
        super().__init__(**kwargs)
        item_name, escape = '', False
        for letter in item[0]:
            if letter == '\n':
                item_name += ' '
            else:
                item_name += letter
        name = Label(size_hint_x = .7, text=item_name)
        price_per = Label(size_hint_x = .1, text=str(item[1]))
        quantity = Label(size_hint_x=.1, text=str(item[2]))
        total = Label(size_hint_x=.1, text=str(item[3]))
        self.add_widget(name)
        self.add_widget(price_per)
        self.add_widget(quantity)
        self.add_widget(total)


class ItemsList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

    def add_item(self, item):
        self.add_widget(Item(item))


class ReceiptPreview(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = .4
        self.orientation = 'vertical'
        self.transaction_total = TransactionTotal()
        self.item_list = ItemsList()
        self.add_widget(self.item_list)
        self.add_widget(self.transaction_total)

    def add_item(self, item):
        # item name, price per, quantity, total
        self.item_list.add_item(item)
        self.transaction_total.transaction_total.text = str(float(self.transaction_total.transaction_total.text) + item[3])