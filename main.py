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
        self.genres = self.data["genres"]
        
        # Make the 3 buttons
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
        
        # Image
        self.movie_image = Image(source = self.data["name"]+ ".jpg")
        h_layout.add_widget(self.movie_image)
        
        like_button = Button(
            text = ":)", font_size = 30, background_color = "green",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        like_button.bind(on_press=self.callback)
        h_layout.add_widget(like_button)
        main_layout.add_widget(h_layout)

                
        # Add Name and Bio
        self.movie_name = Label(text=self.data["name"])
        main_layout.add_widget(self.movie_name)

        self.movie_bio = Label(text=self.data["bio"])
        main_layout.add_widget(self.movie_bio)
        
        return main_layout

        
    def callback(self, instance=None):
        
        # Get a random data again
        self.data = movie_generator.get_single_item()
        
        # Change the details of movie
        self.movie_image.source = self.data["name"] + ".jpg"
        self.movie_bio.text = self.data["bio"]
        self.movie_name.text = self.data["name"]
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
    