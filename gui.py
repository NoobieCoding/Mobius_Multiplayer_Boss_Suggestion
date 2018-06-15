from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


class UI(BoxLayout):

    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)


class MobiusMPSuggestionApp(App):
    def build(self):
        ui = UI()
        return ui


if __name__ == '__main__':
    MobiusMPSuggestionApp().run()
