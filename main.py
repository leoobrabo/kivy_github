from kivy.app import App
#from kivy.core.window import Window
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

#Window.size = (300, 500)

screen_helper = '''                 
MDBoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "Dados Github"

        right_action_items: [['lightbulb-outline', lambda x: app.color()]]
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
        font_size: "18sp"
        pos_hint: {"center_x": .5, "center_y": .25}
        #on_release:  root.manager.current = 'profile'
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
        size_hint_x: .35
        size_hint_y: .09
        text: 'Nome'
        icon: "nature-people"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .7}      
    MDRectangleFlatIconButton:
        size_hint_x: .35
        size_hint_y: .09
        text: 'Compania'
        icon: "domain"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .6}
    MDRectangleFlatIconButton:
        size_hint_x: .35
        size_hint_y: .09
        text: 'Localização'
        icon: "home-group"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .5}    
    MDRectangleFlatIconButton:
        size_hint_x: .35
        size_hint_y: .09
        text: 'Repositorios'
        icon: "source-repository"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .4}    
    MDRectangleFlatIconButton:
        size_hint_x: .35
        size_hint_y: .09
        text: 'Gists'
        icon: "book"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .3}
    MDRectangleFlatIconButton:
        size_hint_x: .35
        size_hint_y: .09
        text: 'Seguidores'
        icon: "account-group-outline"
        user_font_size: '10sp'
        pos_hint: {"x": .1, "center_y": .2}
    MDRectangleFlatIconButton:
        size_hint_x: .35
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
        pos_hint: {"x": .55, "center_y": .7}     
    MDLabel:
        id: compania
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .6}    
    MDLabel:
        id: localizacao
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .5}   
    MDLabel:
        id: repositorios
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .4}     
    MDLabel:
        id: gists
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .3}    
    MDLabel:
        id: seguidores
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .2}   
    MDLabel:
        id: seguindo
        size_hint_x: .43
        size_hint_y: .1
        text: ''
        icon: "github"
        user_font_size: '10sp'
        pos_hint: {"x": .55, "center_y": .1}  
'''


class InicialScreen(MDScreen):

    def on_release(self):
        #print('mudando tela')
        self.parent.current = 'profile'

    def back(self):
        self.manager = 'menu'

    def req_git(self, *args):
        # print('aqui1')
        global usuario
        global name
        global repos
        global avatar
        global compania
        global localizacao
        global bio
        global gists
        global seguindo
        global seguidores

        usuario = self.ids.usuario.text

        if usuario == '':
            #print('Digite um valor valido')
            self.back()

        else:
            # print(usuario)
            search_url = f"https://api.github.com/users/{usuario}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            self.request = UrlRequest(search_url, req_headers=headers)
            self.request.wait()
            # print(self.request)
            # print(self.request.result)
            name = self.request.result['name']
            login = self.request.result['login']
            avatar = self.request.result['avatar_url']
            link = self.request.result['html_url']
            repos = self.request.result['public_repos']
            compania = self.request.result['company']
            localizacao = self.request.result['location']
            bio = self.request.result['bio']
            gists = self.request.result['public_gists']
            seguidores = self.request.result['followers']
            seguindo = self.request.result['following']
            self.on_release()

        # print(res["created_at"])
        # print(res["updated_at"])


class ProfileScreen(MDScreen):

    def dados(self, *args):
        # print('aqui2')
        # print(self.name)
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
        self.theme_cls.theme_style = 'Light'
        return Builder.load_string(screen_helper)

    def color(self):
        style = self.theme_cls.theme_style
        if style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    GitHub().run()
