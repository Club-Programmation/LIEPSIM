import pygame_menu
import pygame

class Menu:

    pygame.init()
    start = 0
    surface = pygame.display.set_mode((800, 600))
    menubackgroundimage = pygame_menu.baseimage.BaseImage(image_path="assets/images/liep_background.png", drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
    font_title = "assets/fonts/SuperPixel.ttf"
    font_widget = pygame_menu.font.FONT_8BIT
    menubarstyle = pygame_menu.widgets.MENUBAR_STYLE_NONE
    theme_mainmenu = pygame_menu.Theme(background_color=menubackgroundimage,
                                       selection_color=(225, 225, 225),
                                       title_bar_style=menubarstyle,
                                       title_font=font_title,
                                       title_font_color=(255, 255, 255),
                                       title_font_size=60,
                                       title_offset=(250, 40),
                                       widget_font=font_widget,
                                       widget_font_color=(255, 255, 255),
                                       widget_font_size=30,
                                       widget_padding=(16, 32))
    theme_credits = pygame_menu.Theme(background_color=menubackgroundimage,
                                      selection_color=(225, 225, 225),
                                      title_bar_style=menubarstyle,
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

    def start_the_game():
        Menu.start = 1

    def options_menu(self):
        pass

    def credits_menu_open():
        Menu.mainmenu._open(Menu.credits_menu)

    mainmenu = pygame_menu.Menu('LIEPSIM', 800, 450, theme=theme_mainmenu)
    mainmenu.add.button('Jouer', start_the_game)
    mainmenu.add.button('Options', options_menu)
    mainmenu.add.button('Credits', credits_menu_open)
    mainmenu.add.button('Quitter', pygame_menu.events.EXIT)

    credits_menu = pygame_menu.Menu(" ", 800, 450, theme=theme_credits)
    for i in credits_text:
        credits_menu.add.label(i, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    credits_menu.add.button('Precedent', pygame_menu.events.BACK)

    options = pygame_menu.Menu('Options', 600, 400)
    options.add.selector('', [('', 1), ('', 2)])
