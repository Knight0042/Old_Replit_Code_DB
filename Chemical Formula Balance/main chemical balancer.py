reactants = []
reactants_value = []
products = []
reactants_dictionary = {}
products_dictionary = {}
element_list_total = []
input_react = True
parenthesis = False



element_total = int(input("How Many Elements are there? "))
num = 0
while num < element_total:
    element = input("Element Symbol (ex. O for Oxygen): ")
    element_list_total.append(element)
    num += 1

full_equation = input("Equation: ")
finding_reactants = True

reactant = ''
product = ''

for char in full_equation:
    if finding_reactants:
        if char == '+':
            reactants.append(reactant)
            reactant = ''
        elif char == '>':
            reactants.append(reactant)
            reactant = ''
            finding_reactants = False
        else:
            reactant += f'{char}' 
    else:
        if char == '+':
            products.append(product)
            product = ''
        else:
            product += f'{char}'
products.append(product)
product = ''
print(reactants)
print(products)


# reactants_total = int(input("How Many how many reactants are there? "))
# num = 0
# while num < reactants_total:
#     reactant = input("Reactant:")
#     reactants.append(reactant)
#     num += 1
for element in element_list_total:
    reactants_dictionary[element] = 0
for reactnt in reactants:
    num2 = -1
    for char in reactnt:
        num2 += 1
        for element in element_list_total:
            num = 0
            for c in element:
                num+=1
            
            if num > 1:
                if num2+1 < len(reactnt):
                    if element[0] == char and element[1] == reactnt[num2+1]:
                        element_amount = 1
                        counting = True
                        num_string = ''
                        num4 = 2
                        while counting:
                            if num2+num4 < len(reactnt):
                                if reactnt[num2+num4].isdigit():
                                    num_string += f'{reactnt[num2+num4]}'
                                else:
                                    counting = False
                            else:
                                counting = False
                            num4 += 1
                        if num_string == '':
                            num_string = '1'
                        element_amount = int(num_string)
                        if parenthesis:
                            num3 = -1
                            for char in reactnt:
                                num3 += 1
                                if char == ')':
                                    counting = True
                                    num_string = ''
                                    num4 = 1
                                    while counting:
                                        if num3+num4 < len(reactnt):
                                            if reactnt[num3+num4].isdigit():
                                                num_string += f'{reactnt[num3+num4]}'
                                            else:
                                                counting = False
                                        else:
                                            counting = False
                                        num4 += 1
                                    if num_string == '':
                                        num_string = '1'
                                    element_amount = (element_amount * int(num_string))
                        reactants_dictionary[element] = (reactants_dictionary[element] + element_amount)

            else:
                if element == char:
                    element_amount = 1
                    num_string = ''
                    num4 = 1
                    if num2+1 < len(reactnt):
                        if reactnt[num2+1].islower():
                            break
                        if reactnt[num2+1].isdigit():
                            counting = True
                            while counting:
                                if num2+num4 < len(reactnt):
                                    if reactnt[num2+num4].isdigit():
                                        num_string += f'{reactnt[num2+num4]}'
                                    else:
                                            counting = False
                                else:
                                    counting = False
                                num4 += 1
                    if num_string == '':
                        num_string = '1'
                    element_amount = int(num_string)

                    if parenthesis:
                        num3 = -1
                        for char in reactnt:
                            num3 += 1
                            if char == ')':
                                counting = True
                                num_string = ''
                                num4 = 1
                                while counting:
                                    if num3+num4 < len(reactnt):
                                        if reactnt[num3+num4].isdigit():
                                            num_string += f'{reactnt[num3+num4]}'
                                        else:
                                            counting = False
                                    else:
                                        counting = False
                                    num4 += 1
                                if num_string == '':
                                    num_string = '1'
                                element_amount = (element_amount * int(num_string))

                    reactants_dictionary[element] = (reactants_dictionary[element] + element_amount)
        if char == '(':
            parenthesis = True
        if char == ')':
            parenthesis = False

# products_total = int(input("How Many how many products are there? "))
# num = 0
# while num < products_total:
#     product = input("Product:")
#     products.append(product)
#     num += 1

for prdct in products:
    num2 = -1
    for char in prdct:
        num2 += 1
        for element in element_list_total:
            num = 0
            for c in element:
                num+=1

            if num > 1:
                if num2+1 < len(prdct):
                    if element[0] == char and element[1] == prdct[num2+1]:
                        element_amount = 1
                        counting = True
                        num_string = ''
                        num4 = 2
                        while counting:
                            if num2+num4 < len(prdct):
                                if prdct[num2+num4].isdigit():
                                    num_string += f'{prdct[num2+num4]}'
                                else:
                                    counting = False
                            else:
                                counting = False
                            num4 += 1
                        if num_string == '':
                            num_string = '1'

                        element_amount = int(num_string)

                        if element in products_dictionary:
                            products_dictionary[element] = (products_dictionary[element] + element_amount)
                        else:
                            products_dictionary[element] = element_amount

            else:
                element_amount = 1
                if num2+1 < len(prdct):
                    if element == char:
                        if prdct[num2+1].isupper() or prdct[num2+1].isdigit():
                            element_amount = 1
                            counting = True
                            num_string = ''
                            num4 = 1
                            while counting:
                                if num2+num4 < len(prdct):
                                    if prdct[num2+num4].isdigit():
                                        num_string += f'{prdct[num2+num4]}'
                                    else:
                                        counting = False
                                else:
                                    counting = False
                                num4 += 1
                            if num_string == '':
                                    num_string = '1'
                            element_amount = int(num_string)


                            if parenthesis:
                                num3 = -1
                                for char in prdct:
                                    num3 += 1
                                    if char == ')':
                                        counting = True
                                        num_string = ''
                                        num4 = 1
                                        while counting:
                                            if num3+num4 < len(prdct):
                                                if prdct[num3+num4].isdigit():
                                                    num_string += f'{prdct[num3+num4]}'
                                                else:
                                                    counting = False
                                                    
                                            else:
                                                counting = False
                                            num4 += 1
                                        if num_string == '':
                                            num_string = '1'
                                        element_amount = (element_amount * int(num_string))
                            if element in products_dictionary:
                                products_dictionary[element] = (products_dictionary[element] + element_amount)
                            else:
                                products_dictionary[element] = element_amount
                else:
                    if element == char:
                        if element in products_dictionary:
                            products_dictionary[element] = (products_dictionary[element] + element_amount)
                        else:
                            products_dictionary[element] = element_amount
        if char == '(':
            parenthesis = True
        if char == ')':
            parenthesis = False

print(reactants_dictionary)
print(products_dictionary)
