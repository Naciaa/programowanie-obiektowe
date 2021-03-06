class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchPasiasty(self, x, y, paski): # dodajemy ilość pasków, w które ma być kwadrat
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej
        space = self.bok/paski # wyliczamy przerwę między paskami
        _xLinii_ = 0 # to jest pole chronione, nie powinno się go używać w kodzie po za klaą i klasami po niej dziedziczącymi 
        for pasek in range(0, paski): # dorysowujemy paski
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KwadratZKwadratem(Kwadrat): # klasa która rysuje małe kwadraty wewnątrz dużego kwadratu
    def sketchKwadratowy(self, x, y, ileKwadratow): #
        Kwadrat.sketch(self, x, y) #narysowanie dużego kwadratu korzystając z metody klasy bazowej
        self.bok = self.bok/ileKwadratow #wyliczenie długości boku małych kwadratów i zapisanie ich w zmiennej klasy bazowej
        for i in range(0, ileKwadratow): #stworzenie podwójnej pętli do 
            for j in range(0, ileKwadratow):
                Kwadrat.sketch(self, x + self.bok * j, y + self.bok * i) #wywołanie metody klasy bazowej
            
            
            
def setup():
    size(500, 500)
    #malyKwadrat = Kwadrat(50.0) # obiekt typu kwardrat o wielkości 50
    #malyKwadrat.sketch(200, 300) # rysujemy go w podanych wsółrzędnych
    #duzyKwadrat = Kwadrat(200.0)
    #duzyKwadrat.sketch(50, 75)
    #malyKwadrat.sketch(100, 200) # rysujemy kwadrat wielkości 50 również w innych współrzędnych
    #malyPasiastyKwadrat = PasiastyKwadrat(30.0) # tu tworzymy obiekt typu pasiasty kwadrat korzystając z konstruktora klasy bazowej
    #malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) # umieszczamy stworzony kwadrat w 5 pasków w tych współrzędnych
    #malyPasiastyKwadrat.sketchPasiasty(100,300, 8) # a teraz w 8 pasów w innych współrzędnych
    #duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    #duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    #duzyPasiastyKwadrat.sketch(350, 300) # na obiekcie typu klasy pochodnej można wywołać metodę klasy bazowej ( rysujemy kwadrat bez pasków )
    
    kwadratowyKwadrat = KwadratZKwadratem(150.0)
    kwadratowyKwadrat.sketchKwadratowy(300,300,  7)
    malyKwadratowyKwadrat = KwadratZKwadratem(100.0)
    malyKwadratowyKwadrat.sketchKwadratowy(15, 20, 2)
    malutkiKwadratowyKwadrat = PasiastyKwadrat(50.0)
    malutkiKwadratowyKwadrat.sketchPasiasty(140, 40, 3)
    
# ok, 2 pkt
