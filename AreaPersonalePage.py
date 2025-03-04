from kivy.uix.screenmanager import  Screen, SlideTransition
from kivy.properties import StringProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.animation import Animation

flagSaveRegion=0

import MainPage
tipo_errori=0

class AreaPersonalePage(Screen):
    nome=StringProperty('aa')
    pos_cinghiale = NumericProperty(0.5)
    pos_penna= NumericProperty(1.4)
    done_animation=0
    old_indice = 0

    def on_pre_enter(self, *args):
        try:
            from MainPage import name,indice,regione
            self.old_indice=0
            self.nome=str(name)

            if indice==1:
                self.pos_cinghiale=0.5
                self.pos_penna = 1.4
                self.ids.cinghiale.color = .99, .43, .23, 1
                self.ids.penna.color = .2,.3,.23,1
                name='cinghiale'
            elif indice==2:
                self.pos_cinghiale = -1.4
                self.pos_penna = 0.5
                self.ids.penna.color = .99, .43, .23, 1
                self.ids.cinghiale.color = .2,.3,.23,1
                name='penna'
            score=self.read_score(name,regione)
            self.ids.score.n_quiz=f'{score[0]}'
            self.ids.score.perc_passati=f'{score[1]}%'
            self.write_errori(indice)
        except:
            pass

    def write_indice(self):
        from MainPage import indice,regione

        store = JsonStore('credential.json')

        if indice==1:
            self.ids.cinghiale.color = .99, .43, .23, 1
            self.ids.penna.color = .2,.3,.23,1
            name='cinghiale'
        elif indice==2:
            self.ids.penna.color = .99, .43, .23, 1
            self.ids.cinghiale.color = .2,.3,.23,1
            name='penna'
        score=self.read_score(name,regione)
        self.ids.score.n_quiz=f'{score[0]}'
        self.ids.score.perc_passati=f'{score[1]}%'
        tmp_nome=self.ids.modifyname.text
        if tmp_nome != '':
            store.put('user', name=tmp_nome, type=indice)
        else:
            store.put('user', name=MainPage.name, type=indice)

    def write_errori(self,indice):
        from MainPage import regione
        self.scrollview = self.ids.grid_error
        self.remove_all_error()

        if indice==1:
            if regione==0:
                try:
                    self.add_error(4,indice)
                except:
                    pass
            elif regione==1:
                try:
                    self.add_error(0,indice)

                except:
                    pass

        elif indice==2:
            if regione==0 and indice!=self.old_indice:
                self.add_error(5, indice)

            elif regione==1 and indice!=self.old_indice:
                self.add_error(6, indice)



        ##if indice==1:
        ##    try:
        ##        self.scrollview.remove_widget(self.btn5)
        ##    except:
        ##        pass
        ##elif indice==2 and indice!=self.old_indice:
        ##    self.btn5 = TypeErrorCard()
        ##    self.btn5.index = 5
        ##    self.btn5.image = icone[5]
        ##    self.btn5.text = nome[5]
        ##    self.scrollview.add_widget(self.btn5)
        self.old_indice=indice

    def read_score(self,nome,regione):
        if regione==0:
            store = JsonStore('errori/Lombardia/Statistiche.json')
        elif regione==1:
            store = JsonStore('errori/Toscana/Statistiche.json')
        try:

            tot_quiz=store.get(nome)['tot_quiz']
            tot_promosso = store.get(nome)['perc_passate']
            tot_promosso = '%.1f'% tot_promosso
        except:
            tot_quiz=0
            tot_promosso=0
        return tot_quiz, tot_promosso

    def animate_it(self,index,indice_sel):
        MainPage.indice = indice_sel
        self.write_indice()
        if self.done_animation==0:
            animate = (
                Animation(pos_cinghiale=0.25,
                          pos_penna=0.75,
                          d=0.3)

            )
            animate.start(self)
            self.done_animation=1
        else:

            if index==1:
                self.ids.penna.color=.2,.3,.23,1
                self.ids.cinghiale.color =.99,.43,.23,1
                animate = (
                    Animation(pos_cinghiale=0.5,
                              pos_penna=1.4,
                              d=0.3)

                )
                animate.start(self)
                self.done_animation=0
            elif index==2:
                self.ids.cinghiale.color=.2,.3,.23,1
                self.ids.penna.color =.99,.43,.23,1
                animate = (
                    Animation(pos_cinghiale=-0.5,
                              pos_penna=0.5,
                              d=0.3)

                )
                animate.start(self)
                self.done_animation = 0
            self.write_errori(indice_sel)

    def on_pre_leave(self, *args):
        global flagSaveRegion
        flagSaveRegion=1
        ##print(flagSaveRegion)
        animate = (
            Animation(pos_cinghiale=0.5,
                      pos_penna=1.4,
                      d=0.3)

        )
        animate.start(self)
        self.done_animation = 0
        try:
            self.scrollview.remove_widget(self.btn5)
        except:
            pass
        store = JsonStore('credential.json')
        name=self.ids.modifyname.text
        if name != '':
            store.put('user', name=name, type=MainPage.indice)

    def remove_all_error(self):
        self.scrollview.clear_widgets()

    def add_error(self, num,indice):
        from MainPage import regione, nomi_cinghiale_Lombardia, nomi_penna_Lombardia, icone_cinghiale_Lombardia, icone_penna_Lombardia, nomi_cinghiale_Toscana, nomi_penna_Toscana, icone_cinghiale_Toscana, icone_penna_Toscana
        if indice==1:
            if regione==0:
                nome=nomi_cinghiale_Lombardia
                icone=icone_cinghiale_Lombardia
            elif regione==1:
                nome = nomi_cinghiale_Toscana
                icone = icone_cinghiale_Toscana
        elif indice==2:
            if regione==0:
                nome=nomi_penna_Lombardia
                icone=icone_penna_Lombardia
            elif regione == 1:
                nome=nomi_penna_Toscana
                icone=icone_penna_Toscana
        if num>0:
            for x in range (1,num+1):
                btn = TypeErrorCard()
                btn.index = x
                ##btn.image = icone[x]
                btn.text = nome[x]
                self.scrollview.add_widget(btn)
        else:
            btn = TypeErrorCard()
            btn.index = 0
            ##self.btn[1].image = icone[1]
            btn.text = nome[0]
            self.scrollview.add_widget(btn)

class TypeErrorCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_release(self):
        global tipo_errori
        tipo_errori=self.index
        App.get_running_app().root.transition=SlideTransition(direction='left')
        App.get_running_app().root.current ='storico'

