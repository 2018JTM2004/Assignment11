import kivy,pymysql
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup 
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition,SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
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
class CustomPopup(Popup):
    pass

class SampleBoxLayout(BoxLayout):
    checkbox_is_active = ObjectProperty(False)
    def checkbox_18_clicked(self,instance,value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox is unchecked")
class LoginWindow(Screen):
    def verify_credentials(self):
        statement = f"select password from login_details where entry_no='{self.ids['entry_no'].text}'"
        cursor.execute(statement)
        marks = cursor.fetchall()
        print(marks)
        if marks !=():
            if self.ids["password"].text == marks[0][0]:
                self.manager.current = "studenthomepage"
            else:
                wrongpassword = Popup(title = 'Oops Something went wrong!',content = Label(text= "Please check your password!"),size_hint = (None,None),size = (400,100))
                wrongpassword.open()
        else:
            wrongcre = Popup(title = 'Oops Something went wrong!',content = Label(text= "Please check your login credentials!"),size_hint = (None,None),size = (400,100))
            wrongcre.open()
    def goback(self):
        self.ids["password"].text = ""
        self.ids["entry_no"].text = ""
        self.manager.current = "mainscreen"
        
class StudentHomePage(Screen):
    
    def validate_marks(self):
        statement = f"select * from student_marks where entry_no ='{self.ids['entry_no'].text}'"
#         print(statement)
        cursor.execute(statement)
        marks = cursor.fetchall()
#         print(marks)
#         desc = cursor.description
#         print(desc)
        popup1 = Popup(title = 'Oops Something went wrong!',content = Label(text= "Please check your entry number!"),size_hint = (None,None),size = (400,100))
        popup2 = Popup(title = 'Wow! You remember your entry number!',content = Label(text= "Valid Entry Number."),size_hint = (None,None),size = (400,100)) 
#         popup1.bind(on_press = popup1.dismiss())
#         popup2.bind(on_press = popup2.dismiss())
        if marks == ():
            popup1.open()
            self.ids["entry_no"].text = ""
        else:
            popup2.open()
            
    def checkbox_clicked1(self,instance,value):
        if value is True:
            statement = f"select ell711 from student_marks where entry_no ='{self.ids['entry_no'].text}'"
            cursor.execute(statement)
            marks = cursor.fetchall()
            self.ids["ell711"].text = str(marks[0][0])
        else:
            self.ids["ell711"].text = ""
    def checkbox_clicked2(self,instance,value):
        if value is True:
            statement = f"select ell712 from student_marks where entry_no ='{self.ids['entry_no'].text}'"
            cursor.execute(statement)
            marks = cursor.fetchall()
            self.ids["ell712"].text = str(marks[0][0])
        else:
            self.ids["ell712"].text = ""
    def checkbox_clicked3(self,instance,value):
        if value is True:
            statement = f"select ell785 from student_marks where entry_no ='{self.ids['entry_no'].text}'"
            cursor.execute(statement)
            marks = cursor.fetchall()
            self.ids["ell785"].text = str(marks[0][0])
        else:
            self.ids["ell785"].text = ""
    def checkbox_clicked4(self,instance,value):
        if value is True:
            statement = f"select ell718 from student_marks where entry_no ='{self.ids['entry_no'].text}'"
            cursor.execute(statement)
            marks = cursor.fetchall()
            self.ids["ell718"].text = str(marks[0][0])
        else:
            self.ids["ell718"].text = ""
    def checkbox_clicked5(self,instance,value):
        if value is True:
            statement = f"select ell818 from student_marks where entry_no ='{self.ids['entry_no'].text}'"
            cursor.execute(statement)
            marks = cursor.fetchall()
            self.ids["ell818"].text = str(marks[0][0])
        else:
            self.ids["ell818"].text = ""

    def go_back(self):
        self.manager.current = "loginwindow"
    def submit_details(self):
        statement = f"delete from student_info where entry_no='{self.ids['entry_no'].text}'"
        cursor.execute(statement)
#         details = cursor.fetchall()
#         print("No here")
#         print(deta)
        statement = f"insert into student_info (entry_no,name,department,\
                        email_address,contact_no,address,ell711,ell712,ell785,\
                        ell718,ell818) values ('{self.ids['entry_no'].text}',\
                        '{self.ids['name'].text}','{self.ids['department'].text}',\
                        '{self.ids['email_address'].text}',{int(self.ids['contact_no'].text)},\
                        '{self.ids['address1'].text+self.ids['address2'].text}',{self.ids['ell711'].text},\
                        {(self.ids['ell712'].text)},{self.ids['ell785'].text},\
                        {self.ids['ell718'].text},{self.ids['ell818'].text})"
        cursor.execute(statement)
        database.commit()
#             print(statement)            
#         else:
#             print("here")
#             alreadyaentry = Popup(title = 'Oops Something went wrong!',content = Label(text= "There is already an entry with provided entry number!"),size_hint = (None,None),size = (400,100))
#             alreadyaentry.open()

class ScreenManagement(ScreenManager):
    pass
class CheckBox(ToggleButton):
    pass
class AdminHomePage(Screen):
    pass
class ViewStudentDetails(Screen):
    def fetch_marks(self):
        statement = f"select * from student_info where entry_no ='{self.ids['entry_no'].text}'"
#         print(statement)
        cursor.execute(statement)
        marks = cursor.fetchall()
        print(marks)
        self.ids["name"].text = str(marks[0][1])
        self.ids["department"].text = str(marks[0][2])
        self.ids["email_address"].text = str(marks[0][3])
        self.ids["contact_no"].text = str(marks[0][4])
        self.ids["address"].text = str(marks[0][5])
        self.ids["ell711"].text = str(marks[0][6])
        self.ids["ell712"].text = str(marks[0][7])
        self.ids["ell785"].text = str(marks[0][8])
        self.ids["ell718"].text = str(marks[0][9])
        self.ids["ell818"].text = str(marks[0][10])
         
    
        
class DetailedAnalysis(Screen):
    pass

class Top5Students(Screen):
    pass

presentation = Builder.load_file("imsv2.kv")

class ImsApp(App):
    def build(self):
        return presentation


ImsApp().run()