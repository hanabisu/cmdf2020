from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from os import path
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
    #sm.switch_to(screen3, direction='right', duration=1.)

class WorkingOptionScreen(Screen):
    pass



# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EnterItemScreen(name='enter_item'))
sm.add_widget(FirstStepScreen(name='first_step'))
sm.add_widget(SixMonthLaterScreen(name='sml'))
sm.add_widget(WorkingOptionScreen(name='work_option'))
sm.add_widget(SpendAllScreen(name='spend_all'))

class InvestFemme(App):

    def build(self):
        return sm

if __name__ == '__main__':
    InvestFemme().run()