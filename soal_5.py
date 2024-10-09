# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
# note: reversed(<string>) => menghasilkan list
#       __[::-1] => membalikkan string
#       range(start, stop-1, step)

# def solution(string):
#     reversed_string = ""
#     for char in string:
#         reversed_string = char + reversed_string  # Menambahkan karakter ke depan hasil
#     return reversed_string

# def solution(string):
#     reversed_string = ""
#     for i in range(len(string) - 1, -1, -1):
#         reversed_string += string[i]
#     return reversed_string

# def solution(string):
#     return "".join(reversed(string))

def solution(string):
    return string[::-1]


print(f"{solution("arya")}")