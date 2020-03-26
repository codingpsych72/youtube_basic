import pytube
import kivy
from kivy.app import App
import kivy.uix.button,kivy.uix.label,kivy.uix.textinput,kivy.uix.boxlayout,kivy.uix.gridlayout,kivy.uix.button
from kivy.uix.gridlayout import GridLayout
from pytube import YouTube

class YtdApp(App):
    def build(self):
        self.label1 = kivy.uix.label.Label(text="youtube downloader app")
        self.textInput1 =kivy.uix.textinput.TextInput(text="delete me-> and paste the link")
        self.boxlayout = GridLayout(cols=3)
        self.boxlayout=kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.button1=kivy.uix.button.Button(text="start downloading")
        self.boxlayout.add_widget(self.label1)
        self.boxlayout.add_widget(self.textInput1)
        self.boxlayout.add_widget(self.button1)
        self.button1.bind(on_press=self.downloadable)
        return self.boxlayout

    def downloadable(self,btn):
        path = "/home/lee/Videos"
        link=self.textInput1.text
        yt = pytube.YouTube(link)
        down = yt.streams.first()
        down.download(path)





if __name__=="__main__":
    yta=YtdApp()
    yta.run()
