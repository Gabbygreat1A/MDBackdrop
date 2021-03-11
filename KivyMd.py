from kivy.lang import Builder
from kivymd.app import MDApp

kv = '''
#:import Window kivy.core.window.Window
MDScreen:
    MDBackdrop:
        id: backdrop
        on_close: self.title = 'Pycified Services'
        header: False
        right_action_items: [['dots-vertical', lambda x: print('dot')]]
        title: 'Pycified Services'
        bold: True
        radius_left: 0
        radius_right: 0
        MDBackdropBackLayer:
            ScreenManager:
                id: manage
                Codes:
                    name: 'codes'
                Electronics:
                    name: 'electronics'
                Clothings:
                    name: 'clothings'
                Gadgets:
                    name: 'gadgets'
                Books:
                    name: 'books'
                Musicals:
                    name: 'musicals'
                Foods:
                    name: 'foods'
        MDBackdropFrontLayer:
            ScrollView:
                do_scroll_y: False
                MDList:
                    TwoLineAvatarIconListItem:
                        text: 'Codes'
                        secondary_text: '10.6% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open(0)
                            manage.current = 'codes'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'code-braces'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Electronics'
                        secondary_text: '20% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'electronics'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'television'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Clothings'
                        secondary_text: '23.7% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'clothings'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'tshirt-crew'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Gadgets'
                        secondary_text: '10.6% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'gadgets'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'cellphone-android'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Books'
                        secondary_text: '19% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'books'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'book'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Musicals'
                        secondary_text: '15.7% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'musicals'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'guitar-electric'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                    TwoLineAvatarIconListItem:
                        text: 'Foods'
                        secondary_text: '10.2% Discount'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        on_release:
                            backdrop.open()
                            manage.current = 'foods'
                            app.title_change(self.text)
                        IconLeftWidget:
                            icon: 'food'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        IconRightWidget:
                            icon: 'check-bold'
                            theme_text_color: 'Custom'
                            text_color: app.theme_cls.primary_color
                        
<Codes@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Codes Screen'
            halign: 'center'
<Electronics@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Electronics Screen'
            halign: 'center'
<Clothings@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Clothings Screen'
            halign: 'center'
<Gadgets@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Gadgets Screen'
            halign: 'center'
<Books@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Books Screen'
            halign: 'center'
<Musicals@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Musicals Screen'
            halign: 'center'
<Foods@MDScreen>
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_dark
        MDLabel:
            text: 'This is A Foods Screen'
            halign: 'center'
'''


class MainApp(MDApp):
    def build(self):
        self.close_ = True
        return Builder.load_string(kv)

    def title_change(self, title):
        self.root.ids.backdrop.title =  title

MainApp().run()
