
from operator import itemgetter
import os

def analyze_statutes(analyzed_cases_csv):
    with open(analyzed_cases_csv, "r") as dups:
        count = 0
        single_l2_equal = {}
        single_l2_not_equal = {}
        single_l3_equal = {}
        single_l3_not_equal = {}
        for case in dups:
            current_data = case.split("|")
            current_case = current_data[0].lower()
            if len(current_data[2]) > 1 or len(current_data[3])>1:
                count+=1
                #grab case number
                case_id = [" ".join(l.split(" ")[:4]).strip() for l in current_case.split(",")[1:] if ".3d" in l]
                cases = []
                new_case_id2 = ""
                if len(case_id) == 1:
                    new_case_id1 = case_id[0].replace(" ", "_").replace(".", "_").strip()
                    cases.append(new_case_id1)
                else:
                    new_case_id1 = case_id[0].replace(" ", "_").replace(".", "_").strip()
                    new_case_id2 = case_id[1].replace(" ", "_").replace(".", "_").strip()
                    cases.append(new_case_id1)
                    cases.append(new_case_id2)

                for ca in cases:
                    c = ca.split("(")[0]
                    #         #lookup l2 and l3
                    case_name_l2 = c +".txt-l2.txt"
                    case_name_l3 = c +".txt-l3.txt"
                    l2 = current_data[2]
                    l3 = current_data[3]
                    #
                    if len(l2.split(";")) > len(l2.split(",")):
                        l2_sections = l2.split(";")
                    else:
                        l2_sections = l2.split(",")

                    if len(l3.split(";")) > len(l3.split(",")):
                        l3_sections = l3.split(";")
                    else:
                        l3_sections = l3.split(",")


                    def removeNonAscii(s):
                        return "".join(filter(lambda x: ord(x) < 128, s))
                    l2_sections = [removeNonAscii(s.strip().replace(".","").replace("§","").replace("â","").replace("  ", " ").lower()) for s in l2_sections]
                    l3_sections = [removeNonAscii(s.strip().replace(".","").replace("§","").replace("â","").replace("  ", " ").lower())  for s in l3_sections]

                    #
                    #         ### STANDARDIZE Frequency Count and Answer ###
                    if os.path.isfile("statutes\\" + case_name_l2):
                        with open("statutes\\" + case_name_l2, "r", encoding="utf-8") as l2_txt:
                            lines = l2_txt.readlines()
                            l2dict = {}
                            for li in lines:
                                statute = "---".join(li.split("---")[:-1]).strip().replace(".","").replace("§","").replace("  ", " ")
                                value = int(li.split("---")[-1].strip())
                                l2dict[statute] = value
                        freq_list = sorted(l2dict.items(), key=itemgetter(1), reverse=True)

                        if len(l2_sections) == 1:
                            max = freq_list[0][1]
                            current_list = [ f for f in freq_list if f[1] == max]
                            unequal_temp = []
                            equal_temp = []
                            most_freq = False
                            for cur in current_list:
                                l2_pair = (l2_sections[0], cur[0])
                                if l2_sections[0] in cur[0] or cur[0] in l2_sections[0]:

                                    equal_temp.append(l2_pair)
                                    most_freq = True
                                else:
                                    unequal_temp.append(l2_pair)

                            if most_freq  :
                                if c in single_l2_equal:
                                    single_l2_equal[c].extend(equal_temp)
                                else:
                                    single_l2_equal[c] = [e for e in equal_temp]
                            else:
                                if c in single_l2_not_equal:
                                    single_l2_not_equal[c].extend(unequal_temp)
                                else:
                                    single_l2_not_equal[c] = [e for e in unequal_temp]
                    else:
                        case_name_l2 = c + "--1.txt-l2.txt"
                        with open("statutes\\" + case_name_l2, "r", encoding="utf-8") as l2_txt:
                            lines = l2_txt.readlines()
                            l2dict = {}
                            for li in lines:
                                statute = "---".join(li.split("---")[:-1]).strip().replace(".", "").replace("§",
                                                                                                            "").replace(
                                    "  ", " ")
                                value = int(li.split("---")[-1].strip())
                                l2dict[statute] = value
                        freq_list = sorted(l2dict.items(), key=itemgetter(1), reverse=True)

                        if len(l2_sections) == 1:
                            max = freq_list[0][1]
                            current_list = [f for f in freq_list if f[1] == max]
                            unequal_temp = []
                            equal_temp = []
                            most_freq = False
                            for cur in current_list:
                                l2_pair = (l2_sections[0], cur[0])
                                if l2_sections[0] in cur[0] or cur[0] in l2_sections[0]:

                                    equal_temp.append(l2_pair)
                                    most_freq = True
                                else:
                                    unequal_temp.append(l2_pair)

                            if most_freq:
                                if c in single_l2_equal:
                                    single_l2_equal[c].extend(equal_temp)
                                else:
                                    single_l2_equal[c] = [e for e in equal_temp]
                            else:
                                if c in single_l2_not_equal:
                                    single_l2_not_equal[c].extend(unequal_temp)
                                else:
                                    single_l2_not_equal[c] = [e for e in unequal_temp]

                    # else:
                    #     subsect = [f[0] for f in freq_list[:len(l2_sections)]]
                    #     for sect in l2_sections:
                    #         if sect in subsect:
                    #             if c in multi_l2_equal:
                    #                 multi_l2_equal[c].append((sect,))
                    #             else:
                    #                 multi_l2_equal[c] = [(sect,)]
                    #         else:
                    #             if c in multi_l2_not_equal:
                    #                 multi_l2_not_equal[c].append((sect,))
                    #             else:
                    #                 multi_l2_not_equal[c] = [(sect,)]
                    #
                    if os.path.isfile("statutes\\" + case_name_l3):
                        with open("statutes\\" + case_name_l3, "r", encoding="utf-8") as l3_txt:
                            lines = l3_txt.readlines()
                            l3dict = {}
                            for li in lines:
                                statute = "---".join(li.split("---")[:-1]).strip().replace(".", "").replace("§","").replace("  ", " ")
                                value = int(li.split("---")[-1].strip())
                                l3dict[statute] = value
                        freq_list = sorted(l3dict.items(), key=itemgetter(1), reverse=True)

                        if len(l3_sections) == 1:
                            max = freq_list[0][1]
                            current_list = [ f for f in freq_list if f[1] == max]
                            unequal_temp = []
                            equal_temp = []
                            most_freq = False
                            for cur in current_list:
                                l3_pair = (l3_sections[0], cur[0])
                                if l3_sections[0] in cur[0] or cur[0] in l3_sections[0]:

                                    equal_temp.append(l3_pair)
                                    most_freq = True
                                else:
                                    unequal_temp.append(l3_pair)

                            if most_freq  :
                                if c in single_l3_equal:
                                    single_l3_equal[c].extend(equal_temp)
                                else:
                                    single_l3_equal[c] = [e for e in equal_temp]
                            else:
                                if c in single_l3_not_equal:
                                    single_l3_not_equal[c].extend(unequal_temp)
                                else:
                                    single_l3_not_equal[c] = [e for e in unequal_temp]
                    else:
                        case_name_l3 = c + "--1.txt-l3.txt"
                        with open("statutes\\" + case_name_l3, "r", encoding="utf-8") as l3_txt:
                            lines = l3_txt.readlines()
                            l3dict = {}
                            for li in lines:
                                statute = "---".join(li.split("---")[:-1]).strip().replace(".", "").replace("§",
                                                                                                            "").replace(
                                    "  ", " ")
                                value = int(li.split("---")[-1].strip())
                                l3dict[statute] = value
                        freq_list = sorted(l3dict.items(), key=itemgetter(1), reverse=True)

                        if len(l3_sections) == 1:
                            max = freq_list[0][1]
                            current_list = [f for f in freq_list if f[1] == max]
                            unequal_temp = []
                            equal_temp = []
                            most_freq = False
                            for cur in current_list:
                                l3_pair = (l3_sections[0], cur[0])
                                if l3_sections[0] in cur[0] or cur[0] in l3_sections[0]:

                                    equal_temp.append(l3_pair)
                                    most_freq = True
                                else:
                                    unequal_temp.append(l3_pair)

                            if most_freq:
                                if c in single_l3_equal:
                                    single_l3_equal[c].extend(equal_temp)
                                else:
                                    single_l3_equal[c] = [e for e in equal_temp]
                            else:
                                if c in single_l3_not_equal:
                                    single_l3_not_equal[c].extend(unequal_temp)
                                else:
                                    single_l3_not_equal[c] = [e for e in unequal_temp]

                                # else:
                        #     subsect = [f[0] for f in freq_list[:len(l3_sections)]]
                        #     for sect in l3_sections:
                        #         if sect in subsect:
                        #             if c in multi_l3_equal:
                        #                 multi_l3_equal[c].append((sect,))
                        #             else:
                        #                 multi_l3_equal[c] = [(sect,)]
                        #         else:
                        #             if c in multi_l3_not_equal:
                        #                 multi_l3_not_equal[c].append((sect,))
                        #             else:
                        #                 multi_l3_not_equal[c] = [(sect,)]

    print(single_l2_equal)
    print(single_l2_not_equal)
    print(len(single_l2_equal)/(len(single_l2_equal) + len(single_l2_not_equal)))
