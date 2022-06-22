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
           'cor': color(0),
           },
         {'nome': 'gás carbônico',
           'formula': 'CO₂',
           'final': (110, 80, 255),
           'inicio':  (400, 300, 30),
           'cor': color(0),
           },
        {'nome': 'ATP',
           'formula': 'ATP',
           'inicio': (400, 300, 0),
           'final':  (700, 450, 255),
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
    fullScreen(0)
    #size(800, 600)
    print(width, height)
    textSize(30)
    textAlign(CENTER, CENTER)
    

def draw():
    background(255)
    noStroke()
    fill(128, 42, 46, 64)
    circle(width/2, height/2, height / 2 + 50)
    d = width / 24

    t = constrain(frameCount % 400 / 300.0, 0, 1)
    for ator in atores:
        if keyPressed:
            texto = ator['formula']
        else:
            texto = ator['nome']
        xip, yip, opacidadei = ator['inicio']
        xfp, yfp, opacidadef = ator['final']
        cor = ator['cor']
        xi = map(xip, 0, 800, 0, width)
        yi = map(yip, 0, 600, 0, height)
        xf = map(xfp, 0, 800, 0, width)
        yf = map(yfp, 0, 600, 0, height)
        x = lerp(xi, xf, t)
        y = lerp(yi, yf, t)
        opa = lerp(opacidadei, opacidadef, t)
        fill(cor, opa)
        text(texto, x, y)
    fill(71, 255,0)
    

    fill(0, 100,0)
    text("mitocôndria - respiração celular", 
         width / 2, height - 2 * d)
    
