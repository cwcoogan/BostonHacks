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
        
        # Build Values
        self.data = movie_generator.get_single_item()
        main_layout = BoxLayout(orientation = "vertical")
        self.preferences = {}
        self.movie_name = Label(text=self.data["name"])
        self.movie_bio = Label(text=self.data["bio"])
        self.movie_image = Image(source = self.data["name"])
        self.genres = self.data["genres"]

        # Make the 3 buttons
        super_like_button = Button(
            text = ":D", font_size = 30, background_color = "yellow",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        
        dislike_button = Button(
            text = ":(", font_size = 30, background_color = "red",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        
        like_button = Button(
            text = ":)", font_size = 30, background_color = "green",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        
        # Add Widgets to Screen
        # Image
        h_layout.add_widget(self.movie_image)
        
        # Like/Dislike Buttons
        super_like_button.bind(on_press=self.callback)
        main_layout.add_widget(super_like_button)
        
        dislike_button.bind(on_press=self.callback)
        h_layout.add_widget(dislike_button)
        
        like_button.bind(on_press=self.callback)
        h_layout.add_widget(like_button)

        # Add Name and Bio
        main_layout.add_widget(self.movie_name)
        main_layout.add_widget(self.movie_bio)
        
        # Make the box layout
        h_layout = BoxLayout()
        main_layout.add_widget(h_layout)

        return main_layout

        
    def callback(self, instance=None):
        
        # Get a random data again
        self.data = movie_generator.get_single_item()
        
        # Change the details of movie
        self.food_image.source = self.data["name"]
        self.food_bio.text = self.data["bio"]
        self.food_name.text = self.data["name"]
        self.genres = self.data["genres"]
        
        # Check Choice and update preferences
        if instance.text == ":)": 
            self.preferences = menu(self.genres, 'L')
            
        elif instance.text == ":(": 
            self.preferences = menu(self.genres, 'D')
            
        elif instance.text == ":D": 
            self.preferences = menu(self.genres, 'S')        

if __name__ == '__main__':
    app = MainApp()
    app.run()
    