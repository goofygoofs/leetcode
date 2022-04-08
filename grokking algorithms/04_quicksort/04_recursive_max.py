def max(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max