# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
# note: [<i> for <i> in <array> if <kondisi>]

def positive_sum(arr):
    return sum([i for i in arr if i>0])

print(f"{positive_sum([-2, -3, 1, 4, 5])}")