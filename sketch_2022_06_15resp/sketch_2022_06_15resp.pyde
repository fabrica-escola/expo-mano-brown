from __future__ import unicode_literals

atores = [
           {'nome': 'Glicose',
           'formula': 'C₆H₁₂O₆',
           'final': (300, 200, 0),
           'inicio':  (450, 300, 255),
           'cor': color(232, 12, 71)
           },
          {'nome': 'Oxigênio',
           'formula': 'O₂',
           'final': (300, 400, 0),
           'inicio':  (450, 200, 255),
           'cor': color(200),
           },
         {'nome': 'gás carbônico',
           'formula': 'CO₂',
           'final': (20, 100, 255),
           'inicio':  (400, 300, 30),
           'cor': color(200),
           },
                     {'nome': 'ATP',
           'formula': 'ATP',
           'inicio': (400, 300, 0),
           'final':  (500, 500, 255),
           'cor': color(12, 90, 242)
           },
    
         # {'nome': 'respiração celular',
         #   'formula': 'O₂',
         #   'inicio': (100, 350, 0),
         #   'final':  (400, 268, 255),
         #   'cor': color(50),
         #   },
         
    ]      
          
def setup():
    size(800, 600)
    textSize(30)
    textAlign(CENTER, CENTER)
    

def draw():
    background(0)
    t = constrain(frameCount % 400 / 300.0, 0, 1)
    for ator in atores:
        if keyPressed:
            texto = ator['formula']
        else:
            texto = ator['nome']
        xi, yi, opacidadei = ator['inicio']
        xf, yf, opacidadef = ator['final']
        cor = ator['cor']
        x = lerp(xi, xf, t)
        y = lerp(yi, yf, t)
        opa = lerp(opacidadei, opacidadef, t)
        fill(cor, opa)
        text(texto, x, y)
    fill(71, 255,0)
    text("respiração celular", 400, 580)
    print(mouseX, mouseY)
    
    
    
    
    
