from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob, random
from datetime import datetime
from pathlib import Path


# Builder is the connection between main.py and design.kv
Builder.load_file('design.kv')


# LoginScreen has to inherit from Screen
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        # Self is referring to the instance of this LoginScreen class.
        # LoginScreen is the class and self is the object that has been instantiated from this class, that has been created from this class.
        # Manager is the property of Screen.
        # Since this class is inheriting from Screen, so Screen is a parent and LoginScreen is a child.
        # And parent is giving the child all its methods, properties, attributes, including manager.
        # So self is able to access manager and manager has its own attribute which is current.
        # So current of manager and manager of LoginScreen. And this current attribute will get the name of the screen which is sign_up_screen.
        # This sign_up_screen in here, which is a widget that have been created in design.kv
    

    # Need to open to read json file where the users data are kept and check to see if that username and password are in that file.
    # If that username is in the file and it has a password, the password of the user is providing in the graphical user interface.
    def login(self, uname, pword):
        with open("users.json", 'r') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
           self.ids.wrong_login.text = "Wrong username or password!" 


# RootWidget has to inherit from ScreenManager
class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        # First open users.json as file, and get the users load in a dictionary. Now, IMPORT JSON here which is line4


        # Creating the format of json file
        # To see the date and time of creating, IMPORT DATETIME from datetime (line5)
        users[uname] = {'username': uname, 'password': pword, 
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        

        # To add the user info to json file, should use WRITE mode 'w' and DUMP the user's info (which is a dictionary) to the file.
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        # The movement to the next screen always goes towards the LEFT.
        # However, it is better to go towards RIGHT from the sign up successful page TO BACK to login page. And to do that:
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
    
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        
        # When click on Enlighten Me! button, to get ONLY the names of the txt files such as ['happy', 'sad', 'unloved'] 
        # instead of getting ['quotes\\happy.txt', 'quotes\\sad.txt', 'quotes\\unloved.txt']
        available_feelings = [Path(filename).stem for filename in available_feelings]
        
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try Another Feeling!"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()
        # Make sure to return the OBJECT not the CLASS !!!


if __name__ == "__main__":
    MainApp().run()


"""The highest in hierarchy is the APP object (line98).
Then comes the ScreenManager (line42) which is represented by RootWidget.
And then comes Screen (line17) which is represented by LoginScreen"""