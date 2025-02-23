import pygame_menu
import pygame
from variables import *

class Menu:
    pygame.init()
    assets = Assets()
    start = 0
    surface = pygame.display.set_mode((800, 450))
    color_selection = (225, 225, 225)
    widget_color = (255, 255, 255)
    widget_size = 30
    padding = (16, 32)
    menu_background_image = pygame_menu.baseimage.BaseImage(image_path=assets.liep_background, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
    font_title = assets.super_pixel
    font_widget = pygame_menu.font.FONT_8BIT
    menu_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

    theme_main_menu = pygame_menu.Theme(background_color=menu_background_image,
                                       selection_color=color_selection,
                                       title_bar_style=menu_bar_style,
                                       title_font=font_title,
                                       title_font_color=(255, 255, 255),
                                       title_font_size=60,
                                       title_offset=(250, 40),
                                       widget_font=font_widget,
                                       widget_font_color=widget_color,
                                       widget_font_size=widget_size,
                                       widget_padding=padding)

    theme_credits = pygame_menu.Theme(background_color=menu_background_image,
                                      selection_color=color_selection,
                                      title_bar_style=menu_bar_style,
                                      title_close_button=False,
                                      widget_font=font_widget,
                                      widget_font_color=widget_color,
                                      widget_font_size=widget_size,
                                      widget_padding=padding,
                                      scrollbar_color=(255, 255, 255),
                                      scrollbar_slider_color=(225, 225, 225))

    options_text = ["Options",
                    " "]

    credits_text = ["Credits",
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
                    " ",
                    "Sprite designer",
                    " ",
                    "Annie WANG",
                    " "]

    sounds = pygame_menu.sound.Sound()
    sounds.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, assets.fart)

    main_menu = pygame_menu.Menu("LIEPSIM", 800, 450, theme=theme_main_menu)
    credits_menu = pygame_menu.Menu(" ", 800, 450, theme=theme_credits)
    options_menu = pygame_menu.Menu(" ", 800, 450, theme=theme_credits)

    custom_controller = pygame_menu.controls.Controller()

    def btn_move_up(self, event):
        return Keys().down

    custom_controller.move_up = btn_move_up

    def btn_move_down(self, event):
        return Keys().up

    custom_controller.move_down = btn_move_down

    def start_the_game():
        Menu.start = 1
        Menu.main_menu.clear()
        Menu.main_menu.full_reset()

    def options_menu_open():
        Menu.main_menu._open(Menu.options_menu)

    def credits_menu_open():
        Menu.main_menu._open(Menu.credits_menu)


    def menu_init(self):

        Menu.main_menu.add.button('Jouer', Menu.start_the_game)
        Menu.main_menu.add.button('Options', Menu.options_menu)
        Menu.main_menu.add.button('Credits', Menu.credits_menu_open)
        Menu.main_menu.add.button('Quitter', pygame_menu.events.EXIT)
        Menu.main_menu.set_sound(Menu.sounds, recursive=True)

        Menu.main_menu.set_controller(Menu.custom_controller)

    for i in credits_text:
        credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    credits_menu.add.button('Precedent', pygame_menu.events.BACK)
    credits_menu.set_sound(sounds, recursive=True)

    for j in options_text:
        options_menu.add.label(j, align=pygame_menu.locals.ALIGN_CENTER, font_size=40)

    def set_music_volume(slider_value: float):
        pygame.mixer.music.set_volume(slider_value / 100.0)  # Convert range 0-100 to 0.0-1.0

    # Add the range slider and link it to set_music_volume
    options_menu.add.range_slider('Volume', 100, (0, 100), 1,
                                  rangeslider_id='range_slider',
                                  value_format=lambda x: str(int(x)),
                                  onchange=set_music_volume)
    options_menu.add.button('Precedent', pygame_menu.events.BACK)
    options_menu.set_sound(sounds, recursive=True)