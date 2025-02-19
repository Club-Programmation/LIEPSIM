import pygame_menu
import pygame

class Menu:

    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    menubackgroundimage = pygame_menu.baseimage.BaseImage(image_path="assets/images/liep_background.png", drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
    font_title = "assets/fonts/SuperPixel.ttf"
    font_widget = pygame_menu.font.FONT_8BIT
    menubarstyle = pygame_menu.widgets.MENUBAR_STYLE_NONE
    mytheme = pygame_menu.Theme(background_color=menubackgroundimage,
                                selection_color=(230, 230, 230),
                                title_bar_style=menubarstyle,
                                title_font=font_title,
                                title_font_color=(255, 255, 255),
                                title_font_size=60,
                                title_offset=(250, 40),
                                widget_font=font_widget,
                                widget_font_color=(255, 255, 255),
                                widget_font_size=30,
                                widget_padding=(16, 32))

    def set_difficulty(value, difficulty):
        pass
        #print(value)
        #print(difficulty)

    def start_the_game(self):
        pass

    def options_menu(self):
        pass

    def credits_menu(self):
        pass

    mainmenu = pygame_menu.Menu('LIEPSIM', 800, 450, theme=mytheme)
    mainmenu.add.button('Jouer', start_the_game)
    mainmenu.add.button('Options', options_menu)
    mainmenu.add.button('Credits', credits_menu)
    mainmenu.add.button('Quitter', pygame_menu.events.EXIT)

    options = pygame_menu.Menu('Options', 600, 400)
    options.add.selector('', [('', 1), ('', 2)], onchange=set_difficulty)
