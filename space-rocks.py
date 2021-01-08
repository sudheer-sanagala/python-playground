# https://docs.microsoft.com/en-us/learn/paths/introduction-python-space-exploration-nasa/

print("Artemis Rover Rock Scanner Starting")

basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []



def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt\n")
        basalt += 1
    elif("breccia" in rockToID):
        print("Found a breccia\n")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith\n")
        regolith += 1
    return

strPath = "rocks.txt"
fileObject = open(strPath)
rockList = fileObject.readlines()

for rock in rockList:
    #print(rock)
    countMoonRocks(rock)
fileObject.close()

print("Number of Basalt: ", basalt)
print("Number of Breccia: ", breccia)
print("Number of Highland: ", highland)
print("Number of Regolith: ", regolith)

print("The max number of one type of rock found was:", max(basalt, breccia, highland,regolith))
print("The minimum number of one type of rock found was:", min(basalt, breccia, highland, regolith))
