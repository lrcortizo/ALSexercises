def f(texto):
    d = {}
    line = texto.split("\n")
    line1 = line[0].split(", ")
    for x in range(1, len(line1), 2):
        d[line1[x]] = line1[x-1]
    for x in range(1, len(line)):
        print(line[x].replace(line[x][0], d[line[x][0]], 1))
texto = "Microsoft, 1, Apple, 2, Google, 3, Yahoo, 4\n1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5\n2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234\n3, 2015-01-09, 934, 922, 866, 444, 235, 999, 789\n4, 2015-01-09, 45, 56, 78, 23, 44, 90, 9"
f(texto)

