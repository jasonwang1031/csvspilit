import csv


def csvspilit(csvfile):
    with open(csvfile, encoding='UTF-8') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        i = 0
        d = 1
        while d <40:
            limit = i + 195
            with open('list%d.csv'%(d),'w',newline="") as new:
                writer = csv.writer(new)
                while i < limit:
                    if i >= len(rows):
                        break
                    else:
                        writer.writerow(rows[i])
                        i+=1
            new.close
            d+=1
    f.close

csvfile = "email_list.csv"
csvspilit(csvfile)


