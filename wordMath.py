test = 'ONETWOPLUSONEMINUSNEGATIVETWO'
exp = ''
result = ''
print('The Text : ' + test)
for c in test:
    exp = exp + c.lower()
    #check for numbers and other expressions
    if exp == 'negative':
        result = result + '-'
        exp = ""
    elif exp == 'minus':
        result = result + ' - '
        exp = ""
    elif exp == "plus":
        result = result + ' + '
        exp = ""
    elif exp == 'zero':
        result = result + '0'
        exp = ""
    elif exp == 'one':
        result = result + '1'
        exp = ""
    elif exp == 'two':
        result = result + '2'
        exp = ""
    elif exp == 'three':
        result = result + '3'
        exp = ""
    elif exp == 'four':
        result = result + '4'
        exp = ""
    elif exp == 'five':
        result = result + '5'
        exp = ""
    elif exp == 'six':
        result = result + '6'
        exp = ""
    elif exp == 'seven':
        result = result + '7'
        exp = ""
    elif exp == 'eight':
        result = result + '8'
        exp = ""
    elif exp == 'nine':
        result = result + '9'
        exp = ""
exp = result.split()
print('Parsed text to numbers : ' + result)
result = int(exp[0])
add = False
sub = False
for x in exp[1:]:
    #actual math
    if add == True:
        result = result + int(x)
        add = False
    elif sub == True:
        result = result - int(x)
        sub = False
    #Flags
    if x == '+':
        add = True
    elif x == '-':
        sub = True
exp = str(result)
print('The result of doing math : ' + exp)
result = ''
for x in exp:
    #check for numbers
    if x == '-':
        result = result + 'NEGATIVE'
    elif x == '0':
        result = result + 'ZERO'
    elif x == '1':
        result = result + 'ONE'
    elif x == '2':
        result = result + 'TWO'
    elif x == '3':
        result = result + 'THREE'
    elif x == '4':
        result = result + 'FOUR'
    elif x == '5':
        result = result + 'FIVE'
    elif x == '6':
        result = result + 'SIX'
    elif x == '7':
        result = result + 'SEVEN'
    elif x == '8':
        result = result + 'EIGHT'
    elif x == '9':
        result = result + 'NINE'
print('Reworded : ' + result)

