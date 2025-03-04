from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivy.animation import Animation
import MainPage
type = 0

class ChooseMDCard(MDCard):
    increment = NumericProperty(0)
    def change_bg(self):
        self.color = .99,.43,.23,1

    def select(self,index):
        global type
        type = index
        App.get_running_app().root.transition=SlideTransition(direction='right')
        App.get_running_app().root.current ='domande'



class ChooseMDCardNoImage(MDCard):
    def change_bg(self):
        self.color = .99,.43,.23,1
    def select(self,index):
        global type
        type = index


class ElementCard(MDCard):
    def change_bg(self):
        self.md_bg_color = .99, .43, .23, 1

    def change_page(self,index):
        global type
        type = index
        App.get_running_app().root.transition=SlideTransition(direction='left')
        App.get_running_app().root.current ='domande'



class ChoosePage(Screen):
    pos_argomento = NumericProperty(0.4)
    pos_completo= NumericProperty(0.6)
    pos_label= NumericProperty(0.77)
    opacity_comlpeto = NumericProperty(1)
    pos_grid = NumericProperty(0)
    opacity_grid = NumericProperty(0)

    def on_pre_enter(self, *args):
        from MainPage import indice,regione



        if indice==1:
            from MainPage import icone_cinghiale,nomi_cinghiale
            tmp_icone=icone_cinghiale[regione]
            tmp_nomi=nomi_cinghiale[regione]
            self.ids.image.image= f'icone/cinghiale.png'

            if regione!=1:
                self.ids.uno.image = tmp_icone[1]
                self.ids.uno.text = tmp_nomi[1]

                self.ids.due.image = tmp_icone[2]
                self.ids.due.text = tmp_nomi[2]

                self.ids.tre.image = tmp_icone[3]
                self.ids.tre.text = tmp_nomi[3]

                self.ids.quattro.image = tmp_icone[4]
                self.ids.quattro.text = tmp_nomi[4]
            elif regione==1:
                try:
                    self.remove_widget(self.ids.argomento)
                except:
                    pass
                try:
                    self.remove_widget(self.ids.grid)
                except:
                    pass
        elif indice==2:
            from MainPage import icone_penna,nomi_penna
            tmp_icone = icone_penna[regione]
            tmp_nomi = nomi_penna[regione]
            self.ids.image.image = 'icone/penna.png'

            self.ids.uno.image = tmp_icone[1]
            self.ids.uno.text = tmp_nomi[1]

            self.ids.due.image = tmp_icone[2]
            self.ids.due.text = tmp_nomi[2]

            self.ids.tre.image = tmp_icone[3]
            self.ids.tre.text = tmp_nomi[3]

            self.ids.quattro.image = tmp_icone[4]
            self.ids.quattro.text = tmp_nomi[4]

            self.add1=ElementCard()
            self.add1.index=5
            self.add1.image = tmp_icone[5]
            self.add1.text = tmp_nomi[5]
            self.ids.grid.add_widget(self.add1)
            if regione==1:
                self.add2 = ElementCard()
                self.add2.index = 6
                self.add2.image = tmp_icone[6]
                self.add2.text = tmp_nomi[6]
                self.ids.grid.add_widget(self.add2)


    def on_enter(self, *args):
        self.parent.transition = SlideTransition(direction='left')
    def on_touch_up(self, touch):

        try:
            self.ids.completo.color = .2, .3, .23, 1
            self.ids.uno.md_bg_color = .2, .3, .23, 1
            self.ids.due.md_bg_color = .2, .3, .23, 1
            self.ids.tre.md_bg_color = .2, .3, .23, 1
            self.ids.quattro.md_bg_color = .2, .3, .23, 1
            self.ids.argomento.color = .2, .3, .23, 1
            self.natura.md_bg_color = .2,.3,.23,1
            self.add2.md_bg_color = .2,.3,.23,1
        except:
            pass

    def animate_it(self):
        try:
            self.ids.argomento.color = .99, .43, .23, 1
        except:
            pass
        animate = (
            Animation(pos_argomento=0.8,
                      pos_completo=1.3,
                      pos_label=1,
                      opacity_comlpeto=0,
                      pos_grid =0.6,
                      opacity_grid=1,
                      d=0.3)

        )
        animate.start(self)

    def on_touch_move(self, touch):
        global type
        tmp_touch_down = touch.oy -self.height/3
        if touch.y < tmp_touch_down and type ==99:

            animate = (
                Animation(pos_argomento=0.4,
                          pos_completo=0.6,
                          pos_label=0.77,
                          opacity_comlpeto=1,
                          pos_grid=0,
                          opacity_grid=0,
                          d=0.3)
            )
            animate.start(self)
            type=0
            self.ids.argomento.color = .2,.3,.23,1

    def on_leave(self, *args):
        from MainPage import indice,regione
        self.ids.completo.color =.2,.3,.23,1
        try:
            self.ids.argomento.color =.2,.3,.23,1
        except:
            pass
        animate = (
            Animation(pos_argomento=0.4,
                      pos_completo=0.6,
                      pos_label=0.77,
                      opacity_comlpeto=1,
                      pos_grid=0,
                      opacity_grid=0,
                      d=0.3)
        )
        animate.start(self)
        try:
            self.ids.grid.remove_widget(self.add1)

        except:
            pass
        try:
            self.ids.grid.remove_widget(self.add2)
        except:
            pass

        if regione==1 and indice ==1:
            try:
                self.add_widget(self.ids.argomento)
                self.add_widget(self.ids.grid)
            except:
                pass





