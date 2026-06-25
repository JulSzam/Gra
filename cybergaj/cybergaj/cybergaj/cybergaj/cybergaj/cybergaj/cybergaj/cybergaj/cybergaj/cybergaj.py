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
            self.predkosc_x = 5
            self.predkosc_y = 5
            
        def ruch_krazka(self):
            self.x += self.predkosc_x
            self.y += self.predkosc_y
            
            if self.y <=0 + self.promien/2 and self.x <= 350 or self.y <=0 + self.promien/2 and self.x >= 650 or self.y >= height-self.promien/2 and self.x <= 350 or self.y >= height-self.promien/2 and self.x >=650:
                self.predkosc_y *= -0.9 #odbicie góra i dół pomijając bramki
            if self.x <0 + self.promien/2 or self.x >=width-self.promien/2:
                self.predkosc_x *= -0.9 #odbicie prawo i lewo
            
            if self.y <=0 + self.promien/2 and self.x >=350 and self.x <=650:
                self.x = width/2
                self.y = height/2
                self.predkosc_x = 5
                self.predkosc_y = 5
            if self.y >=height-self.promien/2 and self.x >= 350 and self.x <=650:
                self.x = width/2
                self.y = height/2
                self.predkosc_x = 5
                self.predkosc_y = -5
                #reset pozycji krążka po trafieniu w bramkę
            if self.y <= 0 or self.y >= height or self.x <= 0 or self.x >= width:
                self.x = width/2
                self.y = height/2
                self.predkosc_x = 5
                self.predkosc_y = 5
                
        def kolizja_z_paletka(self,p):
            promien_paletki = p.promien * 1.25
            dx = self.x - p.x
            dy = self.y - p.y
            odleglosc = sqrt (dx * dx + dy * dy)
            suma_promieni = self.promien / 2 + promien_paletki
            
            if odleglosc < suma_promieni and odleglosc > 0:
                nx = dx / odleglosc
                ny = dy / odleglosc
                
                przenikniecie = suma_promieni - odleglosc
                self.x += nx * przenikniecie
                self.y += ny * przenikniecie
                #bez tego przenikają przez siebie
                
                predkosc_normalna = self.predkosc_x * nx + self.predkosc_y * ny
                self.predkosc_x = (self.predkosc_x - 2 * predkosc_normalna *nx) * 1.05
                self.predkosc_y = (self.predkosc_y - 2 * predkosc_normalna * ny) * 1.05
                # odbicie i przyspieszenie
                
                maks_predkosc = 20
                if abs(self.predkosc_x) > maks_predkosc:
                    self.predkosc_x = maks_predkosc * (1 if self.predkosc_x > 0 else -1)
                if abs(self.predkosc_y) > maks_predkosc:
                    self.predkosc_y = maks_predkosc * (1 if self.predkosc_y > 0 else -1)
                

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
        rect (350, 0, 300, 20)
        rect (350, height- 20, 300, 20)

        self.gracz1.gracz_1_sterowanie()
        self.gracz1.model_paletki()
        self.gracz2.gracz_2_sterowanie()
        self.gracz2.model_paletki()
        #paletki
        self.krazek.kolizja_z_paletka(self.gracz1)
        self.krazek.kolizja_z_paletka(self.gracz2)
        #kolizje
        self.krazek.model_krazka()
        self.krazek.ruch_krazka()
        #krazek

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
