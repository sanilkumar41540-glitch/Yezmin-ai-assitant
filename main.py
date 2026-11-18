from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.04, 0.12, 1)

class YazminAI(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="YAZMIN AI",
            font_size=35,
            color=(0.2, 0.6, 1, 1)
        ))

        self.gemini = TextInput(
            hint_text="AI Brain API Key",
            password=True,
            multiline=False
        )
        layout.add_widget(self.gemini)

        self.eleven = TextInput(
            hint_text="ElevenLabs API Key",
            password=True,
            multiline=False
        )
        layout.add_widget(self.eleven)

        self.voice = TextInput(
            hint_text="ElevenLabs Voice ID",
            multiline=False
        )
        layout.add_widget(self.voice)

        layout.add_widget(Button(
            text="SAVE API SETTINGS",
            on_press=self.save_settings
        ))

        layout.add_widget(Button(
            text="START YAZMIN",
            background_color=(0.05, 0.4, 1, 1)
        ))

        return layout

    def save_settings(self, instance):
        with open("settings.txt", "w") as f:
            f.write(self.gemini.text + "\n")
            f.write(self.eleven.text + "\n")
            f.write(self.voice.text)

        instance.text = "SETTINGS SAVED"

YazminAI().run()
