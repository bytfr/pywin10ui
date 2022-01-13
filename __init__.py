# coding:utf-8
import pygame, easygui, sys

__all__ = ["Window", "FillText", "Rectangular", "Entry", "Progress_bar", "Select_box", "Button", "Picture_box"]


class Window():
    def __init__(self, title, width, height, icon=None, Exit_the_method=None):
        self.title = title
        self.width = width
        self.height = height
        self.icon = icon
        self.event = None
        self.zj = []
        self.Exit_the_method = Exit_the_method
        pygame.init()
        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        if not self.icon is None:
            pygame.display.set_icon(self.icon)

    def mainloop(self):
        for self.event in pygame.event.get():
            # 判断事件是否是退出事件，是则退出
            if self.event.type == pygame.QUIT:
                if self.Exit_the_method is None:
                    # 先退出pygame窗口，再退出程序
                    pygame.quit()
                    sys.exit()
                else:
                    self.Exit_the_method()
            for zjevent in self.zj:
                zjevent.event = self.event
        pygame.display.update()
        pygame.time.delay(10)

    def set_tiltle(self, title):
        pygame.display.set_caption(title)

    def append_component(self, component):
        if isinstance(component, list):
            for cp in component:
                self.zj.append(cp)
        else:
            self.zj.append(component)


class FillText:
    def __init__(self, window: Window, text: str, x: int, y, font, rgb, gjc: bool, quyu=None):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.rgb = rgb
        self.gjc = gjc
        self.quyu = quyu

    def paint(self):
        text = self.font.render(str(self.text), self.gjc, self.rgb)
        if self.quyu is None:
            self.window.canvas.blit(text, (self.x, self.y))
        else:
            self.window.canvas.blit(text, (self.x, self.y), self.quyu)


class Rectangular():
    def __init__(self, window, x, y, width, height, rgb, alpha):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rgb = rgb
        self.alpha = alpha

    def paint(self):
        s = pygame.Surface((self.width, self.height))  # the size of your rect
        s.set_alpha(self.alpha)  # alpha level
        s.fill(self.rgb)  # this fills the entire surface
        self.window.canvas.blit(s, (self.x, self.y))


class Button():
    def __init__(self, window, x, y, text, width, height, common=None, font=None, normal_img=None, focus_img=None,
                 click_img=None):
        self.window = window
        self.event = None
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.common = common
        self.font = font
        self.normal_img = normal_img
        self.focus_img = focus_img
        self.click_img = click_img
        self.rgb1 = (180, 180, 180)
        self.rgb2 = (225, 225, 225)
        self.mousebutton = False

    def mainloop(self):
        mousepos = pygame.mouse.get_pos()
        r1 = Rectangular(self.window, self.x, self.y, self.width, self.height, self.rgb1, 255)
        r2 = Rectangular(self.window, self.x + 1, self.y + 1, self.width - 2, self.height - 2, self.rgb2, 255)
        if self.x <= mousepos[0] <= self.x + self.width and mousepos[1] >= self.y and mousepos[
            1] <= self.y + self.height:
            if self.window.event.type == pygame.MOUSEBUTTONDOWN and not self.mousebutton:
                self.common()
            if self.window.event.type == pygame.MOUSEBUTTONDOWN:
                self.mousebutton = True
            if self.window.event.type == pygame.MOUSEBUTTONUP:
                self.mousebutton = False
            if self.mousebutton:
                self.rgb1 = (73, 132, 180)
                self.rgb2 = (204, 228, 247)
            else:
                self.rgb1 = (24, 132, 218)
                self.rgb2 = (229, 241, 251)
        else:
            self.rgb1 = (180, 180, 180)
            self.rgb2 = (225, 225, 225)
        r1.paint()
        r2.paint()

        font1 = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 14)
        painttext = FillText(self.window, self.text, self.x + (
                (self.width / 2) - (font1.render(self.text, True, (255, 255, 255)).get_width() / 2)), self.y + (
                                     (self.height / 2) - (
                                     font1.render(self.text, True, (255, 255, 255)).get_height() / 2)), font1,
                             (0, 0, 0), True)

        if not self.font is None:
            painttext.font = self.font[0]
            painttext.x = self.x + (
                    (self.width / 2) - (self.font[0].render(self.text, True, (255, 255, 255)).get_width() / 2))
            painttext.y = self.y + (
                    (self.height / 2) - (self.font[0].render(self.text, True, (255, 255, 255)).get_height() / 2))
            painttext.rgb = self.font[1]
            painttext.gjc = self.font[2]
        painttext.paint()


class Entry():
    def __init__(self, window, x, y, text, width, height, common=None, font=None, normal_img=None, click_img=None):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.common = common
        self.font = font
        self.normal_img = normal_img
        self.click_img = click_img
        self.event = None

    def mainloop(self):
        mousepos = pygame.mouse.get_pos()
        r1 = Rectangular(self.window, self.x, self.y, self.width, self.height, (135, 135, 135), 255)
        r2 = Rectangular(self.window, self.x + 1, self.y + 1, self.width - 2, self.height - 2, (255, 255, 255), 255)
        r1.paint()
        r2.paint()
        if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
            if self.event.type == pygame.MOUSEBUTTONDOWN and self.event.button == 1:
                if self.normal_img is None:
                    r1.rgb = (13, 127, 216)
                    r2.rgb = (255, 255, 255)
                    r1.paint()
                    r2.paint()
                else:
                    self.window.canvas.blit(self.normal_img, (self.x, self.y))
                e = easygui.enterbox("", "", self.text)
                if e != "" and not e is None:
                    self.text = e
                if not self.common is None:
                    self.common()
        font1 = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 14)
        painttext = FillText(self.window, self.text, self.x + 2, self.y + (
                (self.height / 2) - (font1.render(self.text, True, (255, 255, 255)).get_height() / 2)), font1,
                             (0, 0, 0), True, (0, 0, self.width - 4, self.height))
        if not self.font is None:
            painttext.font = self.font[0]
            painttext.x = self.x + 2
            painttext.y = self.y + (
                    (self.height / 2) - (self.font[0].render(self.text, True, (255, 255, 255)).get_height() / 2))
            painttext.rgb = self.font[1]
            painttext.gjc = self.font[2]
        painttext.paint()


class Progress_bar():
    def __init__(self, window, x, y, width, height, max_location, location):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_location = max_location
        self.location = location

    def mainloop(self):
        Rectangular(self.window, self.x, self.y, self.width, self.height, (175, 175, 175), 255).paint()
        Rectangular(self.window, self.x + 1, self.y + 1, self.width - 2, self.height - 2, (255, 255, 255), 255).paint()
        Rectangular(self.window, self.x + 1, self.y + 1,
                    ((self.width - 2) / self.max_location * self.location), self.height - 2,
                    (6, 176, 37), 255).paint()


class Select_box():
    def __init__(self, window, x, y, text, font=None, selected=None, common=None):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.selected = selected
        self.common = common
        self.event = None
        self.mousebuttondown = False

    def mainloop(self):
        if self.selected is None:
            self.selected = False
        font1 = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 14)
        Rectangular(self.window, self.x, self.y, 20, 20, (0, 0, 0), 255).paint()
        Rectangular(self.window, self.x + 1, self.y + 1, 20 - 2, 20 - 2, (255, 255, 255), 255).paint()
        if self.selected:
            Rectangular(self.window, self.x + 3, self.y + 3, 20 - 6, 20 - 6, (0, 0, 0), 255).paint()
        painttext = FillText(self.window, self.text, self.x + 24, self.y + (10 - font1.get_height() / 2), font1,
                             (0, 0, 0), True)
        if self.window.event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if self.x < pygame.mouse.get_pos()[0] < self.x + 20 and self.y < pygame.mouse.get_pos()[
            1] < self.y + 20 and self.event.type == pygame.MOUSEBUTTONDOWN and self.event.button == 1 and not self.mousebuttondown:
            self.selected = not self.selected
            if not self.common is None:
                self.common()
        if self.mousebuttondown and self.event.type == pygame.MOUSEBUTTONUP:
            self.mousebuttondown = False
        if (not self.mousebuttondown) and self.event.type == pygame.MOUSEBUTTONDOWN:
            self.mousebuttondown = True
        if not self.font is None:
            painttext.font = self.font[0]
            painttext.x = self.x + 2
            painttext.y = self.y
            painttext.rgb = self.font[1]
            painttext.gjc = self.font[2]
        painttext.paint()


class Picture_box():
    def __init__(self, window, x, y, width, height, common=None, img=None):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.commond = common
        self.img = img

    def mainloop(self):
        Rectangular(self.window.canvas, self.x, self.y, self.width, self.height, (240, 240, 240), 255)
        if not self.img is None:
            self.window.canvas.blit(self.img, (self.x, self.y), (0, 0, self.width, self.height))

print('''PyWin10UI 0.0.9 Python %s on %s
The PyWin10UI Development documentation:https://github.com/bytfr/pywin10ui''' % (sys.version, sys.platform))
