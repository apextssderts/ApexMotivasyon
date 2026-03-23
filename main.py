from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from random import choice

# Karanlık tema başlangıç
Window.clearcolor = (0.05, 0.05, 0.15, 1)  # Hafif lacivert-mavi

sozler = [
    "Senin gibi adamlar dünyayı değiştirir, devam et!",
    "Her sabah yeni bir başlangıç, kalk ve yap!",
    "Pes etmek yok, yol uzun ama sen güçlüsün.",
    "Küçük adımlar büyük zafer getirir, inan bana.",
    "Bugün yorulursun, yarın gurur duyarsın.",
    "Hayallerin peşinden git, onlar seni bekliyor.",
    "Sen başaracaksın, çünkü vazgeçmiyorsun.",
    "Zor günler geçer, kazanan sensin.",
    "Gülümse, dünya seninle değişir.",
    "Devam et reis, zirve yakın!"
]

class MotivasyonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=40, adaptive_height=True)
        
        self.label = MDLabel(
            text="Butona bas, motive ol!",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H5",
            markup=True,
            size_hint_y=None,
            height=200
        )
        
        button = MDFlatButton(
            text=">",
            pos_hint={"center_x": 0.5},
            md_bg_color=(0.3, 0.6, 1, 1),  # Mavi buton
            text_color=(1, 1, 1, 1),
            font_size=50,
            size_hint=(0.3, None),
            height=100,
            on_release=self.yeni_soz
        )
        
        layout.add_widget(self.label)
        layout.add_widget(button)
        self.add_widget(layout)
    
    def yeni_soz(self, instance):
        soz = choice(sozler)
        self.label.text = f"[b]{soz}[/b]"
        # Hafif renk değişimi (mavi tonları)
        colors = [(0.05, 0.05, 0.2, 1), (0.1, 0.2, 0.4, 1), (0.0, 0.3, 0.5, 1)]
        Window.clearcolor = choice(colors)

class MotivasyonApp(MDApp):
    def build(self):
        return MotivasyonScreen()

if __name__ == "__main__":
    MotivasyonApp().run()
