import flet as ft
import controller as c

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = c.SpellChecker(view=self)
        # UI elements
        self.__title = None
        self.__theme_switch = None


        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        #ROW1
        self.dd = ft.Dropdown(label="Seleziona lingua",
                    options=[ft.dropdown.Option("english"), ft.dropdown.Option("italian"), ft.dropdown.Option("spanish")],
                            width=1250, on_change=self.__controller.handleLanguage)

        row1 = ft.Row([self.dd])

        #ROW2
        self.ddSelection = ft.Dropdown(label="Seleziona modalità",
                    options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Lineare"), ft.dropdown.Option("Dicotomica")],
                            width=300,
                            on_change=self.__controller.handleSelection)

        self.myText = ft.TextField(label="Aggiungi una frase", value="", disabled=False, width=800)

        self.btnSpellCheck = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellCheck)

        row2 = ft.Row([self.ddSelection, self.myText, self.btnSpellCheck])

        #Row3

        self.txtOut = ft.ListView(expand=1, spacing=10)

        self.page.add(row1, row2, self.txtOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
