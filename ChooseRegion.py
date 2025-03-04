from kivy.uix.screenmanager import  Screen, SlideTransition
from kivymd.uix.card import MDCard
from kivy.app import App
from kivy.storage.jsonstore import JsonStore

import MainPage

nomiRegioni=['Lombardia','Toscana']

class SelRegion(MDCard):


    def change_bg(self,index):
        self.color = .99,.43,.23,1

    def on_leave(self):
        self.color = .2,.3,.23,1

    def return_bg(self,index):
        import AreaPersonalePage
        MainPage.regione=index
        self.color = .95,.92,.85,1
        ##print(AreaPersonalePage.flagSaveRegion)
        if AreaPersonalePage.flagSaveRegion==0:
            App.get_running_app().root.transition = SlideTransition(direction='left')
            App.get_running_app().root.current = 'home'
        elif AreaPersonalePage.flagSaveRegion==1:
            App.get_running_app().root.transition = SlideTransition(direction='left')
            App.get_running_app().root.current = 'personale'

    ##def change_page(self):



class ChooseRegion(Screen):
    def on_kv_post(self, base_widget):
        for x in range(0,2):
            y=SelRegion()
            y.text=nomiRegioni[x]
            y.index=x
            if x==0:
                y.pos_hint={'center_x':.5,'center_y':.6}
            else:
                y.pos_hint = {'center_x': .5, 'center_y': .35}
            self.add_widget(y)




    pass