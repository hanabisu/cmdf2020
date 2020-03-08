import os
import math
import random
from os import path

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
screenFolder = 'screens'
itemName = ""
itemCost = 0.0
balance = 0.0
savings = 99.0
workoptions = ""
amount = 99.0

inputErrorAmt = False
inputErrorText = False
for filename in os.listdir(screenFolder):
    with open(os.path.join(screenFolder, filename), encoding='utf8') as f:
        Builder.load_string(f.read())

class MainScreen(Screen):
    pass


class EnterItemScreen(Screen):
    global inputErrorAmt
    global inputErrorText

    def errorDisplay(self):
        if inputErrorAmt:
            self.ids.error_amt.text = "Please enter an amount"
        else:
            self.ids.error_amt.text = ""

        if inputErrorText:
            self.ids.error_text.text = "Please enter an item"
        else:
            self.ids.error_text.text = ""
    pass

class FirstStepScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstStepScreen, self).__init__(**kwargs)
        with self.canvas.before:
            global itemName
            global balance

            self.ids.item_name.text = itemName
            self.ids.balance.text = str(balance)
    pass


class SpendAllScreen(Screen):
    pass


class SixMonthLaterScreen(Screen):
    pass


class WorkingOptionScreen(Screen):

    def __init__(self, **kwargs):
        super(WorkingOptionScreen, self).__init__(**kwargs)
        with self.canvas.before:
            global savings
            saving_text = str(savings)
            self.ids.work_text.text = 'you have $' + saving_text + ' saved in your savings, do you want to work?'


class SaveSomeScreen(Screen):
    pass


class BankAccountScreen(Screen):
    pass

class InvestmentScreen(Screen):

    def __init__(self, **kwargs):
        super(InvestmentScreen, self).__init__(**kwargs)
        with self.canvas.before:
            global amount
            outcome = self.getOutcome(amount)
            earnings = outcome - amount
            earnings_text = str(abs(earnings))
            outcome_text = str(outcome)
            if earnings >= 0:
                self.ids.earning_text.text = 'You are lucky! You earned $' + earnings_text + ' !'
            else:
                self.ids.earning_text.text = 'Too bad! You lost $' + earnings_text + ' !'
            self.ids.outcome_text.text = 'Your current balance is $' + outcome_text + ' !'


    def getOutcome(self, p):
        outcome = int(p*(1+random.uniform(-1 , 1)))
        return outcome


class EndingScreen(Screen):
    def closeScreen(self):
        App.get_running_app().stop()
        Window.close()



# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EnterItemScreen(name='enter_item'))
sm.add_widget(FirstStepScreen(name='first_step'))
sm.add_widget(SixMonthLaterScreen(name='sml'))
sm.add_widget(WorkingOptionScreen(name='work_option'))
sm.add_widget(SpendAllScreen(name='spend_all'))
sm.add_widget(SaveSomeScreen(name='save_some'))
sm.add_widget(BankAccountScreen(name='bank_account'))
sm.add_widget(InvestmentScreen(name='investment'))
sm.add_widget(EndingScreen(name='ending'))


class InvestFemme(App):

    def build(self):
        return sm

    def getItemInfo(self):
        global itemName
        global itemCost
        global inputErrorText
        global inputErrorAmt
        global balance
        global savings

        itemName = self.root.get_screen('enter_item').ids.txt_input.text
        itemCostScreenVal = self.root.get_screen('enter_item').ids.amt_input.text

        if len(itemCostScreenVal) > 0 and len(itemName) > 0:
            itemCost = float(itemCostScreenVal)
            balance = itemCost * 0.8
            sm.switch_to(FirstStepScreen(name='first_step'))
        else:
            if len(itemName) > 0:
                inputErrorText = False
            else:
                inputErrorText = True
            if len(itemCostScreenVal) > 0:
                inputErrorAmt = False
            else:
                inputErrorAmt = True

    def getSaveAmount(self):
        amount = self.root.get_screen('save_some').ids.txt_input.text
        print(amount)
        sm.switch_to(BankAccountScreen(name='bank_account'))


    def calculateInterest(self, p, n):
        r = 0.02
        return p * math.pow((1-r/n), n)


if __name__ == '__main__':
    InvestFemme().run()
