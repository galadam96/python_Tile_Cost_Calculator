#Find Cost of Tile to Cover W x H Floor
#magasság

while True:
    
    height = input("Magasság: ")
    try: 
        height = int(height)
        break
    except: 
        print("Csak számot adj meg!")
        continue
    
#szélesség

while True:
    width = input("Szélesség: ")
    try: 
        width = int(width)
        break
    except: 
        print("Csak számot adj meg!")
        continue
    
#ár 

while True:
    ar = input("Mennyibe kerül 1 nm? ")
    try:
        ar = int(ar)
        break
    except:
        print("Számot adj meg.")
        continue
    
# Ha mindkét számot sikerült elrakni
terulet = width * height
koltseg = terulet * ar
print(f'A teljes terület:{terulet} nm')
print(f'Költség: {koltseg}')
