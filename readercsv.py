import csv

# with open('sample.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Player","Type","Batting Order"])
#     writer.writerow(["Sachin","Batsman","TopOrder"])
#     writer.writerow(["Virat","Batsman","Top Order"])
#     writer.writerow(["Dhoni","Batsman","Lower Middle Order"])
#     writer.writerow(["Bumrah","Bowler","Last Order"])
#     writer.writerow(["Hardik","All rounder","Middle Order"])
# file.close()
with open('sample.csv',mode='r') as file:
    csvfile = csv.reader(file)

    for lines in csvfile:
        print(lines)
    