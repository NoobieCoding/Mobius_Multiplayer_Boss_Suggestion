from kivy.app import App
from kivy.uix.widget import Widget


class UI(Widget):
    pass


class MobiusMPSuggestionApp(App):
    def build(self):
        ui = UI()
        return ui


if __name__ == '__main__':
    MobiusMPSuggestionApp().run()
