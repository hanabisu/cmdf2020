from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from os import path
from kivy.config import Config
from kivy.properties import StringProperty
import os

import math

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
screenFolder = 'screens'
balance = StringProperty("100")
savings = ""
itemName = ""
itemCost = 0.0
inputErrorAmt = False
inputErrorText = False
for filename in os.listdir("./" + screenFolder):
    Builder.load_file(os.path.join(screenFolder, filename))




# Declare both screens
class MainScreen(Screen):
    global balance
    balanceScreen = balance


class EnterItemScreen(Screen):

    global item
    item = TextInput(multiline = False).text

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



class FirstStepScreen(Screen):
    itemName = item
    print(itemName)


class SpendAllScreen(Screen):
    pass


class SixMonthLaterScreen(Screen):
    pass


class WorkingOptionScreen(Screen):
    global savings
    amount = StringProperty(savings)


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
    savings = ""

    def build(self):

        return sm

    def getItemName(self):
        item = self.root.get_screen('enter_item').ids.txt_input.text
        print(item)
        sm.switch_to(FirstStepScreen(name='first_step'))
    itemName = ""

    def build(self):
        return sm

    def getItemInfo(self):
        global itemName
        global itemCost
        global inputErrorText
        global inputErrorAmt
        itemName = self.root.get_screen('enter_item').ids.txt_input.text
        itemCostScreenVal = self.root.get_screen('enter_item').ids.amt_input.text
        if len(itemCostScreenVal) > 0 and len(itemName) > 0:
            sm.switch_to(FirstStepScreen(name='first_step'))
            itemCost = float(itemCostScreenVal)
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
        p = int(amount)
        print(p)
        n = 6
        result = (self.calculateInterest(p, n))
        savings = str(result)
        print(savings)
        sm.switch_to(SixMonthLaterScreen(name='sml'))

    def calculateInterest(self, p, n):
        r = 0.02
        return p*math.pow((1+r/n), n)



if __name__ == '__main__':
    InvestFemme().run()
