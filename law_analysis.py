import os
import matplotlib.pyplot as plt
from shutil import copyfile
import numpy as np
from collections import Counter
from operator import itemgetter


NEW_DIR = "meta_text"

SHORT_FILE = ""
LONG_FILE = ""

def flatten(file_type, target_dir):
    special_file = []
    for dir in os.listdir(target_dir):
        files = dir.split("-")
        file1 = files[0]
        file_list = []
        file_list.append(file1)
        if len(files) == 2:
            file2 = files[1]
            special_file.append(file2)
            file_list.append(file2)
        for f in file_list:
            current_dir = os.path.join(target_dir, dir)
            if f in special_file:
                copyfile(current_dir + "\\" + f + file_type, NEW_DIR + "\\" + f+"--1" + file_type)

            else:
                copyfile(current_dir + "\\" + f + file_type, NEW_DIR + "\\" + f + file_type)


stop_counting = False


def average_length():
    count = 0
    shortest_words = 0
    longest_words = 0
    average_words = 0
    hashmap = {}
    global SHORT_FILE
    global LONG_FILE
    global stop_counting
    highlighted = {}
    new_dir = "raw_text"
    for f in os.listdir(new_dir):
        current_dir = os.path.join(new_dir, f)
        count +=1
        highlight_val = False
        if "--" in f:
            highlight_val = True
        stop_counting = False
        with open(current_dir, "r", encoding="utf-8") as f1:
            lines = f1.readlines()
            current_count = 0
            for li in lines[9:-1]:
                l = li.strip().split()
                if len(l) > 1 and l[0][0] == "[" and l[0][1].isnumeric():
                    stop_counting = True
                if not stop_counting:
                    current_count += len(l)
            if shortest_words == 0 or current_count < shortest_words:
                shortest_words = current_count
                SHORT_FILE = f

            if longest_words == 0 or current_count > longest_words:
                longest_words = current_count
                LONG_FILE = f
            average_words += current_count
            if current_count in hashmap:
                current_count += 1
            else:
                hashmap[current_count] = 1

            if highlight_val:
                if current_count not in highlighted:
                    highlighted[current_count] = True
    print(shortest_words)
    print(longest_words)
    print(count)
    print(average_words/count)
    X = list(hashmap.keys())
    X.sort()
    print(X[int(len(X)/2)])
    # Y = []
    # for val in range(0, 58000):
    #     if val in highlighted:
    #         Y.append(1)
    #     else:
    #         Y.append(0)
    highlight = list(highlighted.keys())
    highlight.sort()
    print(highlight)
    # NEW_X = []
    # for val in range(0, 58000):
    #     NEW_X.append(val)
    #
    # plt.axis([0, 60000, 0, 5])
    #
    # plt.plot(NEW_X,Y)
    # print(X)
    # print(Y)
    #
    # plt.show()

def footnotes():
    ref_count = 0
    footnote_count =0
    other_count = 0

    largest_footnote = 0
    smallest_footnote = 0
    largest_ref =0
    smallest_ref =0
    largest_other =0
    smallest_other =0

    foot = []
    other = []
    ref = []

    new_dir = "meta_text"
    for f in os.listdir(new_dir):
        current_dir = os.path.join(new_dir, f)
        with open(current_dir, "r") as f1:
            lines = f1.readlines()
            curr_ref = []
            curr_foot = []
            curr_other = []
            for line in lines[1:-1]:

                li = line.strip()
                if len(li) >= 1 and not (li.isnumeric() or li[0] == "*"):
                    if li[0] == "[":
                        curr_foot.append(li)
                    else:
                        curr_other.append(li)
                    curr_ref.append(li)

            current_foot = len(set(curr_foot))
            current_ref = len(set(curr_ref))
            current_other = len(set(curr_other))

            ref.append(current_ref)
            other.append(current_other)
            foot.append(current_foot)

            if smallest_footnote == 0 or current_foot < smallest_footnote:
                smallest_footnote = current_foot


            if smallest_ref == 0 or current_ref < smallest_ref:
                smallest_ref = current_ref

            if smallest_other == 0 or current_other < smallest_other:
                smallest_other = current_other


            if largest_footnote == 0 or current_foot > largest_footnote:
                largest_footnote = current_foot
                test = f

            if largest_ref == 0 or current_ref > largest_ref:
                largest_ref = current_ref

            if largest_other == 0 or current_other > largest_other:
                largest_other = current_other

            ref_count+= current_ref
            other_count += current_other
            footnote_count += current_foot
    print(smallest_footnote)
    print(smallest_other)
    print(smallest_ref)
    print("#########")
    print(largest_footnote)
    print(largest_other)
    print(largest_ref)
    print("###############")
    print(footnote_count/1012)
    print(other_count/1012)
    print(ref_count/1012)
    print("###############")
    ref.sort()
    foot.sort()
    other.sort()
    print(foot)
    print(foot[int(len(foot)/2)])
    print(other[int(len(foot)/2)])
    print(ref[int(len(foot)/2)])
    print(test)

def find_statutes():
    l3_doc_statute_count = {}
    l2_doc_statute_count = {}

    for fi in os.listdir("raw_text"):
        level3_statute_list = {}
        level2_statute_list = {}
        with open("raw_text/"+fi, "r", encoding="utf-8") as f:
            for line in f:
                words = line.lower().split()
                for i in range(0, len(words)):
                    if "§" in words[i]:


                        if words[i-1].count(".") > 1:
                            if i >= 2:
                                statute = " ".join(words[i-2:i+2])
                            else:
                                statute = " ".join(words[0:i+2])
                        else:
                            statute = " ".join(words[i:i+2])

                        if not statute[-1].isalnum() and statute[-1] != ")":
                            statute = statute[:-1]
                        if statute[0] == "(" or statute[0] == "[":
                            statute = statute[1:]
                        if statute[-1] == ")" and statute[-2] == ")":
                            statute = statute[:-1]
                        if statute[-1] == "]":
                            statute = statute[:-1]
                        #partial shorthand
                        asterisk_split = statute.split(" ")
                        if "*" in asterisk_split[0]:
                            right_ast = asterisk_split[0].split("*")[1] + " "
                            statute = right_ast + " ".join(asterisk_split[1:])
                        if statute in level2_statute_list:
                            level2_statute_list[statute] += 1
                        else:
                            not_subset = True
                            for v in level2_statute_list:
                                vi = set(v.split())
                                sti = set(statute.split())
                                if sti < vi or vi < sti:
                                    level2_statute_list[v] += 1
                                    not_subset = False
                                    break
                            if not_subset:
                                level2_statute_list[statute] = 1
                        if "(" in statute:
                            statute = statute.split("(")[0]
                        if not statute[-1].isalnum():
                            statute = statute[:-1]
                        if statute in level3_statute_list:
                            level3_statute_list[statute] += 1
                        # partial shorthand
                        else:
                            not_subset = True
                            for v in level3_statute_list:
                                vi = set(v.split())
                                sti = set(statute.split())
                                if sti < vi or vi < sti:
                                    level3_statute_list[v] += 1
                                    not_subset = False
                                    break

                            if not_subset:
                                level3_statute_list[statute] = 1

            with open("statutes/" + fi+"-l3.txt", "w", encoding="utf-8") as f1, open("statutes/" + fi+"-l2.txt", "w", encoding="utf-8") as f2:
                for l1 in level3_statute_list:
                    f1.write(l1  + "---" + str(level3_statute_list[l1]) + "\n")

                for l2 in level2_statute_list:
                    f2.write(l2  + "---" + str(level2_statute_list[l2]) + "\n")
                l3_doc_statute_count[fi] = len(level3_statute_list)
                l2_doc_statute_count[fi] = len(level2_statute_list)
    mina = 0
    maxa = 0
    meana = 0
    mediana = 0

    for l in l3_doc_statute_count:

        if mina == 0 or l3_doc_statute_count[l] < mina:
            mina = l3_doc_statute_count[l]
        if maxa == 0 or l3_doc_statute_count[l] > maxa:
            maxa = l3_doc_statute_count[l]
        meana += l3_doc_statute_count[l]
    print(mina)
    import operator
    print(maxa)
    print(len(l3_doc_statute_count))
    print(l3_doc_statute_count)
    print(meana/len(l3_doc_statute_count))
    sorted_x = sorted(l3_doc_statute_count.items(), key=operator.itemgetter(1))
    mediana = sorted_x[int(len(l3_doc_statute_count)/2)]
    print(mediana)

    minb = 0
    maxb = 0
    meanb = 0
    medianb = 0

    for l in l2_doc_statute_count:

        if minb == 0 or l2_doc_statute_count[l] < minb:
            minb = l2_doc_statute_count[l]
        if maxb == 0 or l2_doc_statute_count[l] > maxb:
            maxb = l2_doc_statute_count[l]
        meanb += l2_doc_statute_count[l]
    print(minb)
    print(maxb)
    print(l2_doc_statute_count)
    print(meanb / len(l2_doc_statute_count))
    sorted_x = sorted(l2_doc_statute_count.items(), key=operator.itemgetter(1))
    medianb = sorted_x[int(len(l2_doc_statute_count) / 2)]
    print(medianb)

#sort by length, if subsection add together


if __name__ == "__main__":
    find_statutes()

