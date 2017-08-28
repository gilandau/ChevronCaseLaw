def parse_cases(csv_file):
    import operator
    with open(csv_file, "r") as f:
        level1 ={}
        level2 = {}
        level3 = {}
        level4 = {}
        level5 = {}
        levels = {1:level1, 2: level2, 3:level3, 4:level4, 5:level5}
        multilines = {}
        for line in f:
            worthgoingover = False
            sections = line.split("|")
            for i in range(1,len(sections)):
                if len(sections[i]) > 3:
                    worthgoingover = True
                    break
            if worthgoingover:
                for i in range(1,len(sections)):
                    count = 0
                    semi = sections[i].split(";")
                    comma = sections[i].split(",")
                    if len(semi[0]) == 0 and len(comma[0]) == 0:
                        num = 0
                    else:
                        if len(semi) >= len(comma):
                            num = len(semi)
                        else:
                            num = len(comma)

                    if sections[0] not in levels[i]:
                        levels[i][sections[0]] = num
                    else:
                        levels[i][sections[0]+str(count)] = num
                        count+=1
            if sections[0] not in multilines:
                multilines[sections[0]] = 1
            else:
                multilines[sections[0]] +=1

    mlmin = 0
    mlmax = 0
    mlmedian = 0
    mlmean = 0
    mlmulti = 0
    mlnum = len(multilines)

    for l in multilines:
        if mlmin == 0 or multilines[l] < mlmin:
            mlmin = multilines[l]
        if mlmax == 0 or multilines[l] >= mlmax:
            mlmax = multilines[l]
        mlmean += multilines[l]
        if multilines[l] > 1:
            mlmulti += 1
    sorted_ml = sorted(multilines.items(), key=operator.itemgetter(1))
    mlmedian = sorted_ml[int(mlnum / 2)]

    # print(mlmin)
    # print(mlmax)
    # print(mlmean/mlnum)
    # print(mlmedian)
    # print(mlmulti/mlnum)
    # print("##################")
    for lvl in levels:
        mlmin = -1
        mlmax = 0
        mlmedian = 0
        mlmean = 0
        mlmulti = 0
        mlnum = len(levels[lvl])
        print(lvl)
        loo = levels[lvl]

        for l in loo:
            if mlmin == -1 or loo[l] <= mlmin:
                mlmin = loo[l]
            if mlmax == 0 or loo[l] >= mlmax:
                mlmax = loo[l]
            mlmean += loo[l]
            if loo[l] > 1:
                mlmulti += 1
        sorted_ml = sorted(loo.items(), key=operator.itemgetter(1))
        mlmedian = sorted_ml[int(mlnum / 2)]

        print("LEVEL: " + str(lvl))
        print(mlmin)
        print(mlmax)
        print(mlmean / mlnum)
        print(mlmedian)
        print(mlmulti / mlnum)



    with open(csv_file, "r") as f:
        level2 = {}
        level3 = {}
        levels = { 2: level2, 3: level3}
        multilines = {}
        for line in f:
            worthgoingover = False
            sections = line.split("|")
            for i in range(1, len(sections)):
                if len(sections[i]) > 3:
                    worthgoingover = True
                    break
            if worthgoingover:
                for i in range(1, len(sections)):
                    count = 0
                    semi = sections[i].split(";")
                    comma = sections[i].split(",")
                    if len(semi[0]) == 0 and len(comma[0]) == 0:
                        num = 0
                    else:
                        if len(semi) >= len(comma):
                            num = len(semi)
                        else:
                            num = len(comma)

                    if sections[0] not in levels[i]:
                        levels[i][sections[0]] = num
                    else:
                        levels[i][sections[0] + str(count)] = num
                        count += 1