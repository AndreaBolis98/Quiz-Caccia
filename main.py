import os
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Rectangle, RoundedRectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivymd.material_resources import STANDARD_INCREMENT
from kivymd.uix.button import MDIconButton, MDFloatingActionButton, MDTextButton
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.storage.jsonstore import JsonStore

from kivy.clock import Clock
import random
import threading
import time
import shutil

import MainPage
import ChooseRegion
import HomePage
import ChoosePage
import DomandePage
import PunteggioPage
import CorrezionePage
import AreaPersonalePage
import StoricoErroriPage


class MyApp(MDApp):
    def build(self):
        Window.size=(500 , 800)
        try:
            ##move Lombaridia chinghiale error
            if os.path.exists("c_armi.json"):
                shutil.move("c_armi.json","errori/Lombardia/cinghiale/armi.json")
            if os.path.exists("c_bioeco.json"):
                shutil.move("c_bioeco.json","errori/Lombardia/cinghiale/bioeco.json")
            if os.path.exists("c_caccia.json"):
                shutil.move("c_caccia.json","errori/Lombardia/cinghiale/caccia.json")
            if os.path.exists("c_malattie.json"):
                shutil.move("c_malattie.json","errori/Lombardia/cinghiale/malattie.json")

            ##move Lombaridia penna error
            if os.path.exists("p_armi.json"):
                shutil.move("p_armi.json", "errori/Lombardia/penna/armi.json")
            if os.path.exists("p_natura.json"):
                shutil.move("p_natura.json", "errori/Lombardia/penna/natura.json")
            if os.path.exists("p_soccorso.json"):
                shutil.move("p_soccorso.json", "errori/Lombardia/penna/soccorso.json")
            if os.path.exists("p_venatoria.json"):
                shutil.move("p_venatoria.json", "errori/Lombardia/penna/venatoria.json")
            if os.path.exists("p_zoologia.json"):
                shutil.move("p_zoologia.json", "errori/Lombardia/penna/zoologia.json")

            ##move Statistiche Lombardia
            if os.path.exists("Statistiche.json"):
                shutil.move("Statistiche.json", "errori/Lombardia/Statistiche.json")

            ##move Lombardia conghiale question
            if os.path.exists("testi/cinghiale"):
                shutil.move("testi/cinghiale", "testi/Lombardia")
            if os.path.exists("testi/penna"):
                shutil.move("testi/penna", "testi/Lombardia")
        except:
            pass


        Builder.load_file('MainPage.kv')
        Builder.load_file('ChooseRegion.kv')
        Builder.load_file('HomePage.kv')
        Builder.load_file('ChoosePage.kv')
        Builder.load_file('DomandePage.kv')
        Builder.load_file('PunteggioPage.kv')
        Builder.load_file('CorrezionePage.kv')
        Builder.load_file('AreaPersonalePage.kv')
        Builder.load_file('StoricoErroriPage.kv')
        store = JsonStore('credential.json')
        ##self.load()

        return Builder.load_file('KV.kv')

    def on_stop(self):
        store = JsonStore('credential.json')
        store.put('user', name=MainPage.name, type=MainPage.indice, regione=MainPage.regione)

myapp = MyApp()
myapp.run()
