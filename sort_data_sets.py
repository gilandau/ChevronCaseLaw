# with open("final_total_list.txt", "r", encoding="utf-8") as f1, open("sorted_final_total_list.txt", "w", encoding="utf-8") as new_f1, \
#     open("test.csv", "r", encoding="utf-8") as f2, open("sorted_analyzed_cases.csv","w", encoding="utf-8") as new_f2:
#     testcsv = []
#     for t in f2:
#         testcsv.append(t.lower())
#
#     final_total = f1.readlines()
#     final_total.sort()
#     testcsv.sort()
#     for f in final_total:
#         new_f1.write(f.strip() + "\n")
#     for t in testcsv:
#         new_f2.write(t.strip() + "\n")

with open("sorted_analyzed_cases.csv", "r", encoding="utf-8") as ff:
    count = 0
    for f in ff:
        current_data = f.split("|")
        if len(current_data[2]) > 1 or len(current_data[3]) > 1:
            count+=1
print(count)
