# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
# note: <nilai_jika_true> if <kondisi> else <nilai_jika_false>

def even_or_odd(number):
    return f"Even" if (number % 2 == 0) else f"Odd"

print(f"{even_or_odd(2)}")