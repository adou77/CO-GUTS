def headcount(arr):
    def find_seats(arr,index):
        x = index[0]
        y = index[1]
        same_table = [(x,y)]

        if len(arr) > x+1 and arr[x+1][y] == 1:
            same_table.extend(find_seats(arr,(x+1,y)))

        if len(arr[x])> y+1 and arr[x][y+1] == 1:
            same_table.extend(find_seats(arr,(x,y+1)))

        return set(same_table)
    
    seats = []
    groups = []
    group_num =[]
    num = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                seats.append((i,j))
                
    for i in seats:
        groups.append(find_seats(arr,i))
        
    for i in range(len(groups)):
        placeholder_set = set()
        for j in range(len(groups)):
            if groups[j].intersection(groups[i]):
                placeholder_set = placeholder_set.union(groups[j])
        if placeholder_set not in group_num:
            group_num.append(placeholder_set)
    for i in group_num:
        num.append(len(i))
        
    x = "{n} teams of {l} totaling {s}".format(n = len(num), l = num, s = sum(num))
    return x
