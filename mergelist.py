lst1 = [2, 3, 7, 8, 9, 65, 90]
lst2 = [1, 76, 5, 4, 33, 55]

lstresult = []
i = j = 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] > lst2[j]:
        lstresult.append(lst2[j])
        j += 1
    else:
        lstresult.append(lst1[i])
        i += 1

while j < len(lst2):
    lstresult.append(lst2[j])
    j += 1

while i < len(lst1):
    lstresult.append(lst1[i])
    i += 1

print("mergelist", lstresult)



         
