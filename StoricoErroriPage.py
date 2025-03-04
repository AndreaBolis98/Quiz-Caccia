from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.card import MDCard
from kivy.uix.gridlayout import GridLayout

jSon_Lombardia_cinghiale=['','errori/Lombardia/cinghiale/armi.json','errori/Lombardia/cinghiale/bioeco.json','errori/Lombardia/cinghiale/caccia.json','errori/Lombardia/cinghiale/malattie.json']
jSon_Lombardia_penna=['','errori/Lombardia/penna/armi.json','errori/Lombardia/penna/zoologia.json','errori/Lombardia/penna/venatoria.json','errori/Lombardia/penna/p_soccorso.json','errori/Lombardia/penna/p_natura.json']

jSon_Toscana_cinghiale=['errori/Toscana/cinghiale/generale.json']
jSon_Toscana_penna=['','errori/Toscana/penna/venatoria.json','errori/Toscana/penna/zoologia.json','errori/Toscana/penna/armi.json','errori/Toscana/penna/natura.json','errori/Toscana/penna/soccorso.json','errori/Toscana/penna/cinghiale.json']

jSon_Lombardia=['',jSon_Lombardia_cinghiale,jSon_Lombardia_penna]
jSon_Toscana=['',jSon_Toscana_cinghiale,jSon_Toscana_penna]

errori=[jSon_Lombardia,jSon_Toscana]


class StoricoErrori(Screen):
    card = list(range(0, 30))
    def on_pre_enter(self, *args):

        from AreaPersonalePage import tipo_errori
        from MainPage import indice, regione, nomi_penna_Lombardia,nomi_cinghiale_Lombardia,nomi_penna_Toscana,nomi_cinghiale_Toscana

        if indice==1:
            if regione==0:
                self.ids.indice_errori.text = f'{nomi_cinghiale_Lombardia[tipo_errori]}'
            elif regione==1:
                self.ids.indice_errori.text = f'{nomi_cinghiale_Toscana[tipo_errori]}'
        elif indice ==2:
            if regione==0:
                self.ids.indice_errori.text = f'{nomi_penna_Lombardia[tipo_errori]}'
            elif regione==1:
                self.ids.indice_errori.text = f'{nomi_penna_Toscana[tipo_errori]}'

        name=errori[regione][indice][tipo_errori]


        ##if indice ==1:
        ##    self.ids.indice_errori.text = f'{nomi_cinghiale_Lombardia[tipo_errori]}'
        ##    if tipo_errori==1:
        ##        name='errori/Lombardia/cinghiale/armi.json'
        ##    elif tipo_errori==2:
        ##        name='errori/Lombardia/cinghiale/bioeco.json'
        ##    elif tipo_errori==3:
        ##        name='errori/Lombardia/cinghiale/caccia.json'
        ##    elif tipo_errori==4:
        ##        name='errori/Lombardia/cinghiale/malattie.json'
        ##elif indice==2:
        ##    self.ids.indice_errori.text = f'{nomi_penna_Lombardia[tipo_errori]}'
        ##    if tipo_errori == 1:
        ##        name='errori/Lombardia/penna/armi.json'
        ##    elif tipo_errori == 2:
        ##        name='errori/Lombardia/penna/zoologia.json'
        ##    elif tipo_errori == 3:
        ##        name='errori/Lombardia/penna/venatoria.json'
        ##    elif tipo_errori == 4:
        ##        name='errori/Lombardia/penna/p_soccorso.json'
        ##    elif tipo_errori == 5:
        ##        name='errori/Lombardia/penna/p_natura.json'
        try:
            store=JsonStore(name)
            self.count = store.count()
            list=store.keys()
            self.scrollview = self.ids.error_armi_list
            if self.count<30:
                self.tmp_count=self.count
            else:
                self.tmp_count=30
            for i in range(0,self.tmp_count):
                tmp_card=ErrorCard()
                tmp_card=ErrorCard()
                tmp_card.domanda=store.get(list[self.count-1-i])['domanda']
                tmp_card.corretta=store.get(list[self.count-1-i])['corretta']
                tmp_card.risposta=store.get(list[self.count-1-i])['errata']
                self.card[i]=tmp_card
                self.scrollview.add_widget(self.card[i])
        except:
            print("err")
            pass

    def on_leave(self, *args):
        try:
            for i in range(0,self.tmp_count):
                self.scrollview.remove_widget(self.card[i])
        except:
            pass
        self.scrollview.scroll_x=0

class ErrorCard(GridLayout):
    pass