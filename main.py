from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Builder is the connection between main.py and design.kv
Builder.load_file('design.kv')

# LoginScreen has to inherit from Screen
class LoginScreen(Screen):
    pass

# RootWidget has to inherit from ScreenManager
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
        # Make sure to return the OBJECT not the CLASS !!!

if __name__ == "__main__":
    MainApp().run()


"""The highest in hierarchy is the APP object (line16).
Then comes the ScreenManager (line13) which is represented by RootWidget.
And then comes Screen (line9) which is represented by LoginScreen"""