from resources.lib import redux

def read_rows():
    rowsText = []
    with open('solutions/resources/p067_triangle.txt', 'r') as file:
        rowsText = file.readlines()
    rows = []
    for row in rowsText:
        rows.append([int(x) for x in row.split(' ')])
    return rows


rows = read_rows()

while len(rows) > 1:
    second_last = len(rows) - 2
    last = len(rows) - 1

    rows[second_last] = redux(rows[second_last], rows[last])
    rows.pop()

print(rows[0])