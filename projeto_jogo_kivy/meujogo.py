from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window  import Window


class RebateBola(Widget):
    pontuacao = NumericProperty(0)
    def bola_saltitante(self, bola):
        if self.collide_widget(bola):
            velocidade_cima = 1.1
            desvio = 0.05 * Vector(0, bola.center_y - self.center_y)
            bola.velocidade = velocidade_cima * (desvio - bola.velocidade)


class PingPongJogo(Widget):
    bola = ObjectProperty(None)
    jogador_1 = ObjectProperty(None)
    jogador_2 = ObjectProperty(None)

    def serve_bola(self, vel=(4, 0)):
        self.bola.center = self.center  
        self.bola.velocidade = vel


    def atualizacao(self, dt):
        self.bola.move()

        self.jogador_1.bola_saltitante(self.bola)
        self.jogador_2.bola_saltitante(self.bola)

        if (self.bola.y < self.y) or (self.bola.top > self.top):
            self.bola.velocidade_y *= -1

        if self.bola.x < self.x:
            self.jogador_2.pontuacao += 1
            self.serve_bola(vel = (4, 0))
        if self.bola.right > self.width:
            self.jogador_1.pontuacao += 1
            self.serve_bola(vel = (4, 0))
        if self.jogador_1.pontuacao == 10:
            self.add_widget(Button(text="Sair", on_release= App.get_running_app().stop))
            self.serve_bola(vel=(0, 0))
        if self.jogador_2.pontuacao == 10:
            self.add_widget(Button(text="Sair", on_release= App.get_running_app().stop))
            self.serve_bola(vel=(0, 0))

    def on_touch_move(self, toque):
        if toque.x < self.width / 3:
            self.jogador_1.center_y = toque.y
        if toque.x > self.width / 3:
            self.jogador_2.center_y = toque.y


class BolaPong(Widget):
    #Velocidade da bola nos eixos x e y
    velocidade_x = NumericProperty(0)
    velocidade_y = NumericProperty(0)

# propriedade da lista de referência para que possamos usar velocidade
# da bola como uma abreviação, assim como, por exemplo, w.pos para 
# w.x e w.y
    velocidade = ReferenceListProperty(velocidade_x, velocidade_y)

    # A função ``move`` moverá a bola um passo. Isso será chamado
    # em intervalos iguais para animar a bola 
    def move(self):
        self.pos = Vector(*self.velocidade) + self.pos


class MeuJogoApp(App):
    def build(self):
        jogo = PingPongJogo()
        jogo.serve_bola()
        Clock.schedule_interval(jogo.atualizacao, 1.0 / 80.0)
        return jogo
        


if __name__ == "__main__":
    MeuJogoApp().run()
