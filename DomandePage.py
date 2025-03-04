import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import random
from MainPage import testi_penna_Lombardia,testi_cinghiale_Lombardia,testi_cinghiale_Toscana,testi_penna_Toscana
from kivy.storage.jsonstore import JsonStore

out_domande = list(range(0, 40))
domande_errate=list(range(1, 42))
n_domande =NumericProperty
n_domanda = NumericProperty
risp_giuste = 0
risp_non_date = 0
risp_sbagliate = 0
list_answer=list(range(0, 40))
min = NumericProperty(30)
sec = NumericProperty(0)
flag=0
class NumericScrollView(MDCard):
    pass


class MyScrollview(ScrollView):
    m = 0.0
    q = 0.0

    def on_kv_post(self, base_widget):
        self.bind(on_touch_down=self.start_Scroll)
        self.bind(on_scroll_stop=self.scroll)
        ##self.bind(on_scroll_stop=self.stop_scroll)

    def start_Scroll(self, t, a):
        self.do_scroll_x = True

    def scroll(self, t, a):
        global n_domanda
        global n_domande
        lim_inf = Window.size[1] * 0.865
        lim_sup = Window.size[1] * 0.06 + lim_inf
        if a.oy <= lim_sup and a.oy >= lim_inf:
            self.do_scroll_x = False
            if self.scroll_x <= 0:
                self.scroll_x = 0
            if self.scroll_x >= 1:
                self.scroll_x = 1
            self.m = ((1 - 0) / (n_domande - 1))
            self.q = 1 - self.m * n_domande
            tmp_domanda = (self.scroll_x - self.q) / self.m
            ##print(tmp_domanda)
            if tmp_domanda<1:
                tmp_domanda=1
            n_domanda = int(tmp_domanda)
            ##print(n_domanda)
            resto = tmp_domanda % n_domanda
            if resto <= 0.5:
                #print('min')
                pass
            elif resto < 1:
                #print('max')
                n_domanda = n_domanda + 1
            self.scroll_x = self.m * n_domanda + self.q
            if App.get_running_app().root.current== 'domande':
                domandepage= App.get_running_app().root.ids.domande_pagina
                domandepage.write_domanda()
            elif App.get_running_app().root.current =='correzione':
                correzionepage = App.get_running_app().root.ids.correzione_page
                correzionepage.write_domanda()
        #print(self.scroll_x)

    def stop_scroll(self, t, a):
        # self.do_scroll_x = False
        pass

class DomandePage(Screen):

    domanda = StringProperty('')
    a = StringProperty('')
    b = StringProperty('')
    c = StringProperty('')
    r = StringProperty('')
    tipologies = StringProperty('')
    indice = StringProperty('')
    answare = StringProperty('')
    antiripetizione=0

    def on_pre_enter(self):
        try:
            global n_domande
            global n_domanda
            global risp_giuste
            global risp_sbagliate
            global domande_errate
            global domande_errate_indice
            global min,sec
            from ChoosePage import type
            from MainPage import indice,regione ##cinghiale=1 o penna=2
            risp_giuste=0
            risp_sbagliate=0
            min= 30
            sec =0
            if regione ==0:
                if indice ==1 and type ==4:
                    n_domande=22
                else:
                    n_domande = 30
            elif regione ==1:
                ##print(indice)
                if type ==6:
                    n_domande = 24
                else:
                    n_domande = 40
            chooseQuestion(indice,type,n_domande,regione)
            n_domanda =1
            self.write_scrollview(n_domande)
            self.write_domanda()
            for i in range(1,30):
                domande_errate[i]=''
        except:
            pass

    def on_enter(self):
        Clock.schedule_interval(self.countdown, 1)

    def write_scrollview(self,n_domande):
        global list_answer
        self.card_num =list(range(0, n_domande))
        self.tmp_scrollview = MyScrollview()
        distanziale1=Tmp()
        distanziale2 = Tmp()
        self.tmp_scrollview.ids.numeric_list.add_widget(distanziale1)
        for n in range(n_domande):
            list_answer[n]=0
            self.card_num[n]=NumericScrollView()

            self.card_num[n].text=f'{n+1}'
            self.card_num[n].color=.95,.92,.85,1

            self.tmp_scrollview.ids.numeric_list.add_widget(self.card_num[n])


        self.tmp_scrollview.ids.numeric_list.add_widget(distanziale2)
        self.add_widget(self.tmp_scrollview)

    def on_pre_leave(self, *args):
        global n_domanda,flag
        Clock.unschedule(self.countdown)
        self.remove_widget(self.tmp_scrollview)
        n_domanda=1
        if flag==1:
            self.store_statistics()
        else:
            pass
        #print(flag)
        flag=0

    def countdown(self,tmp):
        global min,sec
        if sec == 0:
            min = min - 1
            sec = 59
        sec = sec - 1
        if sec<10:
            self.ids.count_down.text = f'{min}:0{sec}'
        else:
            self.ids.count_down.text = f'{min}:{sec}'
        if min == 1:
            self.ids.count_down.color = .99,.43,.23,1
        elif min == 0:
            self.ids.count_down.color = 1, 0, 0, 1
        elif min > 1:
            self.ids.count_down.color = 1, 1, 1, 1
        if min == 0 and sec == 0:
            self.parent.current = 'punteggio'
            self.parent.transition = SlideTransition(direction='left')
        ##print(self.tmp_scrollview.scroll_x)

    def press_risposta(self,indice):
        global n_domanda
        global n_domande
        global out_domande
        global n_domanda
        global risp_giuste
        global risp_sbagliate
        global domande_errate
        global list_answer
        #verifica rsiposta
        if self.answare =='':
            if indice == self.r:
                risp_giuste=risp_giuste+1
                list_answer[n_domanda-1]=1
            else:
                risposte=self.write_answare(self.r,indice)
                domande_errate[n_domanda]=f'{self.indice};{self.domanda};{risposte[0]};{risposte[1]};{self.tipologies};{indice}'
                risp_sbagliate=risp_sbagliate+1
                list_answer[n_domanda-1]=2

        else:
            if self.answare != indice:
                if self.answare ==self.r and indice != self.r:
                    risposte = self.write_answare(self.r, indice)
                    domande_errate[n_domanda] = f'{self.indice};{self.domanda};{risposte[0]};{risposte[1]};{self.tipologies};{indice}'

                    risp_giuste=risp_giuste-1
                    risp_sbagliate=risp_sbagliate+1
                    list_answer[n_domanda-1]=2

                elif self.answare != self.r and indice == self.r:
                    domande_errate[n_domanda] = ''
                    risp_giuste=risp_giuste+1
                    risp_sbagliate=risp_sbagliate-1
                    list_answer[n_domanda-1]=1

        self.ids.card_a.md_bg_color = .2,.3,.23,1
        self.ids.card_b.md_bg_color = .2,.3,.23,1
        self.ids.card_c.md_bg_color = .2,.3,.23,1

        tmp=out_domande[n_domanda-1].split(';')

        if self.answare != indice:

            tmp[7] = indice
            out_domande[n_domanda - 1] = f'{tmp[0]};{tmp[1]};{tmp[2]};{tmp[3]};{tmp[4]};{tmp[5]};{tmp[6]};{tmp[7]}'
            self.card_num[n_domanda - 1].color = .99, .43, .23, 1
            if n_domanda<n_domande:
                n_domanda=n_domanda+1

            self.write_domanda()
            self.scroll()
            ##print('add')

        else:
            tmp[7] = ''
            out_domande[n_domanda - 1] = f'{tmp[0]};{tmp[1]};{tmp[2]};{tmp[3]};{tmp[4]};{tmp[5]};{tmp[6]};{tmp[7]}'
            self.card_num[n_domanda - 1].color = .95,.92,.85,1
            list_answer[n_domanda-1]=0
            if self.answare == self.r:
                risp_giuste = risp_giuste - 1
            elif  self.answare != self.r:
                risp_sbagliate = risp_sbagliate - 1
            self.answare=''
            ##print('clean')

    def write_answare(self,corretta,risposta_data):
        if corretta == 'a':
            risp_corretta = self.a
        elif corretta=='b':
            risp_corretta = self.b
        elif corretta=='c':
            risp_corretta = self.c

        if risposta_data == 'a':
            risp_data=self.a
        elif risposta_data == 'b':
            risp_data = self.b
        elif risposta_data == 'c':
            risp_data = self.c

        return risp_corretta, risp_data

    def scroll(self):
        global n_domanda
        global n_domande
        #print('1')
        #self.scroll_x = self.scroll_x
        self.tmp_scrollview.do_scroll_x = False
        if self.tmp_scrollview.scroll_x <= 0:
            self.tmp_scrollview.scroll_x = 0
            #print(self.tmp_scrollview.scroll_x)
        if self.tmp_scrollview.scroll_x >= 1:
            self.tmp_scrollview.scroll_x = 1
        self.m = ((1-0)/(n_domande-1))
        self.q = 1 - self.m * n_domande
        ##print(n_domanda)
        self.tmp_scrollview.scroll_x = self.m*n_domanda +self.q

    def write_domanda(self):
        domanda=split()
        self.ids.card_a.md_bg_color = .2,.3,.23,1
        self.ids.card_b.md_bg_color = .2,.3,.23,1
        self.ids.card_c.md_bg_color = .2,.3,.23,1
        self.domanda = domanda[0]
        self.a = domanda[1]
        self.b = domanda[2]
        self.c = domanda[3]
        self.r = domanda[4]
        self.tipologies = domanda[8]
        self.indice = domanda[7]
        self.answare = domanda[6]
        if self.answare == 'a':
            self.ids.card_a.md_bg_color =.99,.43,.23,1
        elif self.answare == 'b':
            self.ids.card_b.md_bg_color =.99,.43,.23,1
        elif self.answare == 'c':
            self.ids.card_c.md_bg_color =.99,.43,.23,1

    def on_touch_up(self, touch):
        self.antiripetizione=0
        if self.answare == 'a':
            self.ids.card_a.md_bg_color = .99, .43, .23, 1
            self.ids.card_b.md_bg_color = .2,.3,.23,1
            self.ids.card_c.md_bg_color = .2,.3,.23,1
        elif self.answare == 'b':
            self.ids.card_b.md_bg_color = .99, .43, .23, 1
            self.ids.card_a.md_bg_color = .2,.3,.23,1
            self.ids.card_c.md_bg_color = .2,.3,.23,1
        elif self.answare == 'c':
            self.ids.card_c.md_bg_color = .99, .43, .23, 1
            self.ids.card_a.md_bg_color = .2,.3,.23,1
            self.ids.card_b.md_bg_color = .2,.3,.23,1
        elif self.answare == '':
            self.ids.card_a.md_bg_color = .2,.3,.23,1
            self.ids.card_b.md_bg_color = .2,.3,.23,1
            self.ids.card_c.md_bg_color = .2,.3,.23,1

    def store_statistics(self):
        from DomandePage import risp_non_date,risp_giuste,risp_sbagliate,n_domande,min,sec
        from MainPage import indice,regione
        tmp_indice=indice
        self.risposte_corrette=risp_giuste
        self.risposte_sbagliate=risp_sbagliate
        self.risposte_non_date=risp_non_date
        self.numero_domande=n_domande
        if regione ==0:
            statistiche = JsonStore('errori/Lombardia/Statistiche.json')
        elif regione ==1:
            statistiche = JsonStore('errori/Toscana/Statistiche.json')

        if tmp_indice==1:
            name = 'cinghiale'

        elif tmp_indice == 2:
            name = 'penna'
        if statistiche.exists(name):
            pass
        else:
            statistiche.put(name,tot_quiz=0,tot_promosso=0,tot_bocciato=0,tot_giuste=0,tot_sbagliate=0,tot_non_date=0,perc_passate=0.0,perc_errori=0.0,min_medio= 0,sec_medio= 0,errori_ultime_5= [0.0, 0.0, 0.0, 0.0, 0.0],perc_ultime5= 0.0)

        #Tot Quiz
        tot_quiz=statistiche.get(name)['tot_quiz']
        tot_quiz=tot_quiz+1

        #tot promosso o tot bocciato
        limite=n_domande-4
        tot_promosso = statistiche.get(name)['tot_promosso']
        tot_bocciato = statistiche.get(name)['tot_bocciato']
        if risp_giuste>=limite:
            tot_promosso=tot_promosso+1
        else:
            tot_bocciato=tot_bocciato+1

        #tot giuste
        tot_giuste = statistiche.get(name)['tot_giuste']
        tot_giuste=tot_giuste+risp_giuste

        #tot sbaglaite
        tot_sbagliate = statistiche.get(name)['tot_sbagliate']
        tot_sbagliate=tot_sbagliate+risp_sbagliate

        #tot non date
        tot_non_date = statistiche.get(name)['tot_non_date']
        tot_non_date=tot_non_date+risp_non_date

        #%_passate
        perc_passate= tot_promosso*100/tot_quiz

        #%_errori
        perc_errori = statistiche.get(name)['perc_errori']
        percentuale_errori= (self.risposte_sbagliate*100)/self.numero_domande
        perc_errori= (float(perc_errori)*(int(tot_quiz)-1)+percentuale_errori)/int(tot_quiz)

        #min medio
        min_medio = statistiche.get(name)['min_medio']
        min_medio=((min_medio*(tot_quiz-1))+min)/tot_quiz

        #sec medio
        sec_medio = statistiche.get(name)['sec_medio']
        sec_medio=((sec_medio*(tot_quiz-1))+sec)/tot_quiz

        # ultime 5 medio
        errori_ultime_5 = statistiche.get(name)['errori_ultime_5']
        errori_ultime_5[4] = errori_ultime_5[3]
        errori_ultime_5[3] = errori_ultime_5[2]
        errori_ultime_5[2] = errori_ultime_5[1]
        errori_ultime_5[1] = errori_ultime_5[0]
        errori_ultime_5[0] = percentuale_errori
        perc_ultime5=(errori_ultime_5[4]+errori_ultime_5[3]+errori_ultime_5[2]+errori_ultime_5[1]+errori_ultime_5[0])/5

        statistiche.put(name,tot_quiz=tot_quiz,tot_promosso=tot_promosso,tot_bocciato=tot_bocciato,tot_giuste=tot_giuste,tot_sbagliate=tot_sbagliate,tot_non_date=tot_non_date,perc_passate=perc_passate,perc_errori=perc_errori,min_medio= min_medio,sec_medio= sec_medio,errori_ultime_5= errori_ultime_5,perc_ultime5= perc_ultime5)

    def on_touch_move(self, touch):
        global n_domanda
        global n_domande
        lim_inf_y = Window.size[1] * 0.865
        lim_sup_y = Window.size[1] * 0.52
        lim_x = Window.size[0] * 0.5
        if self.antiripetizione==0:
            if touch.oy < lim_inf_y and touch.oy > lim_sup_y and touch.y < lim_inf_y and touch.y > lim_sup_y:
                travel=touch.ox-touch.x
                if travel <0 and travel < -lim_x and n_domanda>1:
                    n_domanda =n_domanda-1
                    self.write_domanda()
                    self.scroll()
                    self.antiripetizione=1

                elif travel >0 and travel >lim_x and n_domanda<n_domande:
                    n_domanda = n_domanda + 1
                    self.write_domanda()
                    self.scroll()
                    self.antiripetizione = 1


def split():
    global out_domande
    global n_domanda
    tmp_domanda = out_domande[n_domanda-1].split(';')
    tmp_indice_domanda = n_domanda-1
    indice = tmp_domanda[0]
    domanda = tmp_domanda[1]
    a = tmp_domanda[2]
    b = tmp_domanda[3]
    c = tmp_domanda[4]
    ##print(tmp_domanda[7])
    if tmp_domanda[5] == 'A' or tmp_domanda[5] == 'a':
        risposta = 'a'
    elif tmp_domanda[5] == 'B' or tmp_domanda[5] == 'b':
        risposta = 'b'
    elif tmp_domanda[5] == 'C' or tmp_domanda[5] == 'c':
        risposta = 'c'
    tipologia = tmp_domanda[6]
    if tmp_domanda[7] != '':
        risposta_data = tmp_domanda[7]
    else:
        risposta_data = ''
    return domanda, a, b, c, risposta, tmp_indice_domanda, risposta_data, indice, tipologia

def chooseQuestion(indice,type,n_domande,regione):


    if indice == 1:
        if regione !=1:
            if type ==0:
                n_domande_cinghiale_Lombardia = [10, 5, 10, 5]  ##Armi,bioEco,caccia,malattie
                readQuestion(testi_cinghiale_Lombardia[1], n_domande_cinghiale_Lombardia[0], 0, 1)
                readQuestion(testi_cinghiale_Lombardia[2], n_domande_cinghiale_Lombardia[1], n_domande_cinghiale_Lombardia[0], 2)
                readQuestion(testi_cinghiale_Lombardia[3], n_domande_cinghiale_Lombardia[2], n_domande_cinghiale_Lombardia[1] + n_domande_cinghiale_Lombardia[0], 3)
                readQuestion(testi_cinghiale_Lombardia[4], n_domande_cinghiale_Lombardia[3],n_domande_cinghiale_Lombardia[1] + n_domande_cinghiale_Lombardia[0] + n_domande_cinghiale_Lombardia[2], 4)
            elif type !=0 :
                readQuestion(testi_cinghiale_Lombardia[type], n_domande, 0, type)
        elif regione ==1:
            readQuestion(testi_cinghiale_Toscana[0], n_domande, 0, 0)

    elif indice == 2:
        if regione==0:
            n_domande_penna_Lombardia = [10, 5, 5, 5, 5]  ##Armi,zoologia,soccorso,venatoria,natura
            n_argomenti=5
            num_domande=n_domande_penna_Lombardia
            domande=testi_penna_Lombardia
        elif regione==1:
            n_domande_penna_Toscana = [10, 10, 5, 5, 5, 5]  ##Armi,zoologia,soccorso,venatoria,natura
            n_argomenti=6
            num_domande=n_domande_penna_Toscana
            domande=testi_penna_Toscana

        if type==0:
            indice=0
            for x in range (0,n_argomenti):
                readQuestion(domande[x+1],num_domande[x],indice,x+1)
                indice=indice+num_domande[x]
        else:
            readQuestion(domande[type], n_domande, 0, type)

        ##if regione!=1:
        #    if type == 0 :

#                readQuestion(testi_penna_Lombardia[1], n_domande_penna_Lombardia[0], 0, 1)
 #               readQuestion(testi_penna_Lombardia[2], n_domande_penna_Lombardia[1], n_domande_penna_Lombardia[0], 2)
  #              readQuestion(testi_penna_Lombardia[3], n_domande_penna_Lombardia[2], n_domande_penna_Lombardia[0] + n_domande_penna_Lombardia[1], 3)
   #             readQuestion(testi_penna_Lombardia[4], n_domande_penna_Lombardia[3], n_domande_penna_Lombardia[0] + n_domande_penna_Lombardia[1] + n_domande_penna_Lombardia[2], 4)
    #            readQuestion(testi_penna_Lombardia[5], n_domande_penna_Lombardia[4], n_domande_penna_Lombardia[0] + n_domande_penna_Lombardia[1] + n_domande_penna_Lombardia[2] + n_domande_penna_Lombardia[3], 5)
     #       else:
      #          readQuestion(testi_penna_Lombardia[type], n_domande, 0, type)
       # elif regione ==1:


    mischiaQuestion()

def readQuestion(name, numero_domande,indice_iniziale,tipologia):
    global out_domande
    b=0
    a = 1
    print(name)
    file = open(name, 'r')
    f = file.read().split('\n')
    file.close()

    for n_line in f:
        if n_line:
            b += 1

    indice = [i for i in range(a, b+1)]
    random.shuffle(indice)

    for i in range(indice_iniziale,numero_domande+indice_iniziale):
        ##print(i)
        tmp_domande =(f[indice[i-indice_iniziale]-1])
        ##print(tmp_domande)
        out_domande[i] = tmp_domande+';'+str(tipologia)+';'+''
        ##print( out_domande[i])

def mischiaQuestion():
    global out_domande
    global n_domande
    tmp_question = out_domande

    a=0
    b=n_domande
    indice = [i for i in range(a, b)]

    random.shuffle(indice)

    file1 = open('domande.txt', 'a')
    i=0
    for i in range(0,b):
        ##out_domande[i] =''
        tmp_indice=indice[i]

        print(tmp_question[tmp_indice], file=file1)
        print(tmp_question[tmp_indice])
    file1.close()
    file2 = open('domande.txt', 'r')
    out_domande =file2.read().split('\n')
    ##print(out_domande)
    file2.close()
    os.remove('domande.txt')


class Tmp(MDCard):
    def on_kv_post(self, base_widget):
        tmp_sub= ((Window.size[1]*6/100)/2)
        self.width= Window.size[0]/2 -tmp_sub


class DomandeCard(MDCard):
    def changebg(self):
        self.md_bg_color= .99,.43,.23,1

    def returnbg(self):
        #self.md_bg_color=.05,.31,.23,1
        pass


class PopUpFlag(Popup):
    def on_open(self):
        global risp_giuste
        global risp_sbagliate
        global n_domande
        global risp_non_date
        risp_non_date=n_domande-(risp_sbagliate+risp_giuste)
        if risp_non_date >1:
            self.ids.popup_label.text=f'Ci sono {risp_non_date} rispste non date.\nVuoi procedere con la correzione?'
        elif risp_non_date ==0:
            self.ids.popup_label.text = f'Confermi di voler procedere con la correzione?'
        elif risp_non_date ==1:
            self.ids.popup_label.text ="è presente una risposta non data.\nVuoi procedere con la correzione?"

    def flag_state(self):
        global flag
        flag=1
    pass
