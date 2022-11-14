#Path to your .map file
mapfile = 'C:\\Games\\ElDewrito\\Halo Online\\mods\\maps\\Guardian-Items\\sandbox.map'

def byte2ascii(hval):
    ascii_object = hval.decode("utf-8")

    return ascii_object

def byte2int(hval):
    int_object = int.from_bytes(hval, "little")

    return int_object

#0x0048 32byte Map Name
#0x0068 64byte Map Description
#0x00E8 16byte Map Author

with open(mapfile, "r+b") as f:
    f.seek(0x0048, 0)
    mapName = f.read(32)
    f.seek(0x0068, 0)
    mapDescription = f.read(128)
    f.seek(0x00E8, 0)
    mapAuthor = f.read(16)

    #Map ID
    f.seek(0x0228, 0)
    mapId = f.read(4)

    #Object Data
    f.seek(0x0242, 0)
    mapScnrObjectCount = f.read(2)
    
    #Total Objects
    f.seek(0x0244, 0)
    mapTotalObject = f.read(2)

    #Budget
    f.seek(0x0246, 0)
    mapBudgetCount = f.read(2)


    f.seek(0xD4A06, 0)
    mysteryByte = f.read(30)
    #print(byte2int(mysteryByte))

    print("Name: " + byte2ascii(mapName))
    print("Description: " + byte2ascii(mapDescription))
    print("Author: " + byte2ascii(mapAuthor))

    print("Map ID: " + str(byte2int(mapId)))
    print("ScnrObjCount: " + str(byte2int(mapScnrObjectCount)))
    print("MapBudgetCount: " + str(byte2int(mapBudgetCount)))
