from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore


class PunteggioPage(Screen):
    risposte_corrette =0
    risposte_sbagliate=0
    risposte_non_date=0
    numero_domande=0
    indice=0

    def on_pre_enter(self, *args):
        from DomandePage import risp_non_date,risp_giuste,risp_sbagliate,n_domande,min,sec
        self.risposte_corrette=risp_giuste
        self.risposte_sbagliate=risp_sbagliate
        tmp_non_date=n_domande-(risp_sbagliate+risp_giuste)
        self.risposte_non_date=tmp_non_date
        self.numero_domande=n_domande
        self.store_error()
        print(tmp_non_date)
        esito= self.numero_domande-self.risposte_corrette
        if esito <=4:
            self.ids.esito.text='Promosso!'
        else:
            self.ids.esito.text = 'Bocciato'

        size_num = int((3.5 * Window.size[1] / 100) / 2)
        size_num_perc = int((3.5 * Window.size[1] / 100) / 2)
        size_bar=75*Window.size[0]/100

        #CORRETTE

        self.ids.num_corrette.text =f"CORRETTE  {self.risposte_corrette}/[size={size_num}]{self.numero_domande}[/size]"

        size_progress_bar_corrette= self.risposte_corrette*size_bar/self.numero_domande
        self.ids.corrette_bar.value= (size_progress_bar_corrette)
        perc_corrette=int((self.risposte_corrette*100)/self.numero_domande)
        self.ids.perc_corrette.text= f"{perc_corrette} [size={size_num_perc}]%[/size]"
        #ERRATE

        self.ids.num_errate.text =f"ERRATE  {self.risposte_sbagliate}/[size={size_num}]{self.numero_domande}[/size]"
        size_progress_bar_errate= self.risposte_sbagliate*size_bar/self.numero_domande
        self.ids.errate_bar.value= (size_progress_bar_errate)
        perc_errate=int((self.risposte_sbagliate*100)/self.numero_domande)
        self.ids.perc_errate.text= f"{perc_errate} [size={size_num_perc}]%[/size]"
        #NON DATE

        self.ids.num_non_date.text =f"NON DATE  {self.risposte_non_date}/[size={size_num}]{self.numero_domande}[/size]"
        size_progress_bar_non_date= self.risposte_non_date*size_bar/self.numero_domande
        self.ids.non_date_bar.value= (size_progress_bar_non_date)
        perc_non_date=int((self.risposte_non_date*100)/self.numero_domande)
        self.ids.perc_non_date.text= f"{perc_non_date} [size={size_num_perc}]%[/size]"

    def store_error(self):
        from DomandePage import domande_errate
        from MainPage import indice,regione
        self.indice=indice
        if regione==0:
            error_cinghiale_armi = JsonStore('errori/Lombardia/cinghiale/armi.json')  # tipologia=1
            error_cinghiale_bioEco = JsonStore('errori/Lombardia/cinghiale/bioeco.json')  # tipologia=2
            error_cinghiale_caccia = JsonStore('errori/Lombardia/cinghiale/caccia.json')  # tipologia=3
            error_cinghiale_malattie = JsonStore('errori/Lombardia/cinghiale/malattie.json')  # tipologia=4

            error_penna_armi = JsonStore('errori/Lombardia/penna/armi.json')  # tipologia=1
            error_penna_zoologia = JsonStore('errori/Lombardia/penna/zoologia.json')  # tipologia=1
            error_penna_soccorso = JsonStore('errori/Lombardia/penna/soccorso.json')  # tipologia=1
            error_penna_venatoria = JsonStore('errori/Lombardia/penna/venatoria.json')  # tipologia=1
            error_penna_natura = JsonStore('errori/Lombardia/penna/natura.json')  # tipologia=1
        elif regione ==1:
            error_cinghiale = JsonStore('errori/Toscana/cinghiale/generale.json')  # tipologia=1

            error_penna_armi = JsonStore('errori/Toscana/penna/armi.json')  # tipologia=1
            error_penna_zoologia = JsonStore('errori/Toscana/penna/zoologia.json')  # tipologia=1
            error_penna_soccorso = JsonStore('errori/Toscana/penna/soccorso.json')  # tipologia=1
            error_penna_venatoria = JsonStore('errori/Toscana/penna/venatoria.json')  # tipologia=1
            error_penna_natura = JsonStore('errori/Toscana/penna/natura.json')  # tipologia=1
            error_penna_cinghiale = JsonStore('errori/Toscana/penna/cinghiale.json')  # tipologia=1

        #Store Errori


        for i in range(1, 32):
            try:
                errori = domande_errate[i].split(';')
                name=f'{errori[0]}{errori[5]}'
                if regione==0:
                    if self.indice ==1:
                        if errori[4] =='1':
                            error_cinghiale_armi.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] =='2':
                            error_cinghiale_bioEco.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '3':
                            error_cinghiale_caccia.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '4':
                            error_cinghiale_malattie.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                    elif self.indice ==2:
                        if errori[4] =='1':
                            error_penna_armi.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] =='2':
                            error_penna_zoologia.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '3':
                            error_penna_soccorso.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '4':
                            error_penna_venatoria.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '5':
                            error_penna_natura.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                elif regione ==1:
                    if self.indice ==1:
                        error_cinghiale.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                    elif self.indice == 2:
                        if errori[4] =='1':
                            error_penna_venatoria.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] =='2':
                            error_penna_zoologia.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '3':
                            error_penna_armi.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '4':
                            error_penna_natura.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '5':
                            error_penna_soccorso.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
                        elif errori[4] == '6':
                            error_penna_cinghiale.put(name, domanda=errori[1], corretta=errori[2], errata=errori[3])
            except:
                    pass

    def on_touch_up(self, touch):
        self.ids.nuovo_quiz.color=.2,.3,.23,1
        self.ids.correzione.color=.2,.3,.23,1

