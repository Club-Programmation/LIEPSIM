import pygame_menu
import pygame
from variables import *

class Menu:
    pygame.init()
    assets = Assets()
    start = 0

    surface = pygame.display.set_mode((800, 600))
    menu_background_image = pygame_menu.baseimage.BaseImage(image_path=assets.liep_background, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
    font_title = assets.super_pixel
    font_widget = pygame_menu.font.FONT_8BIT
    menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

    theme_main_menu = pygame_menu.Theme(background_color=menu_background_image,
                                       selection_color=(225, 225, 225),
                                       title_bar_style=menu_bar_style,
                                       title_font=font_title,
                                       title_font_color=(255, 255, 255),
                                       title_font_size=60,
                                       title_offset=(250, 40),
                                       widget_font=font_widget,
                                       widget_font_color=(255, 255, 255),
                                       widget_font_size=30,
                                       widget_padding=(16, 32))

    theme_credits = pygame_menu.Theme(background_color=menu_background_image,
                                      selection_color=(225, 225, 225),
                                      title_bar_style=menu_bar_style,
                                      title_close_button=False,
                                      widget_font=font_widget,
                                      widget_font_color=(255, 255, 255),
                                      widget_font_size=30,
                                      widget_padding=(16, 32),
                                      scrollbar_color=(255, 255, 255),
                                      scrollbar_slider_color=(225, 225, 225))
    credits_text = ["Credits",
                    " ",
                    "Deloppeurs ",
                    " ",
                    "Kyllian LIM",
                    "Valentin MUSEREAU",
                    "Sacha EWENCZYK",
                    "Lucas RUDANT",
                    "Riyad GHANEM",
                    "Kevin QIU",
                    "Windy JERUME",
                    " ",
                    "Sprite designer",
                    " ",
                    "Annie WANG",
                    " "]

    engine = pygame_menu.sound.Sound()
    engine.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, "assets/sounds/fart.mp3")

    def start_the_game():
        Menu.start = 1

    def options_menu(self):
        pass

    def credits_menu_open():
        Menu.main_menu._open(Menu.credits_menu)

    main_menu = pygame_menu.Menu('LIEPSIM', 800, 450, theme=theme_main_menu)
    main_menu.add.button('Jouer', start_the_game)
    main_menu.add.button('Options', options_menu)
    main_menu.add.button('Credits', credits_menu_open)
    main_menu.add.button('Quitter', pygame_menu.events.EXIT)
    main_menu.set_sound(engine, recursive=True)

    credits_menu = pygame_menu.Menu(" ", 800, 450, theme=theme_credits)
    for i in credits_text:
        credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    credits_menu.add.button('Precedent', pygame_menu.events.BACK)
    credits_menu.set_sound(engine, recursive=True)

    options = pygame_menu.Menu('Options', 600, 400)
    options.add.selector('', [('', 1), ('', 2)])
