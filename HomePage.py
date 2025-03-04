from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.card import MDCard
from kivy.storage.jsonstore import JsonStore
from kivy.app import App

import MainPage

class SelTypeCard(MDCard):
    ##app= App.get_running_app()
    def change_bg(self,index):
        self.color = .99,.43,.23,1


    def select(self,index):
        MainPage.indice = index

class HomePage(Screen):

    def on_touch_up(self, touch):
        global indice
        self.ids.card_cinghiale.color = .2,.3,.23,1
        self.ids.card_penna.color = .2,.3,.23,1


