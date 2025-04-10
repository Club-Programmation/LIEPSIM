import pygame_menu
import pygame
from variables import *

class Menu:
    pygame.init()
    def __init__(self):

        self.assets = Assets()
        self.start = 0
        # Définir la taille de la fenêtre
        fullscreen = False
        width = 800
        height = 450
        surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        #surface = pygame.display.set_mode((800, 450))
        # définir les variables pour les menu
        self.color_selection = (225, 225, 225)
        self.widget_color = (255, 255, 255)
        self.widget_size = 30
        self.padding = (16, 32)
        self.menu_background_image = pygame_menu.baseimage.BaseImage(image_path=self.assets.liep_background, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
        self.font_title = self.assets.super_pixel
        self.font_widget = pygame_menu.font.FONT_8BIT
        self.menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        # définir le thème du menu principal
        self.theme_main_menu = pygame_menu.Theme(background_color=self.menu_background_image,
                                           selection_color=self.color_selection,
                                           title_bar_style=self.menu_bar_style,
                                           title_font=self.font_title,
                                           title_font_color=(255, 255, 255),
                                           title_font_size=60,
                                           title_offset=(250, 40),
                                           widget_font=self.font_widget,
                                           widget_font_color=self.widget_color,
                                           widget_font_size=self.widget_size,
                                           widget_padding=self.padding)

        # définir le thème du menu des crédits
        self.theme_credits = pygame_menu.Theme(background_color=self.menu_background_image,
                                          selection_color=self.color_selection,
                                          title_bar_style=self.menu_bar_style,
                                          title_close_button=False,
                                          widget_font=self.font_widget,
                                          widget_font_color=self.widget_color,
                                          widget_font_size=self.widget_size,
                                          widget_padding=self.padding,
                                          scrollbar_color=(255, 255, 255),
                                          scrollbar_slider_color=(225, 225, 225))

        self.theme_skins = pygame_menu.Theme(background_color=self.menu_background_image,
                                             selection_color=self.color_selection,
                                             title_bar_style=self.menu_bar_style,
                                             title_close_button=False,
                                             widget_font=self.font_widget,
                                             widget_font_color=self.widget_color,
                                             widget_font_size=self.widget_size,
                                             widget_padding=(32, 64),
                                             scrollbar_color=(255, 255, 255),
                                             scrollbar_slider_color=(225, 225, 225))
        # définir les textes des menus
        self.options_text = ["Options",
                        " "]

        self.credits_text = ["Credits",
                        " ",
                        "Developpeurs",
                        " ",
                        "Kyllian LIM",
                        "Valentin MUSEREAU",
                        "Sacha EWENCZYK",
                        "Lucas RUDANT",
                        "Riyad GHANEM",
                        "Kevin QIU",
                        "Windy JERUME",
                        "Rayan KERROUMI-PERALTA",
                        " ",
                        "Sprite designer",
                        " ",
                        "Annie WANG",
                        " "]

        # définir les sons
        self.sounds = pygame_menu.sound.Sound()
        self.sounds.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, self.assets.fart)

        # créer les menus
        self.main_menu = pygame_menu.Menu("LIEPSIM", width, height, theme=self.theme_main_menu)
        self.credits_menu = pygame_menu.Menu(" ", width, height, theme=self.theme_credits)
        self.options_menu = pygame_menu.Menu(" ", width, height, theme=self.theme_credits)
        self.skins_menu = pygame_menu.Menu(" ", width, height, theme=self.theme_skins)

        # boucle qui place le texte dans les crédits
        for i in self.credits_text:
            self.credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
        self.credits_menu.add.button('Precedent', pygame_menu.events.BACK)
        self.credits_menu.set_sound(self.sounds, recursive=True)

        # boucle qui place le texte dans les options
        for j in self.options_text:
            self.options_menu.add.label(j, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)

        self.options_menu.add.button('Precedent', pygame_menu.events.BACK)
        self.options_menu.set_sound(self.sounds, recursive=True)

        # fonction qui permet de régler le volume
        def set_music_volume(slider_value: float):
            pygame.mixer.music.set_volume(slider_value / 100.0)

            # Ajoute un slider connecté à la fonction réglant le volume

        self.options_menu.add.range_slider('Volume', 100, (0, 100), 1,
                                           rangeslider_id='range_slider',
                                           value_format=lambda x: str(int(x)),
                                           onchange=set_music_volume)

        self.order = 0
        self.skins = [pygame_menu.baseimage.BaseImage(image_path=self.assets.choqué,
                                                      drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY),
                      pygame_menu.baseimage.BaseImage(image_path=self.assets.up_arrow,
                                                      drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY),
                      pygame_menu.baseimage.BaseImage(image_path=self.assets.down_arrow,
                                                      drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)]
        for i in range(len(self.skins)):
            self.skins[i].scale(0.5, 0.5)
        self.decorator = self.skins_menu.get_decorator()

        self.skinsx = -125
        self.skinsy = -150

        self.right_arrow = pygame_menu.BaseImage(image_path=self.assets.right_arrow).scale(4, 4)
        self.left_arrow = pygame_menu.BaseImage(image_path=self.assets.left_arrow).scale(4, 4)
        # Ajouter l'image et stocker l'ID
        self.decor_id = self.decorator.add_baseimage(self.skinsx, self.skinsy, self.skins[self.order], False)

        def change_skin_right():
            # Vérifier si l'élément existe avant de le supprimer
            if self.decor_id is not None:
                self.decorator.remove(self.decor_id)

            # Changer d'image
            self.order = (self.order + 1) % len(self.skins)
            self.decor_id = self.decorator.add_baseimage(self.skinsx, self.skinsy, self.skins[self.order], False)

        def change_skin_left():
            # Vérifier si l'élément existe avant de le supprimer
            if self.decor_id is not None:
                self.decorator.remove(self.decor_id)

            # Changer d'image
            self.order = (self.order - 1) % len(self.skins)
            self.decor_id = self.decorator.add_baseimage(self.skinsx, self.skinsy, self.skins[self.order], False)

        #widget = pygame_menu.widgets.Widget("", onselect=change_skin_right())
        #guten_tag = pygame_menu.widgets.selection.LeftArrowSelection((4, 4), 5, 0, 1)
        #guten_morgan = pygame_menu.widgets.selection.RightArrowSelection((4, 4), 5, 0, 1)
        #guten_morgan.draw(self.surface, widget)
        self.skins_menu.add.banner(self.right_arrow, change_skin_right, align=pygame_menu.locals.ALIGN_RIGHT)
        self.skins_menu.add.banner(self.left_arrow, change_skin_left, align=pygame_menu.locals.ALIGN_LEFT)

    # Permettre d'utiliser zqsd et les flèches pour naviguer dans le menu
    custom_controller = pygame_menu.controls.Controller()

    def btn_move_up(self, event):
        return Keys().down

    custom_controller.move_up = btn_move_up

    def btn_move_down(self, event):
        return Keys().up

    custom_controller.move_down = btn_move_down

    # fonctions qui permettent de passer d'un menu à l'autre
    def start_the_game(self):
        self.start = 1
        self.main_menu.clear()
        self.main_menu.full_reset()

    def skins_open(self):
        self.skins_menu.add.button('Valider', self.start_the_game)
        self.main_menu._open(self.skins_menu)

    def options_menu_open(self):
        self.main_menu._open(self.options_menu)

    def credits_menu_open(self):
        self.main_menu._open(self.credits_menu)

    # Fonction d'initialisation du menu
    def menu_init(self):

        self.main_menu.add.button('Jouer', self.skins_open)
        self.main_menu.add.button('Options', self.options_menu_open)
        self.main_menu.add.button('Credits', self.credits_menu_open)
        self.main_menu.add.button('Quitter', pygame_menu.events.EXIT)
        self.main_menu.set_sound(self.sounds, recursive=True)

        self.main_menu.set_controller(self.custom_controller)