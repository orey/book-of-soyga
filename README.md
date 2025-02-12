# Book of Soyga

## Origin

See https://en.wikipedia.org/wiki/Book_of_Soyga

## Program

The Pyton program `soyga.py` is calculating all the 36 tables of 36x36 elements and put them on the console and into a file called `book-of-soyga-tables.txt`.

To run the program, type:

```
> python soyga.py
```

This program is implementing the algorithm described by Jim Reeds in 1998 (see the paper in the same folder). Jim Reeds succeeded in cracking the code of those tables.

## Keywords for table generation

Strangely, those tables are the fruit of a generator keyword of 6 letter, and so seem to be more a kind of amusement than a vehicule for knowledge.

```
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
```

## A translation by Jane Kuplin

The Book of Soyga was translated from latin by Jane Kuplin in 2014. Maybe some chapter could shed some light on the tables.


