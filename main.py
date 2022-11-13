from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

import movie_generator
from menu import *

class MainApp(App):
    def build(self):
        self.data = movie_generator.get_single_item()
        main_layout = BoxLayout(orientation = "vertical")
        self.prefs = {}

        super_like_button = Button(
            text = ":D", font_size = 30, background_color = "yellow",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        super_like_button.bind(on_press=self.callback)
        main_layout.add_widget(super_like_button)

        h_layout = BoxLayout()
        dislike_button = Button(
            text = ":(", font_size = 30, background_color = "red",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        dislike_button.bind(on_press=self.callback)
        h_layout.add_widget(dislike_button)
        
        self.food_image = Image(
            source = self.data["name"],
        )
        h_layout.add_widget(self.food_image)

        like_button = Button(
            text = ":)", font_size = 30, background_color = "green",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        like_button.bind(on_press=self.callback)
        h_layout.add_widget(like_button)
        main_layout.add_widget(h_layout)
        
        self.food_name = Label(text=self.data["name"])
        main_layout.add_widget(self.food_name)
        self.food_bio = Label(text=self.data["bio"])
        main_layout.add_widget(self.food_bio)

        return main_layout


    def on_like_button_press(self, instance):
        self.prefs = menu(self.data["genres"], 'L')
        
        
    def callback(self, instance=None):
        self.data = movie_generator.get_single_item()
        self.food_image.source = self.data["name"]
        self.food_bio.text = self.data["bio"]
        self.food_name.text = self.data["name"]

    def on_dislike_button_press(self, instance):
        self.prefs = menu(self.data["genres"], 'D')

    def on_super_like_button_press(self, instance):
        self.prefs = menu(self.data["genres"], 'S')
            

if __name__ == '__main__':
    
    app = MainApp()
    app.run()
    