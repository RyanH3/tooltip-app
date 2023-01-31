from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager
from kivy.graphics import Color, Rectangle


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)


class MyScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(MyScrollView, self).__init__(**kwargs)
        self.do_scroll_y = 'True'
        self.size_hint_y = 0.88
        self.pos_hint = {'top': 1}


class SquareButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SquareButton, self).__init__(**kwargs)
        self.size_hint_y = None
        self.size_hint_x = None
        self.width = int(Window.width * 0.3)
        self.height = self.width
        self.allow_stretch = True


class BackButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.pos_hint = {'center_x': .25, 'center_y': .061}
        self.size_hint_y = None
        self.size_hint_x = None
        self.width = int(Window.width * 0.25)
        self.height = self.width
        self.source = 'icons/256x256pngFiles/Back/backTransparentNoCircle.png'
        self.allow_stretch = True


class HomeButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(HomeButton, self).__init__(**kwargs)
        self.pos_hint = {'center_x': .75, 'center_y': .061}
        self.size_hint_y = None
        self.size_hint_x = None
        self.width = int(Window.width * 0.25)
        self.height = self.width
        self.source = 'icons/256x256pngFiles/Home/homeTransparentNoCircle.png'
        self.allow_stretch = True


class Toolbar(Label):
    def __init__(self, **kwargs):
        super(Toolbar, self).__init__(**kwargs)
        self.size_hint = (1, .1)
        self.canvas.add(Color(.4, .4, .4, 1))
        self.canvas.add(Rectangle(size=(Window.width, (Window.height * .12)), pos_hint=self.pos_hint))


class AccordionLabel(Label):
    def __init__(self, **kwargs):
        super(AccordionLabel, self).__init__(**kwargs)
        self.color = (0, 0, 0, 1)
        self.font_size = '20sp'
        self.markup = True


class TooltipApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    TooltipApp().run()
