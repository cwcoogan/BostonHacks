from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

import api_methods

class MainApp(App):
    def build(self):
        self.icon = "food.png"
        self.data = api_methods.get_single_item()
        #self.operators = ["constructor elements go here"]
        #self.last_was_operator = None
        #self.last_button = None
        main_layout = BoxLayout(orientation = "vertical")

        super_like_button = Button(
            text = ":D", font_size = 30, background_color = "yellow",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        super_like_button.bind(on_press=self.on_super_like_button_press)
        main_layout.add_widget(super_like_button)

        h_layout = BoxLayout()
        dislike_button = Button(
            text = ":(", font_size = 30, background_color = "red",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        dislike_button.bind(on_press=self.on_dislike_button_press)
        h_layout.add_widget(dislike_button)
        self.food_image = Image(
            source = self.data["img_file"],
            width = 10000
        )
        h_layout.add_widget(self.food_image)
        like_button = Button(
            text = ":)", font_size = 30, background_color = "green",
            size_hint = (0.5, 0.25),
            pos = (50, 20),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}
        )
        like_button.bind(on_press=self.on_like_button_press)
        h_layout.add_widget(like_button)
        main_layout.add_widget(h_layout)
        
        self.food_name = Label(text=self.data["name"])
        main_layout.add_widget(self.food_name)
        self.food_bio = Label(text=self.data["bio"])
        main_layout.add_widget(self.food_bio)
        


        # self.solution = TextInput(background_color = "black", foreground_color = "white",
        #                           multiline=False, halign="right", font_size=40, readonly=True)
        # main_layout.add_widget(self.solution)
        # buttons = [
        #     ["7", "8", "9", "/"],
        #     ["4", "5", "6", "*"],
        #     ["1", "2", "3", "+"],
        #     [".", "0", "C", "-"],
        # ]
        # for row in buttons:
        #     h_layout = BoxLayout()
        #     for label in row:
        #         button = Button(
        #             text = label, font_size = 30, background_color = "white",
        #             pos_hint = {"center_x": 0.5, "centery_y": 0.5}
        #         )
        #         button.bind(on_press=self.on_button_press)
        #         h_layout.add_widget(button)
        #     main_layout.add_widget(h_layout)

        # equal_button = Button(
        #             text = "=", font_size = 30, background_color = "white",
        #             pos_hint = {"center_x": 0.5, "centery_y": 0.5}
        #         )
        # equal_button.bind(on_press=self.on_solution)
        # main_layout.add_widget(equal_button)

        return main_layout

    # def on_button_press(self, instance):
    #     current = self.solution.text # our screen
    #     button_text = instance.text

    #     if button_text == "C":
    #         self.solution.text = ""
    #     else:
    #         if current and (
    #             self.last_was_operator and button_text in self.operators):
    #             return
    #         elif current == "" and button_text in self.operators:
    #             return
    #         else:
    #             new_text = current + button_text
    #             self.solution.text = new_text
    #     self.last_button = button_text
    #     self.last_was_operator = self.last_button in self.operators


    def on_like_button_press(self, instance):
        pass # add the category to the liked list and update the self.food_image, name, bio

    def on_dislike_button_press(self, instance):
        pass # add the category to the disliked list and update the self.food_image, name, bio

    def on_super_like_button_press(self, instance):
        pass # add the category to the disliked list and update the self.food_image, name, bio


    # def on_solution(self, instance):
    #     text = self.solution.text
    #     if text:
    #         solution = str(eval(self.solution.text))
    #         self.solution.text = solution


if __name__ == '__main__':
    app = MainApp()
    app.run()