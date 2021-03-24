from kivy.lang.builder import Builder
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import certifi
import os

# Here's all the magic !
os.environ['SSL_CERT_FILE'] = certifi.where()

#Window.size = (300, 500)

screen_helper = '''                 
MDBoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "Dados Github"
        elevation: 8
    ScreenManager:
        InicialScreen:
        ProfileScreen:
        
<InicialScreen>:
    name: 'inicial'
    Screen:
    MDIconButton:
        icon: "git"
        user_font_size: '70sp'
        pos_hint: {"center_x": .5, "center_y": .8}
        
    MDTextField:
        id: usuario
        required: True
        hint_text: "Usuario GitHub"
        helper_text: "Ex. leoobrabo"
        helper_text_mode: "on_focus"
        size_hint_x: .5
        size_hint_y: .1
        max_text_length: 40
        color_mode: 'accent'
        line_color_normal: app.theme_cls.accent_color
        mode: "rectangle"
        pos_hint: {"center_x": .5, "center_y": .5}
        icon_right: 'account' 
    MDRectangleFlatIconButton:
        icon: "account-search"
        text: "Buscar"
        pos_hint: {"center_x": .5, "center_y": .25}
        on_release:  root.manager.current = 'profile'
        on_press: root.req_git()   
        
<ProfileScreen>:
    on_enter: root.dados()
    name: 'profile'
    Screen:
    AsyncImage:
        id: avatar
        size_hint_x: .43
        size_hint_y: .2
        pos_hint: {"x": .04, "center_y": .88}
        source: ""
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Nome'
        icon: "nature-people"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .7}      
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Compania'
        icon: "domain"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .6}
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Localização'
        icon: "home-group"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .5}    
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Repositorios'
        icon: "source-repository"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .4}    
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Gists'
        icon: "book"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .3}
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Seguidores'
        icon: "account-group-outline"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .2}
    MDRectangleFlatIconButton:
        size_hint_x: .43
        size_hint_y: .09
        text: 'Seguindo'
        icon: "account-multiple-plus"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .1}  
    MDLabel:
        id: nome
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .7}     
    MDLabel:
        id: compania
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .6}    
    MDLabel:
        id: localizacao
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .5}   
    MDLabel:
        id: repositorios
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .4}     
    MDLabel:
        id: gists
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .3}    
    MDLabel:
        id: seguidores
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .2}   
    MDLabel:
        id: seguindo
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .65, "center_y": .1}  
'''


class InicialScreen(MDScreen):

    def req_git(self, *args):
        print('aqui1')
        global usuario, name
        global repos
        global avatar
        global compania
        global localizacao
        global bio
        global gists
        global seguindo
        global seguidores
        usuario = self.ids.usuario.text
        print(usuario)
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        try:
            res = session.get(f'https://api.github.com/users/{usuario}').json()
            name = res['name']
            repos = res['public_repos']
            avatar = res["avatar_url"]
            compania = res["company"]
            localizacao = res["location"]
            bio = res["bio"]
            gists = res["public_gists"]
            seguidores = res["followers"]
            seguindo = res["following"]
            print(res["created_at"])
            print(res["updated_at"])
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
            renewIPadress()

        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
            renewIPadress()

        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
            renewIPadress()

        except KeyboardInterrupt:
            print("Someone closed the program")


class ProfileScreen(MDScreen):

    def dados(self, *args):
        print('aqui2')
        print(self.name)
        self.ids.nome.text = str(name)
        self.ids.compania.text = str(compania)
        self.ids.localizacao.text = str(localizacao)
        self.ids.repositorios.text = str(repos)
        self.ids.gists.text = str(gists)
        self.ids.seguidores.text = str(seguidores)
        self.ids.seguindo.text = str(seguindo)
        self.ids.avatar.source = str(avatar)

    def on_enter(self, *args, **kwargs):
        pass


sm = ScreenManager()
sm.add_widget(InicialScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class GitHub(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(screen_helper)


if __name__ == '__main__':
    GitHub().run()
