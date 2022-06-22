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
           'cor': color(96),
           },
         {'nome': 'gás carbônico',
           'formula': 'CO₂',
           'inicio': (20, 100, 255),
           'final':  (450, 300, 0),
           'cor': color(90),
           },
                     {'nome': 'Água',
           'formula': 'H₂O',
           'inicio': (200, 600, 255),
           'final':  (450, 50,0),
           'cor': color(12, 90, 242)
           },
    ]
 
def setup():
    fullScreen(0)
    #size(800, 600)  # 400 -> width / 2  300 -> height / 2
    print(width, height)
    textSize(30)
    textAlign(CENTER, CENTER)
    

def draw():
    background(255)
    noStroke()
    # BOLA
    fill(0, 100, 0, 128)
    circle(width/2, height/2, height / 2 + 50)
    
    # ATORES
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
    fill(0, 100,0)
    text("cloroplasto fotosintese", width / 2, height - 50)
    stroke(255, 255, 0)
    # SETAS
    m = width / 2
    strokeWeight(3)
    d = width / 24
    inicio = m - d * 2
    final = m + d * 2
    for x in range(inicio, final + 1, 25):
        y = d + d * sin(frameCount / 20.0)
        seta(x, height / 12 + y, x, height / 5 + y)
    fill(width/2, height/2, 0)
    if keyPressed:
        text('luz', width / 2, d * 4)

    
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
    
    
