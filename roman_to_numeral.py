                               #Given a roman numeral, convert it to an integer.

d = {'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000
     }

def roman_sum(roman_inp):

    Inp_roman = roman_inp
    counter = 0

    if d[Inp_roman[0]] > d[Inp_roman[1]]:
        for r in Inp_roman:
            roman_value = d.get(r)
            counter += roman_value

        return counter

def roman_sum_v2(roman_inp):

    counter = 0
    for i, r in enumerate(roman_inp):
        if(i+1 >= len(roman_inp)):
            roman_value = d.get(r)
            counter += roman_value
            break

        if (d[roman_inp[i]] < d[roman_inp[i+1]]) and ((i + 1) < len(roman_inp)):
            roman_value = d.get(r)
            counter -= roman_value
        else:
            roman_value = d.get(r)
            counter += roman_value

    return counter




inp = "LVIII"
print(inp, " ", roman_sum(inp))

inp = "CXXIX"
print(inp, " ", roman_sum_v2(inp))

