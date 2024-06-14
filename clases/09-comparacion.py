class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, x): #igual que ===
        return  self.lat == x.lat and self.lon == x.lon

    def __ne__(self, x): # diferente !=
        return self.lat != x.lat or self.lon != x.lon

    def __lt__(self, x): #<, >, >= <=
        return self.lat + self.lon < x.lat + x.lon

coords = Coordenadas(45, 88)
coords2 = Coordenadas(45, 72)

print(coords == coords2)
print(coords != coords2)
print(coords < coords2)