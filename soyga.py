#----------------------------------------------------
# Program to generate the tables of the Book of Soyga
# Author: rey.olivier@gmail.com
# Date: February 2024
# License: GNU GPL v3
# Based on the paper from Jim Reeds (1998)
# John Dee and the Magic tables in the Book of Soyga
#----------------------------------------------------
import math
from PIL import Image, ImageDraw


#=============================================================Constants

# The standard alphabet at the time of John Dee
#         1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
CHARS = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','x','y','z']

COLORS = [
    (255, 0, 0),
    (255, 67, 0),
    (255, 133, 0),
    (255, 200, 0),
    (244, 255, 0),
    (177, 255, 0),
    (111, 255, 0),
    (44, 255, 0),
    (0, 255, 22),
    (0, 255, 89),
    (0, 255, 155),
    (0, 255, 222),
    (0, 222, 255),
    (0, 155, 255),
    (0, 89, 255),
    (0, 22, 255),
    (44, 0, 255),
    (111, 0, 255),
    (177, 0, 255),
    (244, 0, 255),
    (255, 0, 200),
    (255, 0, 133),
    (255, 0, 67)
]


# The decrypting offset found by Jim Reeds (!)
OFFSET = {
    'a':2,
    'b':2,
    'c':3,
    'd':5,
    'e':14,
    'f':2,
    'g':6,
    'h':5,
    'i':14,
    'k':15,
    'l':20,
    'm':22,
    'n':14,
    'o':8,
    'p':13,
    'q':20,
    'r':11,
    's':8,
    't':8,
    'u':15,
    'x':15,
    'y':15,
    'z':2
}

KEYWORDS = [
    # astrological signs
    (1, "Aries",  "NISRAM"),
    (2, "Taurus", "ROELER"),
    (3, "Gemini", "IOMIOT"),
    (4, "Cancer", "ISIAPO"),
    (5, "Leo",    "ORRASE"),
    (6, "Virgo",  "OSACUE"),
    (7, "Libra",  "XUAUIR"),
    (8, "Scorpio",     "RAOSAC"),
    (9, "Sagitarius",  "RSADUA"),
    (10, "Capricornus","ATROGA"),
    (11, "Aquarius",   "SDUOLO"),
    (12, "Pisces",     "ARICAA"),

    (13, "Aries",  "MARSIN"), #inverse
    (14, "Taurus", "RELEOR"), #inverse
    (15, "Gemini", "TOIMOI"), #inverse
    (16, "Cancer", "OPAISI"), #inverse
    (17, "Leo",    "ESARRO"), #inverse
    (18, "Virgo",  "EUCASO"), #inverse
    (19, "Libra",  "RIUAUX"), #inverse
    (20, "Scorpio",    "CASOAR"), #inverse
    (21, "Sagitarius", "AUDASR"), #inverse
    (22, "Capricornus","AGORTA"), #inverse
    (23, "Aquarius",   "OLOUDS"), #inverse
    (24, "Pisces",     "AACIRA"), #inverse

    # planets
    (25, "Saturni", "OSRESO"),
    (26, "Jovis",   "NIEBOA"),
    (27, "Martis",  "OIAIAE"),
    (28, "Solis",   "ITIABA"),
    (29, "Veneris", "ADAMIS"),
    (30, "Mercurii","REUELA"),
    (31, "Lunae",   "UISEUA"),

    #elements
    (32, "Ignis",  "MERONF"),
    (33, "Aeris",  "ILIOSU"),
    (34, "Aquae",  "OYNIND"),
    (35, "Terrai", "IASULA"),

    (36, "Magistri", "MOYSES")
]

OUTPUTFILE = "book-of-soyga-tables.txt"

#=============================================================Functions
def createGrid(n):
    '''
    Returns a square grid full of 0
    Is used with n=36 in the book of Soyga
    '''
    return [[0] * n for x in range(n)]


def getValue(letter):
    '''
    The value in the aphabet of the time
    '''
    theletter = letter.lower()
    return CHARS.index(theletter) + 1


def getColor(letter):
    theletter = letter.lower()
    return COLORS[CHARS.index(theletter)]

    
def calculateValue(text):
    value = 0
    for letter in text:
        if letter.lower() in CHARS:
            print(letter, end=": ")
            val = getValue(letter.lower())
            print(val)
            value += val
    print("Value for '" + text + "': " + str(value))
    return value


def test_getValue():
    print('Index of a: ' + str(getValue('a')))
    print('Index of J: ' + str(getValue('U')))
    print('Index of Z: ' + str(getValue('Z')))


def f(letter):
    '''
    The 'f' function of Jim Reeds' paper
    '''
    return OFFSET[letter.lower()]


def fillFirstColumn(grid, keyword):
    '''
    The first column is filled with the generating keyword and its inverse
    '''
    inv = keyword[::-1]
    pattern = (keyword + inv) * 3
    #print(pattern)
    num = 0
    for car in pattern:
        grid[num][0] = car.lower()
        num += 1


def myprint(text, end='\n', f=None):
    '''
    f should be a file
    '''
    if f != None:
        f.write(text + end)
    print(text, end=end)
    
        
def printGrid(grid, name="", f=None):
    '''
    f is a file instance
    '''
    index = 1
    myprint("----------------------------------------",'\n',f)
    if name != "":
        myprint(name + '\n','\n',f)
    for row in grid:
        myprint("%02d - " % (index,),' ', f)
        for elem in row:
            myprint(str(elem),' ',f)
        myprint('','\n',f)
        index += 1


def displayColoredGrid(grid, name):
    size = len(grid)
    # size of cell
    w, h = 20,20
    # black offset around the cells 2x20
    gridw, gridh = (w * size) + 40, (h * size) +40
    img = Image.new("RGB",(gridw,gridh))
    # create rectangle image 
    img1 = ImageDraw.Draw(img)
    # x => within line so j, y => line so i
    #origin is at the bottom
    originx, originy = 20, 20
    x, y = 0, 0
    for i in range(size):
        for j in range(size):
            # calculate the position of the cell in i-th line and j-th column
            x = originx + (j * 20)
            y = originy + (i * 20)
            shape = [(x, y), (x+20, y+20)]
            color = None
            if grid[i][j] == 0:
                color = (0,0,0)
            else:
                color = getColor(grid[i][j])
            img1.rectangle(shape, fill =color, outline ="black") 
    #img.show()
    img.save(name)
    
    
        
def firstLineNextChar(west):
     next = (getValue(west) + f(west)) % 23
     return CHARS[next -1]

def test_firstLineNextChar():
    print("First line char after W=N: " + firstLineNextChar("N"))


def standardLineNextChar(west, north):
    next = (getValue(north) + f(west)) % 23
    return CHARS[next -1]

def fillFirstLine(grid):
    west = grid[0][0]
    for i in range(1,36):
        west = firstLineNextChar(west)
        grid[0][i] = west

def fillStandardLine(grid, linenb):
    '''
    linenb should be between 1 and 35
    '''
    #determine starting index
    line = grid[linenb]
    index = 0
    for i in range(36):
        if line[i] == 0:
            index = i
            break
        else:
            i += 1
    #west and north should be defined
    for k in range(index,36):
        west = grid[linenb][k-1]
        north = grid[linenb-1][k]
        grid[linenb][k] = standardLineNextChar(west,north)


def createCompleteGrid(keyword):
    grid = createGrid(36)
    fillFirstColumn(grid, keyword)
    fillFirstLine(grid)
    for i in range(1,36):
        fillStandardLine(grid,i)
    return grid


def compareGrids(g1, g2):
    nblines = len(g1)
    if len(g2) != nblines:
        print("Grids do not have the same number of lines")
        return False
    #else:
        #print("Grids have " + str(nblines) + " lines")
    nbcols = len(g1[0])
    if len(g2[0]) != nbcols:
        print("Grids do not have the same number of columns")
        return False
    #else:
        #print("Grids have " + str(nbcols) + " columns")
    newgrid = createGrid(nblines)
    line = ""
    for i in range(nblines):
        for j in range(nbcols):
            if g1[i][j] == g2[i][j]:
                line += g1[i][j] + " "
                newgrid[i][j] = g1[i][j]
            else:
                line += "- "
        print(line)
        line=""
    return newgrid


def compareByNumbers(tables, nb1, nb2):
    print("++++++++++++++++++++++++++++++++++++++")
    print("Comparison between table "
          + str(KEYWORDS[nb1-1][0]) + ", " + KEYWORDS[nb1-1][1]
          + " and table "
          + str(KEYWORDS[nb2-1][0]) + ", " + KEYWORDS[nb2-1][1]
          + ":")
    return compareGrids(tables[nb1-1], tables[nb2-1])   
    
        
def main():
    f = open(OUTPUTFILE, "w")
    tables = []
    for elem in KEYWORDS:
        g = createCompleteGrid(elem[2])
        printGrid(g,"Grid number " + str(elem[0]) + ": " + elem[1],f)
        displayColoredGrid(g, "%02d - " % (elem[0],) + elem[1] + ".png")
        tables.append(g)
    f.close()
    comp1 = compareByNumbers(tables,1,13)
    displayColoredGrid(comp1, "Comparison Aries 1 Aries 13.png")
    comp2 = compareByNumbers(tables,2,14)
    displayColoredGrid(comp2, "Comparison Taurus 2 Taurus 14.png")
    calculateValue("Pater Creator")
    calculateValue("Aries")


    
#======================================== MAIN
if __name__ == "__main__":
    main()

    
    
    
