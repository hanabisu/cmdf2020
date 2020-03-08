from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from os import path
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
screenFolder = 'screens'

Builder.load_file(screenFolder+'/main_screen.kv')
Builder.load_file(screenFolder+'/first_step.kv')
Builder.load_file(screenFolder+'/enter_item.kv')
Builder.load_file(screenFolder+'/sml.kv')
Builder.load_file(screenFolder+'/spend_all.kv')
Builder.load_file(screenFolder+'/work_option.kv')
Builder.load_file(screenFolder+'/save_all.kv')
Builder.load_file(screenFolder+'/save_some.kv')
Builder.load_file(screenFolder+'/bank_account.kv')
Builder.load_file(screenFolder+'/ending.kv')

# Declare both screens
class MainScreen(Screen):
    pass

class EnterItemScreen(Screen):
    pass

class FirstStepScreen(Screen):
    pass

class SpendAllScreen(Screen):
    pass

class SixMonthLaterScreen(Screen):
    pass

class WorkingOptionScreen(Screen):
    pass

class SaveAllScreen(Screen):
    pass

class SaveSomeScreen(Screen):
    pass

class BankAccountScreen(Screen):
    pass

class EndingScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EnterItemScreen(name='enter_item'))
sm.add_widget(FirstStepScreen(name='first_step'))
sm.add_widget(SixMonthLaterScreen(name='sml'))
sm.add_widget(WorkingOptionScreen(name='work_option'))
sm.add_widget(SpendAllScreen(name='spend_all'))
sm.add_widget(SaveAllScreen(name='save_all'))
sm.add_widget(SaveSomeScreen(name='save_some'))
sm.add_widget(BankAccountScreen(name='bank_account'))
sm.add_widget(EndingScreen(name='ending'))


class InvestFemme(App):
    balance = 100
    itemName = ""

    def build(self):
        balance = 100
        return sm

    def getItemName(self):
        self.itemName = self.root.get_screen('enter_item').ids.txt_input.text
        print(self.itemName)
        sm.switch_to(FirstStepScreen(name='first_step'))

    def getSaveAmount(self):
        amount = self.root.get_screen('save_some').ids.txt_input.text
        print(amount)
        sm.switch_to(SixMonthLaterScreen(name='sml'))

    def printItemName(self):
        return self.itemName

if __name__ == '__main__':
    InvestFemme().run()