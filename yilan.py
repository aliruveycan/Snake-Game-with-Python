import pygame
import random

# Oyun alanı boyutları
GENISLIK = 800
YUKSEKLIK = 600

# Renkler
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)

class Yilan:
    def __init__(self):
        self.boyut = 20
        self.hiz = 20
        self.yilan = [[GENISLIK / 2, YUKSEKLIK / 2]]
        self.yon = "sol"

    def hareket(self):
        if self.yon == "yukari":
            self.yilan[0][1] -= self.hiz
        elif self.yon == "asagi":
            self.yilan[0][1] += self.hiz
        elif self.yon == "sol":
            self.yilan[0][0] -= self.hiz
        elif self.yon == "sag":
            self.yilan[0][0] += self.hiz

    def kontrol(self):
        if self.yilan[0][0] < 0 or self.yilan[0][0] >= GENISLIK or self.yilan[0][1] < 0 or self.yilan[0][1] >= YUKSEKLIK:
            return False
        return True

    def ciz(self, ekran):
        for parca in self.yilan:
            pygame.draw.rect(ekran, SIYAH, [parca[0], parca[1], self.boyut, self.boyut])

    def uzat(self):
        self.yilan.append([self.yilan[-1][0], self.yilan[-1][1]])

class Oyun:
    def __init__(self):
        pygame.init()
        self.ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
        pygame.display.set_caption("Yılan Oyunu")
        self.saat = pygame.time.Clock()
        self.yilan = Yilan()
        self.yem = [random.randrange(0, GENISLIK, 20), random.randrange(0, YUKSEKLIK, 20)]
        self.puan = 0

    def basla(self):
        oyun_devam = True
        while oyun_devam:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_devam = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.yilan.yon != "asagi":
                        self.yilan.yon = "yukari"
                    elif event.key == pygame.K_DOWN and self.yilan.yon != "yukari":
                        self.yilan.yon = "asagi"
                    elif event.key == pygame.K_LEFT and self.yilan.yon != "sag":
                        self.yilan.yon = "sol"
                    elif event.key == pygame.K_RIGHT and self.yilan.yon != "sol":
                        self.yilan.yon = "sag"

            self.yilan.hareket()
            self.ekran.fill(BEYAZ)
            pygame.draw.rect(self.ekran, KIRMIZI, [self.yem[0], self.yem[1], self.yilan.boyut, self.yilan.boyut])

            if self.yilan.yilan[0] == self.yem:
                self.yilan.uzat()
                self.yem = [random.randrange(0, GENISLIK, 20), random.randrange(0, YUKSEKLIK, 20)]
                self.puan += 1

            if not self.yilan.kontrol():
                oyun_devam = False

            self.yilan.ciz(self.ekran)
            pygame.display.update()
            self.saat.tick(10)

        pygame.quit()

if __name__ == "__main__":
    oyun = Oyun()
    oyun.basla()
