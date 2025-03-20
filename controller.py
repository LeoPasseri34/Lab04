import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._language = None

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def handleLanguage(self, e):
        print("Lingua selezionata")
        self._view.txtOut.controls.append(ft.Text(value="Lingua selezionata correttamente: " + self._view.dd.value))
        self._view.update()

    def handleSelection(self, e):
        self._view.txtOut.controls.append(ft.Text(value="Modalità selezionata correttamente: " + self._view.ddSelection.value))
        self._view.update()

    def handleSpellCheck(self, e):
        frase = self._view.myText.value
        if frase == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a sentence!"))
            return

        lingua = self._view.dd.value
        print(lingua)
        modalita = self._view.ddSelection.value
        print(modalita)

        if lingua == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select language!"))
            return
        if modalita == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select modality!"))
            return

        parole, tempo = self.handleSentence(frase, lingua, modalita)

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Frase inserita: " + frase))
        self._view.txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view.txtOut.controls.append(ft.Text(value="Tempo richiesto dalla ricerca: " + str(tempo)))

        self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")



def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

