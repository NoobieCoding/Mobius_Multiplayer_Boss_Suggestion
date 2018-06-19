from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.image import AsyncImage
from kivy.properties import ObjectProperty, StringProperty
import suggestion_system as suggest_sys


class UI(BoxLayout):

    selected_element = StringProperty('')
    selected_role = StringProperty('')
    input_area = ObjectProperty(None)
    result_area = ObjectProperty(None)
    elements = ('Fire', 'Water', 'Earth', 'Wind', 'Light', 'Dark')
    roles = ('Attacker', 'Breaker', 'Supporter', 'Defender')

    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        element_spinner = (Spinner(
                                text='Elements',
                                values=self.elements,
                                size_hint=(1, 0.7),
                                size=(150, 20),
                                color=(1, 0.5, 0.5, 1),
                                pos_hint={'center_x': .5, 'center_y': .45}))
        self.input_area.add_widget(element_spinner)
        element_spinner.bind(text=self.select_element)

        role_spinner = (Spinner(
                                text='Roles',
                                values=self.roles,
                                size_hint=(1, 0.7),
                                size=(150, 20),
                                color=(0.5, 1, 0.5, 1),
                                pos_hint={'center_x': .5, 'center_y': .45}))

        self.input_area.add_widget(role_spinner)
        role_spinner.bind(text=self.select_role)

    def select_element(self, spinner, text):
        self.selected_element = text
        print self.select_element

    def select_role(self, spinner, text):
        self.selected_role = text
        print self.selected_role

    def do_search(self):
        if self.selected_element == '' or self.selected_role == '':
            return
        self.result_area.clear_widgets()
        e = self.selected_element
        r = self.selected_role
        all_jobs_name = (suggest_sys.get_suggested_jobs_name(e, r))
        all_image_name = (suggest_sys.get_suggested_pic_name(e, r))
        # try:
        for i in range(0, len(all_image_name)):
            url = './resources/images/' + all_image_name[i]
            self.load_image(all_jobs_name[i], url)
            print url
        # except Exception:
        #         print 'No Match'

    def load_image(self, name, url):
        name = (Label(text=name,
                font_name="./resources/fonts/jp.otf",
                size_hint_y=None, height=0))
        gridlayout = GridLayout(orientation="vertical", pos=self.pos,
                                size_hint_y=None, height=550, cols=1,
                                spacing=0)
        gridlayout.add_widget(Label())
        gridlayout.add_widget(name)
        gridlayout.add_widget(AsyncImage(source=url,
                                         size_hint_y=None,
                                         height=500))
        self.result_area.add_widget(gridlayout)


class MobiusMPSuggestionApp(App):
    def build(self):
        ui = UI()
        return ui


if __name__ == '__main__':
    MobiusMPSuggestionApp().run()
