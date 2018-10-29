import kivy,pymysql
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition,SlideTransition
# from kivy.uix.widget import Widget
# from kivy.graphics import Line

# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.label import Label

# Builder.load_file('path/to/file.kv')

database = pymysql.connect('localhost','root','mysql@3006','assignment11') #CONNECTION PARAMETERES
cursor = database.cursor()

class MainScreen(Screen):
    pass
    
class LoginWindow(Screen):
    def verify_credentials(self):
        statement = f"select password from login_details where entry_no='{self.ids['entry_no'].text}'"
        cursor.execute(statement)
#         print(cursor.fetchall()[0][0])
        if self.ids["password"].text == cursor.fetchall()[0][0]:
            self.manager.current = "userwindow"
    def goback(self):
        self.ids["password"].text = ""
        self.ids["entry_no"].text = ""
        self.manager.current = "mainwindow"
        
class UserWindow(Screen):
    def fetch_marks(self):
        pass
        

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("ims.kv")

class ImsApp(App):
    def build(self):
        return presentation


ImsApp().run()