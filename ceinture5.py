# coding: utf8
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, GdkPixbuf
import random
import time
import threading


class Statistiques():
    '''Charge un fichier au format cvs
    Format du fichier cvs
    +----------------------------------------------------------------------------------------+
    + date + nombre de questions + nombre de fautes + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
    +----------------------------------------------------------------------------------------+
    '''

    def __init__(self):
        self.file = "stats.cvs"
        self.list_stat = ["date", "questionq", "fautes", "q1", "q2", "q3", "q3", "q4", "q5", "q6", "q7", "q8", "q9",
                          "q10"]
        self.dico_stat = {}
        for clef in range(0, len(self.list_stat)):
            self.dico_stat[self.list_stat[clef]] = ""

            # print(self.dico_stat)

    def open(self):
        input_file = open(self.file, "r")
        t = input_file.read()
        a = t.split("\n")
        # print (a)
        dico_outout = {}
        for b in range(0, len(a)):
            # print (b)
            tableau = a[b].split(';')
            # print (tableau)
            cle = tableau[0]
            valeur = tableau[1]
            dico_outout[cle] = valeur
        return (dico_outout)

    def get_values(self, clef, value):
        for i in range(0, len(self.list_stat)):
            if clef == self.list_stat[i]:
                self.dico_stat[self.list_stat[i]] = value

    def update(self):
        self.write(dico=self.dico_stat)

    def write(self, dico):
        output = open(self.file, 'a')
        dico['date'] = time.strftime("%Y-%m-%d %H:%M:%S")

        for cle, valeur in sorted(dico.items()):
            output.write("'{}';".format(valeur))
        output.write("\n")


class Read_Write():
    def __init__(self):
        self.file = "data.txt"

    def open(self):
        input_file = open(self.file, "r")
        t = input_file.read()
        a = t.split("\n")
        # print (a)
        dico_outout = {}
        for b in range(0, len(a) - 1):
            # print (b)
            tableau = a[b].split(';')
            # print (tableau)
            cle = tableau[0]
            valeur = tableau[1]
            dico_outout[cle] = valeur
        return (dico_outout)

    def read(self, ceinture):
        dico = self.open()
        # print(dico)
        for cle, valeur in dico.items():
            if ceinture == cle:
                return (valeur)

                # dico_outout[cle] = valeur
                # print(a[b])

    def update(self, ceinture, n_valeur):
        dico = self.open()
        # print(dico)
        for cle, valeur in dico.items():
            if ceinture == cle:
                dico[cle] = n_valeur
        return self.write(dico)

    def write(self, dico):
        output = open(self.file, 'w')
        for cle, valeur in dico.items():
            output.write("{};{}\n".format(cle, valeur))


class TimerWindow():
    def __init__(self):
        self.start()

    def start(self):
        entry = main.label_chronometre
        starttime = time.time()
        totaltime = 60  # float(entry.get_text())
        self.update(starttime, totaltime, entry)

    def update(self, starttime, totaltime, entry):
        value = round(totaltime - (time.time() - starttime), 1)
        entry.set_label(str(value))

        if float(entry.get_text()) > 0:
            t = threading.Timer(0.1, self.schedule_update, [starttime, totaltime, entry])
            t.start()

        elif float(entry.get_text()) == 0:
            main.fin()

    def schedule_update(self, *args):
        GObject.idle_add(self.update, *args)


class Ceinture:
    def __init__(self):

        self.gladefile = "ceinture2.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)

        self.cssProvider = Gtk.CssProvider()
        self.cssProvider.load_from_path('style.css')
        self.screen = Gdk.Screen.get_default()
        self.styleContext = Gtk.StyleContext()
        self.styleContext.add_provider_for_screen(self.screen, self.cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self.window1 = self.builder.get_object("window1")
        self.window2 = self.builder.get_object("window3")

        self.button_lancer = self.builder.get_object("button_lancer")

        self.checkbutton1 = self.builder.get_object("checkbutton1")
        self.checkbutton2 = self.builder.get_object("checkbutton2")
        self.checkbutton3 = self.builder.get_object("checkbutton3")
        self.checkbutton4 = self.builder.get_object("checkbutton4")
        self.checkbutton5 = self.builder.get_object("checkbutton5")
        self.checkbutton6 = self.builder.get_object("checkbutton6")
        self.checkbutton7 = self.builder.get_object("checkbutton7")
        self.checkbutton8 = self.builder.get_object("checkbutton8")
        self.checkbutton9 = self.builder.get_object("checkbutton9")
        self.checkbutton10 = self.builder.get_object("checkbutton10")

        self.ligne1 = self.builder.get_object("ligne1")

        # a in range(1, 2):
        #    exec("reponse_correction_"+ str(a) +" = self.builder.get_object('checkbutton" + str(a) + "')")

        self.label_chronometre = self.builder.get_object("label_chronometre")
        self.label_chronometre.set_label("60")
        for a in range(1, 11):
            exec("self.label_question" + str(a) + " = self.builder.get_object('label_question" + str(a) + "')")
            exec("self.label_question" + str(a) + ".set_label('(-) x (-)')")
            exec("self.radiobutton" + str(a) + "_a = self.builder.get_object('radiobutton" + str(a) + "_a')")
            exec("self.radiobutton" + str(a) + "_b = self.builder.get_object('radiobutton" + str(a) + "_b')")
            exec("self.radiobutton" + str(a) + "_c = self.builder.get_object('radiobutton" + str(a) + "_c')")
            exec("self.radiobutton" + str(a) + "_a.set_label('--')")
            exec("self.radiobutton" + str(a) + "_b.set_label('--')")
            exec("self.radiobutton" + str(a) + "_c.set_label('--')")

            exec("self.ligne" + str(a) + " = self.builder.get_object('ligne" + str(a) + "')")
            exec("self.style_ligne" + str(a) + " = self.ligne" + str(a) + ".get_style_context()")

        self.image_q = self.builder.get_object("image_q")

        self.image_jaune = self.builder.get_object("image_jaune")
        self.image_orange = self.builder.get_object("image_orange")
        self.image_rose = self.builder.get_object("image_rose")
        self.image_vert_clair = self.builder.get_object("image_vert_clair")
        self.image_vert_fonce = self.builder.get_object("image_vert_fonce")
        self.image_bleu_clair = self.builder.get_object("image_bleu_clair")
        self.image_bleu_fonce = self.builder.get_object("image_bleu_fonce")
        self.image_mauve = self.builder.get_object("image_mauve")
        self.image_violette = self.builder.get_object("image_violette")
        self.image_marron = self.builder.get_object("image_marron")
        self.image_noire = self.builder.get_object("image_noire")

        self.bouton_blanche = self.builder.get_object("bouton_blanche")
        self.bouton_orange = self.builder.get_object("bouton_orange")
        self.bouton_jaune = self.builder.get_object("bouton_jaune")
        self.bouton_rose = self.builder.get_object("bouton_rose")
        self.bouton_vert_clair = self.builder.get_object("bouton_vert_clair")
        self.bouton_vert_fonce = self.builder.get_object("bouton_vert_fonce")
        self.bouton_bleu_clair = self.builder.get_object("bouton_bleu_clair")
        self.bouton_bleu_fonce = self.builder.get_object("bouton_bleu_fonce")
        self.bouton_mauve = self.builder.get_object("bouton_mauve")
        self.bouton_violette = self.builder.get_object("bouton_violette")
        self.bouton_marron = self.builder.get_object("bouton_marron")
        self.bouton_noire = self.builder.get_object("bouton_noire")

        # Display the window
        self.window1.show()
        self.window2.hide()

        self.list_table_ceinture_blanche = [2, 10]
        self.list_table_ceinture_jaune = [2, 5, 10]
        self.list_table_ceinture_orange = [2, 3, 5, 10]
        self.list_table_ceinture_rose = [2, 3, 4, 5, 10]
        self.list_table_ceinture_vert_clair = [2, 3, 4, 5, 6, 10]
        self.list_table_ceinture_vert = [2, 3, 4, 5, 6, 7, 10]
        self.list_table_ceinture_bleu_clair = [2, 3, 4, 5, 6, 7, 8, 10]
        self.list_table_ceinture_bleu = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.list_table_ceinture_mauve = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.list_table_ceinture_violette = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.list_table_ceinture_marron = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.list_table_ceinture_noir = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.list_table_ceinture = []

        self.dico_reponse = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                             '10': []}
        self.dico_ceinture = {'blanche'}

        self.list_table_ceinture = []
        self.list_resultats = []
        self.question_en_cours = []
        self.tps_chronometre = 0
        self.ceinture = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.response_juste = 0
        self.response_fause = 0
        self.reponse_total = 0
        self.nu_question = 0

        self.score()

    def on_window1_destroy(self, *args):
        Gtk.main_quit(*args)

    def on_window2_destroy(self, *args):
        Gtk.main_quit(*args)

    def on_button_lancer_clicked(self, button):
        self.top()
        self.questionnaire(self.table_ceinture())
        self.button_lancer.set_sensitive(False)
        self.reponse_total = 0
        self.response_juste = 0
        self.response_fause = 0
        for a in range(1, 11):
            exec("self.style_ligne" + str(a) + ".remove_class('faux')")
            exec("self.style_ligne" + str(a) + ".remove_class('juste')")
            exec("self.radiobutton" + str(a) + "_a.set_active(True)")

    def on_Fermer_clicked(self, button):
        self.window2.hide()
        self.window1.show()
        self.score()

    def on_Bouton_blanche_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_blanche)
        self.ceinture_select = "blanche"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_jaune_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_jaune)
        self.ceinture_select = "jaune"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_orange_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_orange)
        self.ceinture_select = "orange"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_rose_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_rose)
        self.ceinture_select = "rose"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_vert_clair_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_vert_clair)
        self.ceinture_select = "vert-clair"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_vert_fonce_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_vert)
        self.ceinture_select = "vert-fonce"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_bleu_clair_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_bleu_clair)
        self.ceinture_select = "bleu-clair"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_bleu_fonce_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_bleu)
        self.ceinture_select = "bleu-fonce"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_mauve_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_mauve)
        self.ceinture_select = "mauve"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_violette_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_violette)
        self.ceinture_select = "violette"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_marron_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_marron)
        self.ceinture_select = "marron"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_Bouton_noir_clicked(self, button):
        self.list_table_ceinture = random.shuffle(self.list_table_ceinture_noir)
        self.ceinture_select = "noire"
        self.choix_ceinture(self.ceinture_select)
        self.raz()

    def on_radiobutton1_a_clicked(self, button):
        self.nu_question = 1
        reponse = button.get_label()
        # print("1-a : "+str(reponse))

    def on_radiobutton1_b_clicked(self, button):
        self.nu_question = 1
        reponse = button.get_label()
        # print("1-b : "+str(reponse))

    def on_radiobutton1_c_clicked(self, button):
        self.nu_question = 1
        reponse = button.get_label()
        # print("1-c : "+str(reponse))

    def reponse1_clicked(self, button):
        id = self.nu_question
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.table_ceinture())

    def reponse2_clicked(self, button, nu_question=0):
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.table_ceinture())

    def reponse3_clicked(self, button, nu_question=0):
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.table_ceinture())

    def top(self):
        self.t = TimerWindow()

    def score(self):
        list_bouton = ["self.bouton_blanche", "self.bouton_jaune", "self.bouton_orange", "self.bouton_rose",
                       "self.bouton_vert_clair", "self.bouton_vert_fonce", "self.bouton_bleu_clair",
                       "self.bouton_bleu_fonce", "self.bouton_mauve", "self.bouton_violette", "self.bouton_marron",
                       "self.bouton_noire"]
        list_couleur = ["blanche", "jaune", "orange", "rose", "vert-clair", "vert-fonce", "bleu-clair", "bleu-fonce",
                        "mauve", "violette", "marron", "noire"]
        read = Read_Write()

        # print(self.label_chronometre)
        for a in range(1, len(list_bouton)):
            # print("" + str(list_bouton[a]) +".set_label('Validée "+ str(read.read(ceinture=list_couleur[a])) +" fois')")
            exec("" + str(list_bouton[a]) + ".set_label('Validée " + str(
                read.read(ceinture=list_couleur[a])) + " fois')")

    def choix_ceinture(self, image):
        self.window1.hide()
        self.window2.show()
        # print(self.ceinture_select)

        if self.ceinture_select == "blanche":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_blanche

        elif self.ceinture_select == "jaune":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_jaune

        elif self.ceinture_select == "orange":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_orange

        elif self.ceinture_select == "rose":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_rose

        elif self.ceinture_select == "vert-clair":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_vert_clair

        elif self.ceinture_select == "vert-fonce":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_vert

        elif self.ceinture_select == "bleu-clair":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_bleu_clair

        elif self.ceinture_select == "bleu-fonce":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_bleu

        elif self.ceinture_select == "mauve":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_mauve

        elif self.ceinture_select == "violette":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_violette

        elif self.ceinture_select == "marron":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_marron

        elif self.ceinture_select == "noire":
            self.img = GdkPixbuf.Pixbuf.new_from_file("ceinture-" + str(image) + ".png")
            self.image_q.set_from_pixbuf(self.img)
            self.list_table_ceinture = self.list_table_ceinture_noir

    def table_ceinture(self):
        random.shuffle(self.list_table_ceinture)
        table = self.list_table_ceinture[0]
        return table

    def multiplicateur(self):
        random.shuffle(self.ceinture)
        result = self.ceinture[-1]
        self.ceinture.pop()
        return result

    def verification(self, table, multiplicateur, reponse, nu):
        # print (str(table) + " x " + str(multiplicateur) + " = "+str(reponse))
        if table * multiplicateur == reponse:
            # print("nu:" + str(nu) + " -- "+ str(table) + " x " + str(multiplicateur) + " = " + str(reponse) + "(OK)")
            self.response_juste += 1
            return "OK"
        elif not table * multiplicateur == reponse:
            # print("nu:" + str(nu) + " -- " + str(table) + " x " + str(multiplicateur) + " = " + str(reponse) + "(Faux)")
            self.response_fause += 1
            return "Faux"

    def question(self, table, multiplicateur, nu_question):

        q = str(table) + ' x ' + str(multiplicateur)  # Formatage de la question
        # print (q)

        self.question_en_cours.append(multiplicateur)
        self.question_en_cours.append(table)

        exec("self.label_question" + str(nu_question) + ".set_label('" + str(q) + "')")
        # Genére l'erreur la plus probable,
        # soit sur le multiplicateur soit sur la table (+/- 1)
        lst = [1, -1, 0]  # (+/- 1)
        erreur_table_ou_multiplicateur = [0, 1]  # soit sur le multiplicateur, soit sur la table
        random.shuffle(erreur_table_ou_multiplicateur)  # mélange la liste
        random.shuffle(lst)  # mélange la liste

        self.reponse1 = int(multiplicateur) * (int(table) + lst[0])
        self.reponse2 = int(multiplicateur) * (int(table) + lst[1])
        self.reponse3 = int(multiplicateur) * (int(table) + lst[2])

        exec("self.radiobutton" + str(nu_question) + "_a.set_label('" + str(self.reponse1) + "')")
        exec("self.radiobutton" + str(nu_question) + "_b.set_label('" + str(self.reponse2) + "')")
        exec("self.radiobutton" + str(nu_question) + "_c.set_label('" + str(self.reponse3) + "')")
        self.reponse_total += 1
        self.nu_question += 1

    def chronometre(self):
        if self.tps_chronometre < 0:
            self.t.cancel()
            self.button_lancer.set_sensitive(True)

        else:
            self.button_lancer.set_sensitive(False)
            self.tps_chronometre += 1
            self.label_chronometre.set_text(str(self.tps_chronometre))

    def questionnaire(self, table):
        self.list_resultats.clear()
        if float(self.label_chronometre.get_label()) > 0 and self.reponse_total < 10:
            for a in range(1, 11):
                self.question(self.table_ceinture(), self.multiplicateur(), nu_question=a)

        elif float(self.label_chronometre.get_label()) > 0 and not self.reponse_total < 10:
            pass

        elif float(self.label_chronometre.get_label()) < 0:
            self.fin()

    def fin(self):
        for a in range(1, 11):
            self.a = eval("self.radiobutton" + str(a) + "_a.get_label()")
            self.b = eval("self.radiobutton" + str(a) + "_b.get_label()")
            self.c = eval("self.radiobutton" + str(a) + "_c.get_label()")
            t = eval('self.label_question' + str(a) + '.get_label()')
            t1 = t.split(sep=" ")
            t2 = t1[0]
            m = t1[2]
            correction = int(t2) * int(m)

            if eval("self.radiobutton" + str(a) + "_a.get_active()") == True:
                t = eval('self.label_question' + str(a) + '.get_label()')
                # print(t)
                t1 = t.split(sep=" ")
                t2 = t1[0]
                m = t1[2]
                r = eval("self.radiobutton" + str(a) + "_a.get_label()")
                self.list_resultats.append(
                    self.verification(table=int(t2), multiplicateur=int(m), reponse=int(r), nu=a))

            elif eval("self.radiobutton" + str(a) + "_b.get_active()") == True:
                t = eval('self.label_question' + str(a) + '.get_label()')
                t1 = t.split(sep=" ")
                t2 = t1[0]
                m = t1[2]
                r = eval("self.radiobutton" + str(a) + "_b.get_label()")
                self.list_resultats.append(
                    self.verification(table=int(t2), multiplicateur=int(m), reponse=int(r), nu=a))

            elif eval("self.radiobutton" + str(a) + "_c.get_active()") == True:
                t = eval('self.label_question' + str(a) + '.get_label()')
                t1 = t.split(sep=" ")
                t2 = t1[0]
                m = t1[2]
                r = eval("self.radiobutton" + str(a) + "_c.get_label()")
                self.list_resultats.append(
                    self.verification(table=int(t2), multiplicateur=int(m), reponse=int(r), nu=a))

            else:
                pass

            if int(self.a) == correction:
                eval("self.radiobutton" + str(a) + "_a.set_active(True)")
            elif int(self.b) == correction:
                eval("self.radiobutton" + str(a) + "_b.set_active(True)")
            elif int(self.c) == correction:
                eval("self.radiobutton" + str(a) + "_c.set_active(True)")

        # print (self.list_resultats)
        for i in range(1, 11):
            if self.list_resultats[i - 1] == "OK":
                exec("self.style_ligne" + str(i) + ".add_class('juste')")
                # exec("self.ligne" + str(i) + ".set_sensitive(True)")
            elif self.list_resultats[i - 1] == "Faux":
                exec("self.style_ligne" + str(i) + ".add_class('faux')")
                # exec("self.ligne" + str(i) + ".set_sensitive(False)")
        if self.response_juste == 10:
            r = Read_Write()
            ancienne_valeur = r.read(ceinture=self.ceinture_select)
            nouvelle_valeur = int(ancienne_valeur) + 1
            r.update(ceinture=self.ceinture_select, n_valeur=nouvelle_valeur)

        self.label_chronometre.set_label("Résultats: " + str(self.response_juste) + "/10")
        self.button_lancer.set_sensitive(True)
        self.ceinture = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def raz(self):
        for a in range(1, 11):
            # exec("self.ligne" + str(a) + ".set_sensitive(True)")
            exec("self.style_ligne" + str(a) + ".remove_class('faux')")
            exec("self.style_ligne" + str(a) + ".remove_class('juste')")
            exec("self.radiobutton" + str(a) + "_a.set_active(True)")
            exec("self.label_question" + str(a) + ".set_label('(-) x (-)')")
            exec("self.radiobutton" + str(a) + "_a.set_label('--')")
            exec("self.radiobutton" + str(a) + "_b.set_label('--')")
            exec("self.radiobutton" + str(a) + "_c.set_label('--')")


if __name__ == "__main__":
    test = Statistiques()
    test.get_values(clef='q1', value=1)
    test.update()
    test.dico_stat

    main = Ceinture()
    Gtk.main()
