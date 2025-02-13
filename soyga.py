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

COLORS2 = [
    (255, 0, 0),
    (255, 11, 0),
    (255, 22, 0),
    (255, 33, 0),
    (255, 44, 0),
    (255, 55, 0),
    (255, 67, 0),
    (255, 78, 0),
    (255, 89, 0),
    (255, 100, 0),
    (255, 111, 0),
    (255, 122, 0),
    (255, 133, 0),
    (255, 144, 0),
    (255, 155, 0),
    (255, 166, 0),
    (255, 177, 0),
    (255, 188, 0),
    (255, 200, 0),
    (255, 211, 0),
    (255, 222, 0),
    (255, 233, 0),
    (255, 244, 0)
]

COLORS3 = [
    (255, 255, 255),
    (243, 243, 243),
    (231, 231, 231),
    (220, 220, 220),
    (208, 208, 208),
    (197, 197, 197),
    (185, 185, 185),
    (173, 173, 173),
    (162, 162, 162),
    (150, 150, 150),
    (139, 139, 139),
    (127, 127, 127),
    (115, 115, 115),
    (104, 104, 104),
    (92, 92, 92),
    (81, 81, 81),
    (69, 69, 69),
    (57, 57, 57),
    (46, 46, 46),
    (34, 34, 34),
    (23, 23, 23),
    (11, 11, 11),
    (0, 0, 0)
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


def getColor(letter, colorset):
    theletter = letter.lower()
    return colorset[CHARS.index(theletter)]

    
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


def displayColoredGrid(grid, name, colorset=COLORS):
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
                color = getColor(grid[i][j], colorset)
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


def compareGrids(g1, g2, verbose=True):
    if verbose:
        print("=" * 80)
    newgrid = createGrid(36)
    line = ""
    for i in range(36):
        for j in range(36):
            if g1[i][j] == g2[i][j]:
                newgrid[i][j] = g1[i][j]
                line += str(g1[i][j]) + " "
            else:
                line += "- "
        if verbose:
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


def buildKey(i, j):
    '''
    This function builds a unique index to avoid duplicates
    Warning: i and j aare indexes and start at 0 but we convert them
    into references to KEYWORDS (starting at 1)
    '''
    if i>j:
        return str(j+1) + "-" + str(i+1)
    elif i<j:
        return str(i+1) + "-" + str(j+1)


def analyzeGrid(g,void='-'):
    d = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'x':0,
        'y':0,
        'z':0
    }
    count = 0
    for i in range(36):
        for j in range(36):
            if g[i][j] in d:
                d[g[i][j]] += 1
                count +=1
    return [count, d]


def extractStringFromGrid(g):
    thestring = ""
    for i in range(36):
        for j in range(36):
            if g[i][j] != "-" and g[i][j] != 0:
                thestring += g[i][j]
    return thestring

#========================================================Functions to read in spiral
def readLine(grid, line, colstart, colend):
    s = ""
    if colend > colstart:
        for i in range(colstart, colend+1):
            if grid[line][i] != 0 and grid[line][i] != '-':
                s += grid[line][i]
    elif colend < colstart:
        for i in range(colstart, colend-1, -1):
            if grid[line][i] != 0 and grid[line][i] != '-':
                s += grid[line][i]
    else:
        if grid[line][colstart] != 0 and grid[line][colstart] != '-':
            s += grid[line][colstart]
                
    return s


def readCol(grid, col, linestart, lineend):
    s = ""
    if lineend > linestart:
        for i in range(linestart, lineend+1):
            if grid[i][col] != 0 and grid[i][col] != '-':
                s += grid[i][col]
    elif lineend < linestart:
        for i in range(linestart, lineend-1, -1):
            if grid[i][col] != 0 and grid[i][col] != '-':
                s += grid[i][col]
    else:
        if grid[linestart][col] != 0 and grid[linestart][col] != '-':
                s += grid[linestart][col]
    return s


def extractStringFromGridSpiral(g):
    '''
    grids start at 0 to 35 (not 1 to 36)
    '''
    s = ""
    s += readCol(g,0,0,35) + readLine(g,35,1,35) + readCol(g,35,34,0) + readLine(g,0,34,1)
    s += readCol(g,1,1,34) + readLine(g,34,2,34) + readCol(g,34,33,1) + readLine(g,1,33,2)
    s += readCol(g,2,2,33) + readLine(g,33,3,33) + readCol(g,33,32,2) + readLine(g,2,32,3)
    s += readCol(g,3,3,32) + readLine(g,32,4,32) + readCol(g,32,31,3) + readLine(g,3,31,4)
    s += readCol(g,4,4,31) + readLine(g,31,5,31) + readCol(g,31,30,4) + readLine(g,4,30,5)
    s += readCol(g,5,5,30) + readLine(g,30,6,30) + readCol(g,30,29,5) + readLine(g,5,29,6)
    s += readCol(g,6,6,29) + readLine(g,29,7,29) + readCol(g,29,28,6) + readLine(g,6,28,7)
    s += readCol(g,7,7,28) + readLine(g,28,8,28) + readCol(g,28,27,7) + readLine(g,7,27,8)
    s += readCol(g,8,8,27) + readLine(g,27,9,27) + readCol(g,27,26,8) + readLine(g,8,26,9)
    s += readCol(g,9,9,26) + readLine(g,26,10,26) + readCol(g,26,25,9) + readLine(g,9,25,10)
    s += readCol(g,10,10,25) + readLine(g,25,11,25) + readCol(g,25,24,10) + readLine(g,10,24,11)
    s += readCol(g,11,11,24) + readLine(g,24,12,24) + readCol(g,24,23,11) + readLine(g,11,23,12)
    s += readCol(g,12,12,23) + readLine(g,23,13,23) + readCol(g,23,22,12) + readLine(g,12,22,13)
    s += readCol(g,13,13,22) + readLine(g,22,14,22) + readCol(g,22,21,13) + readLine(g,13,21,14)
    s += readCol(g,14,14,21) + readLine(g,21,15,21) + readCol(g,21,20,14) + readLine(g,14,20,15)
    s += readCol(g,15,15,20) + readLine(g,20,16,20) + readCol(g,20,19,15) + readLine(g,15,19,16)
    s += readCol(g,16,16,19) + readLine(g,19,17,19) + readCol(g,19,18,16) + readLine(g,16,18,17)
    s += readCol(g,17,17,18) + readLine(g,18,18,18) + readCol(g,18,17,17)
    return s

            
def spiral_traversal(grid):
    n = len(grid)
    s = ""

    # Initialiser les limites de la spirale
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        # Parcourir de haut en bas dans la première colonne
        for i in range(top, bottom + 1):
            if grid[i][left] != 0 and grid[i][left] != '-':
                s += grid[i][left]
        left += 1

        # Parcourir de droite à gauche dans la dernière ligne
        for j in range(right, left - 1, -1):
            if grid[bottom][j] != 0 and grid[bottom][j] != '-':
                s += grid[bottom][j]
        bottom -= 1

        # Parcourir de bas en haut dans la dernière colonne
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if grid[i][right] != 0 and grid[i][right] != '-':
                    s += grid[i][right]
            right -= 1

        # Parcourir de gauche à droite dans la première ligne
        if top <= bottom:
            for j in range(left, right + 1):
                if grid[top][j] != 0 and grid[top][j] != '-':
                    s += grid[top][j]
            top += 1
    return s


def compareAllDeltas(tables):
    i, j = 0, 0
    g = None
    comparisons = {} # key = lowest index + '-' + highest index, value = delta grid
    # 1. Calculating all deltas
    for i in range(36):
        for j in range(i+1, 36):
            g = compareGrids(tables[i],tables[j])
            comparisons[buildKey(i,j)] = g
    print("Length of comparisons: " + str(len(comparisons)))
    # 2. Analyzing deltas
    nbofchars = {} # key = elem, value = nbofchars
    for elem in comparisons:
        [count, d] = analyzeGrid(comparisons[elem])
        nbofchars[elem] = count
    output = list(sorted(nbofchars.items(), key=lambda x: x[1], reverse=True))
    for pair in output:
        thestring = extractStringFromGrid(comparisons[pair[0]])
        print(pair[0] + ", length: " + str(len(thestring)) + ": " + thestring)
        print(extractStringFromGridSpiral(comparisons[pair[0]]))
        print(spiral_traversal(comparisons[pair[0]]))

    
        
def main():
    f = open(OUTPUTFILE, "w")
    tables = []
    # main loop
    for elem in KEYWORDS:
        # create all grids
        g = createCompleteGrid(elem[2])
        # print them in console and file
        printGrid(g,"Grid number " + str(elem[0]) + ": " + elem[1],f)
        # generate images
        displayColoredGrid(g,"Rainbow - " + "%02d - " % (elem[0],) + elem[1] + ".png")
        displayColoredGrid(g,"RedToYellow - " + "%02d - " % (elem[0],) + elem[1] + ".png",COLORS2)
        displayColoredGrid(g,"Greyscale - " + "%02d - " % (elem[0],) + elem[1] + ".png",COLORS3)
        tables.append(g)
    f.close()
    # comparisons
    comp1 = compareByNumbers(tables,1,13)
    displayColoredGrid(comp1, "Comparison between Aries 1 and Aries 13.png")
    comp2 = compareByNumbers(tables,2,14)
    displayColoredGrid(comp2, "Comparison between Taurus 2 and Taurus 14.png")
    comp3 = compareByNumbers(tables,28,35)
    displayColoredGrid(comp3, "Comparison between Solis 28 and Terrai 35.png")
    comp4 = compareByNumbers(tables,5,6)
    displayColoredGrid(comp4, "Comparison between Leo 5 and Virgo 6.png")
    # values of texts => problem
    calculateValue("Pater Creator")
    calculateValue("Aries")
    # compare all deltas
    compareAllDeltas(tables)
    # test with another key as generator
    test = createCompleteGrid("KTULHU")
    printGrid(test, "Grid generated with KTULHU")
    comptest = compareGrids(test, tables[35])
    print("String = " + extractStringFromGrid(comptest))
    print("Spiral string = \n" + extractStringFromGridSpiral(comptest))
    print(spiral_traversal(comptest))

    
#======================================== MAIN
if __name__ == "__main__":
    main()

    
    
    
