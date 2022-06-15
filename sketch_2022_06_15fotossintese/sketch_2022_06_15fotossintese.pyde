from __future__ import unicode_literals

atores = [
           {'nome': 'Glicose',
           'formula': 'C₆H₁₂O₆',
           'inicio': (300, 300, 0),
           'final':  (650, 200, 255),
           'cor': color(232, 12, 71)
           },
          {'nome': 'Oxigênio',
           'formula': 'O₂',
           'inicio': (300, 350, 0),
           'final':  (650, 400, 255),
           'cor': color(200),
           },
         {'nome': 'gás carbônico',
           'formula': 'CO₂',
           'inicio': (20, 100, 255),
           'final':  (450, 300, 0),
           'cor': color(200),
           },
                     {'nome': 'Água',
           'formula': 'H₂O',
           'inicio': (200, 600, 255),
           'final':  (450, 50,0),
           'cor': color(12, 90, 242)
           },
    ]

def setup():
    size(800, 600)
    textSize(30)
    textAlign(CENTER, CENTER)
    

def draw():
    background(0)
    noStroke()
    fill(0, 250, 0, 30)
    circle(400, 300, 500)
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
    text("cloropasto fotosintese", 400, 550)
    print(mouseX, mouseY)
    stroke(255, 255, 0)
    for x in range(350, 451, 25):
        y = 25 + 25 * sin(frameCount / 20.0)
        seta(x, 50 + y, x, 150 + y)
    fill(255, 255, 0)
    if keyPressed:
        text('luz', 400, 100)

    
def seta(xa, ya, xb, yb):
    tam_seta = dist(xa, ya, xb, yb)
    ang = atan2(yb - ya, xb - xa)
    line(xa, ya, xb, yb)
    pushMatrix() 
    translate(xb, yb)
    rotate(ang)
    tam_ponta = tam_seta / 10 
    line(0, 0, -tam_ponta, tam_ponta)
    line(0, 0, -tam_ponta, -tam_ponta)
    popMatrix()    
    
    
