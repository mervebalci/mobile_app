from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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


# RootWidget has to inherit from ScreenManager
class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        print(uname, pword)


class MainApp(App):
    def build(self):
        return RootWidget()
        # Make sure to return the OBJECT not the CLASS !!!


if __name__ == "__main__":
    MainApp().run()


"""The highest in hierarchy is the APP object (line29).
Then comes the ScreenManager (line22) which is represented by RootWidget.
And then comes Screen (line9) which is represented by LoginScreen"""