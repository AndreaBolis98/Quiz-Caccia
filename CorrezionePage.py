from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, NumericProperty

class CorrezionePage(Screen):
    domanda = StringProperty('')
    a = StringProperty('')
    b = StringProperty('')
    c = StringProperty('')
    r = StringProperty('')
    tipologies = StringProperty('')
    indice = StringProperty('')
    answare = StringProperty('')
    def on_enter(self, *args):
        from DomandePage import min,sec
        self.write_scrollview()
        if sec < 10:
            self.ids.count_down.text = f'{min}:0{sec}'
        else:
            self.ids.count_down.text = f'{min}:{sec}'
        self.write_domanda()

    def write_scrollview(self):
        from DomandePage import list_answer,MyScrollview,Tmp,NumericScrollView,n_domande
        self.card_num_review=list(range(0, n_domande))
        #self.card_num =list(range(0, n_domande))
        self.tmp_scrollview = MyScrollview()
        distanziale1=Tmp()
        distanziale2 = Tmp()
        self.tmp_scrollview.ids.numeric_list.add_widget(distanziale1)
        for n in range(n_domande):
            self.card_num_review[n]=NumericScrollView()

            if list_answer[n]==0:
                color=.894,.627,.0627,1
            elif list_answer[n]==1:
                color= .45,.51,.30,1
            elif list_answer[n]==2:
                color= .7,.3,.22,1
            self.card_num_review[n].color=color
            self.card_num_review[n].text=f'{n+1}'
            self.tmp_scrollview.ids.numeric_list.add_widget(self.card_num_review[n])

        self.tmp_scrollview.ids.numeric_list.add_widget(distanziale2)
        self.add_widget(self.tmp_scrollview)

    def write_domanda(self):
        from DomandePage import split
        domanda=split()
        self.ids.card_a.md_bg_color = .2,.3,.23,.3
        self.ids.card_b.md_bg_color = .2,.3,.23,.3
        self.ids.card_c.md_bg_color = .2,.3,.23,.3
        self.domanda = domanda[0]
        self.a = domanda[1]
        self.b = domanda[2]
        self.c = domanda[3]
        self.r = domanda[4]
        self.tipologies = domanda[8]
        self.indice = domanda[7]
        self.answare = domanda[6]
        if self.answare == 'a':
            self.ids.card_a.md_bg_color =.7,.3,.22,1
        elif self.answare == 'b':
            self.ids.card_b.md_bg_color =.7,.3,.22,1
        elif self.answare == 'c':
            self.ids.card_c.md_bg_color =.7,.3,.22,1

        if self.r == 'a':
            self.ids.card_a.md_bg_color =.45,.51,.30,1
        elif self.r == 'b':
            self.ids.card_b.md_bg_color =.45,.51,.30,1
        elif self.r == 'c':
            self.ids.card_c.md_bg_color =.45,.51,.30,1

    def on_leave(self, *args):
        self.remove_widget(self.tmp_scrollview)