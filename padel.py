spillere = ["Rithaann", "Leon", "Kenneth", "Phu", "Adam", "Aibo", "Odin", "Jonathan", "Anarththan", "Mika", "Jonna", "Apisan"]

# print(len(spillere))

bane1 = spillere[0:4]
bane2 = spillere[4:8]
bane3 = spillere[8:12]
# print(f"Bane 1: {bane1}")
# print(f"Bane 2: {bane2}")
# print(f"Bane 3: {bane3}")

# print(f"Bane 1: {bane1[0]} & {bane1[1]} vs {bane1[2]} & {bane1[3]}")



def visBane(nummer, bane):
    print(f"Bane {nummer}: {bane[0]} & {bane[1]} vs {bane[2]} & {bane[3]} ")
    
visBane(3,bane3)

baner = [bane1,bane2,bane3]

for i in range(len(baner)):
    visBane(i+1, baner[i])

    