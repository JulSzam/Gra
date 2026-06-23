klawisze = {}      #słownik na wcisniete klawisze
#---------------------------------------------------------------------------------------#paletki graczy
class paletka:
    def __init__(self, x, y, kolor_paletki, kolor_obrys):
        self.x = x
        self.y = y
        self.kolor = kolor_paletki
        self.kol = kolor_obrys
        self.promien = 30
        self.predkosc = 10
    
    def gracz_1_sterowanie(self):
        if klawisze.get('w'): self.y -= self.predkosc
        if klawisze.get('s'): self.y += self.predkosc
        if klawisze.get('a'): self.x -= self.predkosc
        if klawisze.get('d'): self.x += self.predkosc

        if self.x < self.promien:                     #kolizjie lewa sciana
            self.x = self.promien
        if self.x > width - self.promien:             #kolizjie prawa sciana
            self.x = width - self.promien
        if self.y < self.promien:                     #kolizjie góra sciana
            self.y = self.promien
        if self.y > (height / 2) - self.promien:      #kolizjie dół sciana
            self.y = (height / 2) - self.promien
        
    def gracz_2_sterowanie(self): 
        if klawisze.get(UP): self.y -= self.predkosc
        if klawisze.get(DOWN): self.y += self.predkosc
        if klawisze.get(LEFT): self.x -= self.predkosc
        if klawisze.get(RIGHT): self.x += self.predkosc

        if self.x < self.promien:                     #kolizjie lewa sciana
            self.x = self.promien
        if self.x > width - self.promien:             #kolizjie prawa sciana
            self.x = width - self.promien
        if self.y < (height / 2) + self.promien:      #kolizjie góra sciana
            self.y = (height / 2) + self.promien
        if self.y > height- self.promien:             #kolizjie dół sciana
            self.y = height - self.promien

    def model_paletki(self):
        self.kolor
        stroke(self.kol)
        strokeWeight(7)
        fill(self.kolor) 
        ellipse(self.x, self.y, self.promien * 2.5, self.promien * 2.5)
        noStroke()
        ellipse(self.x, self.y, self.promien * 2, self.promien * 2)
        stroke(self.kol)
        strokeWeight(5)
        ellipse(self.x, self.y, self.promien * 1, self.promien * 1)
#--------------------------------------------------------------------------------
class krazek:
        def __init__(self, x, y, kolor_krazka):
            self.x = x
            self.y = y
            self.kolor = kolor_krazka
            self.promien = 45
            self.predkosc = 10
            
        def ruch_krazka(self):
            self.x += self.predkosc
            self.y += self.predkosc

        def model_krazka(self):
            self.kolor
            noStroke()
            fill(self.kolor)
            ellipse(self.x,self.y,self.promien,self.promien)

#--------------------------------------------------------------------------------
class gra: #klasa, która ogarnia całą gre
    def __init__(self):
        self.gracz1 = paletka(width / 2, 100, color(239, 191, 16), color(206, 149, 19),) 
        self.gracz2 = paletka(width / 2, height - 100, color(228, 47, 209), color(126, 25, 168))
        self.krazek = krazek(width/2, height/2, color(55,55,55))
    def rysuj(self):
        stroke(30, 50)      #linie planszy
        strokeWeight(5)
        line(0, height / 2, width, height / 2)
        noFill()
        ellipse(width / 2, height / 2, 200, 200)

        self.gracz1.gracz_1_sterowanie()
        self.gracz1.model_paletki()
        self.gracz2.gracz_2_sterowanie()
        self.gracz2.model_paletki()
        self.krazek.model_krazka()
        self.krazek.ruch_krazka()

#-------------------------------------------------------------------------------
Gra = None      #to chyba musi być
def setup():
    size(1000, 800)
    global Gra
    Gra = gra() 

def draw():
    background(220) #bez tego robi się wąż z drogi paletki
    Gra.rysuj()

def keyPressed():
    if key == CODED:
        klawisze[keyCode] = True
    else:
        klawisze[str(key).lower()] = True  #nie ważne czy jest 'W' czy 'w' bedzie działać
        
def keyReleased():
    if key == CODED:
        klawisze[keyCode] = False
    else:
        klawisze[str(key).lower()] = False
