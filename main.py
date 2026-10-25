from kivy.app import App
from kivy.uix.button import Button

class NioHubTest(App):
    def build(self):
        return Button(text="Touchez-moi",
                      on_press=self.dit_bonjour)

    def dit_bonjour(self, bouton):
        bouton.text = "NioHub fonctionne !"

NioHubTest().run()
