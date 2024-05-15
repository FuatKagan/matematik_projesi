import pygame
import sys
import time
import math

# Asker sınıfı
class Asker:
    def __init__(self, numara, aci, merkez, yaricap):
        self.numara = numara
        self.aci = aci
        self.merkez = merkez
        self.yaricap = yaricap

        # Askerin pozisyonunu hesapla
        self.pozisyon = (self.merkez[0] + self.yaricap * math.cos(math.radians(self.aci)),
                         self.merkez[1] + self.yaricap * math.sin(math.radians(self.aci)))

# Ekran boyutları
WIDTH, HEIGHT = 1000, 800

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ekranı güncelleme fonksiyonu
def ekran_guncelle(askerler):
    screen.fill(WHITE)
    for asker in askerler:
        pygame.draw.circle(screen, BLACK, asker.pozisyon, 20)
        font = pygame.font.SysFont(None, 30)
        text = font.render(str(asker.numara), True, RED)
        screen.blit(text, (asker.pozisyon[0]-10, asker.pozisyon[1]-10))
    pygame.display.flip()

# Josephus Problemi'ni simüle eden fonksiyon
def josephus(n, k):
    merkez = (WIDTH // 2, HEIGHT // 2)  # Dairenin merkezi
    yaricap = min(merkez) - 50  # Dairenin yarıçapı

    aci_araligi = 360 // n  # Askerlerin arasındaki açı farkı

    askerler = [Asker(i, i * aci_araligi, merkez, yaricap) for i in range(1, n+1)]
    index = 0
    while len(askerler) > 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ekran_guncelle(askerler)
        time.sleep(1)  # Görsel simülasyonu yavaşlatmak için
        index = (index + k - 1) % len(askerler)
        asker_silinen = askerler.pop(index)
        print(f"{asker_silinen.numara}. asker öldü.")
    print(f"Kalan asker: {askerler[0].numara}")
    time.sleep(2)  # Görsel sonucu göstermek için bekle
    pygame.quit()

# Pencere oluşturma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Josephus Problemi Simülasyonu")

# Simülasyon başlatma
n = int(input("Asker sayısını girin: "))
k = int(input("Her turda kaçıncı askeri öldüreceğinizi girin: "))

josephus(n, k)
