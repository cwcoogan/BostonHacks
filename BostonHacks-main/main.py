from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.window import Window

import movie_generator
import imdb_api
from menu import *

from twilio.rest import Client

account_sid = 'ACc054cafc9632fa3b8b64a3ceccae7e9d'
auth_token = '4548c4868a0a963ea8e3e4864aecb2d8'
client = Client(account_sid, auth_token)

class MainApp(App):
    def build(self):
                
        self.preferences = {}
        self.movies_dict = imdb_api.get_data(self.preferences)
        self.data = movie_generator.get_single_item(self.movies_dict)
        main_layout = BoxLayout(orientation = "vertical",)
        self.genres = self.data["genres"]
        self.id = self.data["id"]
        
        # Image
        self.movie_image = Image(
            source = self.data["name"]+ ".jpg"#,
            #keep_ratio = True,
            #width = 500,
            #height = 1100
            )
        main_layout.add_widget(self.movie_image)
        
        # Make the 3 buttons    
        h_layout = BoxLayout()
        dislike_button = Button(
            text = ":(", font_size = 24, background_color = "red",
            bold = True,
            #size_hint = (0.5, 0.8),
            #pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
            )
        dislike_button.bind(on_press=self.callback)
        h_layout.add_widget(dislike_button)
        
        super_like_button = Button(
            text = ":D", font_size = 24, background_color = "yellow",
            bold = True,
            #size_hint = (0.5, 0.8),
            #pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        super_like_button.bind(on_press=self.callback)
        h_layout.add_widget(super_like_button)
        
        like_button = Button(
            text = ":)", font_size = 24, background_color = "green",
            bold = True,
            #size_hint = (0.5, 0.8),
            #pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        like_button.bind(on_press=self.callback)
        h_layout.add_widget(like_button)
        main_layout.add_widget(h_layout)

                
        # Add Name and Bio
        self.movie_name = Label(
            text=self.data["name"],
            # color = "black",
            #size_hint_y = None,
            font_size = 24,
            bold = True
            )
        main_layout.add_widget(self.movie_name)

        self.movie_bio = Label(
            text='[i]'+self.data["bio"]+'[/i]',
            # color = "black",
            #size_hint_y = None,
            font_size = 16,
            markup = True
            )
        main_layout.add_widget(self.movie_bio)
        
        return main_layout

        
    def callback(self, instance=None):
        
        # Get a random data again
        self.data = movie_generator.get_single_item(self.movies_dict)
        
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
            message = client.messages.create(  
                              messaging_service_sid='MG0271c0c4f3007cdd3e6be50275e0655a', 
                              body='Hello, MyFlix here! Here is the full name of the movie you ' 
                              + 'super liked for easy access in case you want to stream it: :) \nmovie name: ' 
                              + self.movie_name.text + '. \nHappy movie watching!',      
                              to='+16099214505' 
                          )
            print(message.sid)

        
        print(self.preferences) 


if __name__ == '__main__':
    Window.size = (360, 740)
    # Window.clearcolor = (1, 1, 1, 1)
    app = MainApp()
    app.run()
    
    