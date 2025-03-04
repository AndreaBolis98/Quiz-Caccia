from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock


## Lombardia ==0
## Toscana ==1

name= ''
regione=0
indice= 0

icone_penna_Lombardia=['icone/quiz.png','icone/proiettile.png','icone/zoologia.png','icone/legislazione.png','icone/medico.png','icone/catura.png']
icone_cinghiale_Lombardia=['icone/quiz.png','icone/proiettile.png','icone/ecologia.png','icone/sparo.png','icone/medico.png']

nomi_cinghiale_Lombardia=['completo','Armi e Munizioni','Biologia ed Ecologia','Caccia','Malattie']
nomi_penna_Lombardia = ['Completo','Armi e Munizioni','Zoologia','Legislatura Venatoria','Pronto Soccorso','Natura']
testi_cinghiale_Lombardia=['','testi/Lombardia/cinghiale/Armi.txt','testi/Lombardia/cinghiale/BioEco.txt','testi/Lombardia/cinghiale/Caccia.txt','testi/Lombardia/cinghiale/Malattie.txt']
testi_penna_Lombardia=['','testi/Lombardia/penna/Armi.txt','testi/Lombardia/penna/Zoologia.txt','testi/Lombardia/penna/LegislazioneVenatoria.txt','testi/Lombardia/penna/ProntoSoccorso.txt','testi/Lombardia/penna/Catura.txt']

icone_penna_Toscana=['icone/quiz.png','icone/legislazione.png','icone/zoologia.png','icone/proiettile.png','icone/catura.png','icone/medico.png','icone/cinghiale2.png']
icone_cinghiale_Toscana=['icone/quiz.png']

nomi_cinghiale_Toscana=['completo']
nomi_penna_Toscana = ['Completo','Legislatura Venatoria','Zoologia','Armi e Munizioni','Natura','Pronto Soccorso','Cinghiale in braccata']
testi_cinghiale_Toscana=['testi/Toscana/cinghiale/Cinghiale.txt']
testi_penna_Toscana=['','testi/Toscana/penna/LegislazioneVenatoria.txt','testi/Toscana/penna/Zoologia.txt','testi/Toscana/penna/Armi e muniuzioni.txt','testi/Toscana/penna/Catura.txt','testi/Toscana/penna/ProntoSoccorso.txt','testi/Toscana/penna/CinghialeBraccata.txt']

icone_penna=[icone_penna_Lombardia,icone_penna_Toscana]
icone_cinghiale=[icone_cinghiale_Lombardia,testi_cinghiale_Toscana]
nomi_penna=[nomi_penna_Lombardia,nomi_penna_Toscana]
nomi_cinghiale=[nomi_cinghiale_Lombardia,nomi_cinghiale_Toscana]
testi_penna=[testi_penna_Lombardia,testi_penna_Toscana]
testi_cinghiale=[testi_cinghiale_Lombardia,testi_cinghiale_Toscana]

class MainPage(Screen):
    def on_pre_enter(self, *args):
        global name, indice, regione
        store = JsonStore('credential.json')
        ##self.load()
        try:
            name = store.get('user')['name']
            if name !='' :
                Clock.schedule_once(self.change_screen)

        except:
            pass

    def change_screen(self, tmp):
        global name, indice, regione
        store = JsonStore('credential.json')
        try:
            indice = store.get('user')['type']
            regione = store.get('user')['regione']
            self.parent.transition = NoTransition()
            if indice > 0:
                self.parent.current = 'choose'
            else:
                pass
        except:
            pass

    def press_forward(self):
        global name
        tmp_name = self.ids.user.text
        if tmp_name != '':
            name = tmp_name
            self.parent.transition = SlideTransition(direction='left')
            self.parent.current = 'ChooseRegion'
