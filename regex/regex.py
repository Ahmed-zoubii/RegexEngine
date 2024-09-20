def backward(reg='', word='', result=None):
    if all(('\\' in reg, '$' not in reg, '.' not in reg, '?' not in reg, '+' not in reg)):
        result = all(([True if i in reg else False for i in word]))
    elif '$' in reg:
        reg = reg.replace('$', '').replace('\\', '')
        result = True if word.endswith(reg) else False
    elif '+' in reg:
        reg = reg.replace('\\', '')
        result = all(([True if i in word else False for i in reg]))
    elif '?' in reg:
        reg = reg.replace('\\', '')
        result = True if reg in word else False
    return  result
def Regexp(reg='', word='', result=None):
    if all(('.' in reg, '+' in reg, '^' not in reg, '$' not in reg)):
        result = True
    elif all(('+' in reg, '.' not in reg, '^' not in reg)):
        reg = reg.replace('+','')
        result = all((True if i in word else False for i in reg))
    elif  all(('*' in reg, '.' not in reg, '$' not in reg)):
        preceding_index = reg.find('*') - 1
        preceding_character = reg[preceding_index]
        reg = reg.replace(preceding_character,'' , reg.count(preceding_character)).replace('*', '')
        word = word.replace(preceding_character, '', word.count(preceding_character))
        result = all((True if i == j else False for i, j in zip(reg, word)))
    elif all(('.' in reg, '*' in reg, '$' not in reg)):
     result = True
    elif all(('.' in reg, '*' in reg, '$' in reg)):
        preceding_index = reg.find('*') + 1
        preceding_character = reg[preceding_index]
        result = True if word.endswith(preceding_character) else False
    elif '?' in reg:
        if '.' not in reg:
            meta_index = reg.find('?')
            reg = reg.replace('?', '')
            if len(reg)  == (len(word)):
                result = all((True if i == j else False for i, j in zip(reg, word)))
            elif (len(reg) -1) == len(word):
                reg = reg.replace(reg[meta_index -1] , '')
                result = all((True if i == j else False for i, j in zip(reg, word)))
            else:
                result = False
        else:
            result = True
    elif all(('^' in reg, '$' not in reg, '+' not in reg)):
        reg = reg.replace('^','')
        result = True if word.startswith(reg) else False
    elif all(('$' in reg, '^' not in reg)):
        if '.' in reg:
            result = True
        else:
            reg = reg.replace('$','')
            result = True if word.endswith(reg) else False
    elif '^' and '$' in reg :
        if '+' not in reg:
            reg = reg.replace('^','').replace('$','')
            result = True if reg == word else False
        elif '+' in reg and not '.' in reg:
            preceding_index = reg.find('+') - 1  # 3
            preceding_character = reg[preceding_index]  # O
            reg = reg.replace(preceding_character, '').replace('+','').replace('^','')
            word = word.replace(preceding_character, '', word.count(preceding_character))
            result = all(([True if i == j else False for i, j in zip(reg, word)]))
        elif '+' in reg and '.' in reg:
            after_index = reg.find('+') + 1
            after_charqacter = reg[after_index]
            after_index_in_word = word.find(after_charqacter) - 1
            after_charqacter_in_word = word[after_index_in_word]
            word = word.replace(word[after_index_in_word], '', word.count(after_charqacter_in_word))
            reg = reg.replace('.', '').replace('+','')
            reg = reg.replace('$', '').replace('^', '')
            result = True if word.endswith(reg) else False
    elif any((not reg and word, not reg and not word, reg == '.' and len(reg) == 1)):
        result = True
    elif '.' in reg and '+' not in reg:
        reg = reg.replace('.','')
        result = True if reg in word else False
    elif all(('^' in reg, '+' in reg)):
        reg = reg.replace('^', '').replace('+', '')
        result = True if word.startswith(reg) else False
    else:
        result = True if reg in word else True if reg == '.' else 'False'

    return  result


reg, word = input().split('|')
if '\\' in reg:
    print(backward(reg, word))
else:
    print(Regexp(reg, word))

