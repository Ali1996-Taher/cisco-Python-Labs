Birth_Date = input(
    "Enter yourbirthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY : ")

if len(Birth_Date) != 8 or not Birth_Date.isdigit():
    print("f")
else:
    while len(Birth_Date) > 1:
        sum = 0
        for digit in Birth_Date:
            sum += int(digit)
        Birth_Date = str(sum)
    print(Birth_Date)
