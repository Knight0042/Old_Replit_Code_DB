import sys

test_input = '2Fe2O3 + H2SO4 -> Fe2(SO4)3 + H2O'

def is_num(char): # determines if a string is a number 0-9
  numbers = [str(i) for i in range(10)]  # how
  if char in numbers:
    return True
  return False

def capital(string):
  if string.upper() == string:
    return True
  return False

def count_single(element, parentheses):
  subscript = 1
  element_string = element
  if parentheses:
    if not is_num(element[-1]):
      print('No subscript found after parentheses in "{}", is this a mistake?'.format(element))
    for i in range(len(element) - 1, -1, -1):  # decrement through element (to get subscript)
      letter = element[i]
      if not is_num(letter):
        subscript = int(element[i + 1:])
        element_string = element[:i + 1]
        break
  else:
    for i, letter in enumerate(element):
      if is_num(letter):
        subscript = int(element[i:])
        element_string = element[:i]
        break
  return [element_string, subscript]
  
def add_or_update(obj, res):
  if res[0] in obj:
    obj[res[0]] += res[1]
  else:
    obj[res[0]] = res[1]

def parse_parentheses(string):
  # Return segments like in parse, multiply by subscript
  parsed = count_single(string, True)
  elements = parsed[0][1:-1]  # strip parentheses at front and back
  coefficient = parsed[1]
  if len(elements) == 0:
    sys.exit('Failure! Nothing inside of parentheses in "{}"'.format(string))
  segments = parse(elements)

  result = []  # contains elements with subscripts multiplied by the coefficient
  for segment in segments:
    element_info = count_single(segment, False)
    element_string = element_info[0] + str(coefficient  * element_info[1])
    result.append(element_string)

  return result

def parse(string):
  ##########
  #  Rules: 
  #  * Capital letters start a new element
  #  * Make parentheses their own segment with the subscript
  #  Steps: 
  #  1. Add new character to buffer
  #  2. See if we can continue
  #  3. If we can, keep going; if not, add content to list
  #  4. Always continue if we have open parentheses
  ##########

  segments = []
  buffer = ''
  parentheses_open = 0
  has_parentheses = False
  for i, letter in enumerate(string):
    #print('letter: ' + letter + '; index: ' + str(i))
    buffer += letter

    if letter == '(':
      parentheses_open += 1
      has_parentheses = True
    if letter == ')':
      if parentheses_open == 0:
        sys.exit('Failure! No opening found for closing ")" in term "{}"'.format(string))
      parentheses_open -= 1

    p_open = parentheses_open != 0

    # We're not counting parts with parentheses yet
    if i == len(string) - 1:  # End of string
      if p_open:
        sys.exit('Failure! Unclosed parentheses in term "{}"'.format(string))
      if not has_parentheses:
        segments.append(buffer)
      else:
        segments.extend(parse_parentheses(buffer))
    elif is_num(letter) and not capital(string[i + 1]):
      sys.exit('Failure! In term "{}", there is a lowercase letter after a subscript.'.format(string))
    elif not is_num(string[i + 1]) and capital(string[i + 1]) and not p_open:  # New element
      if not has_parentheses:
        segments.append(buffer)
      else:
        segments.extend(parse_parentheses(buffer))
      buffer = ''

  return segments

def count_elements(side_string):
  parts_string = side_string.split('+')  # Pretty sure we only split for a plus
  res = {}

  # Find coefficient
  for part in parts_string:
    coefficient_length = 0  # length of coefficient in characters
    for i in range(len(part)):
      char = part[coefficient_length]  # works as an index too
      if is_num(char):
        coefficient_length += 1
      else:
        break
    
    coefficient = 1
    if coefficient_length > 0:
      coefficient = int(part[:coefficient_length])
    
    part_remaining = part[coefficient_length:]
    if len(part_remaining) == 0:  # if they only put a coefficient
      sys.exit('Failure! Term "{}" has no elements'.format(part))

    #print('Coefficient of {}: {}'.format(part_remaining, str(coefficient)))

    # Count elements
    parsed = parse(part_remaining)  # split into segments
    #print(parsed)
    for segment in parsed:
      final = count_single(segment, False)  # get elements in segment
      final[1] *= coefficient  # multiply element subscript by coefficient
      add_or_update(res, final)  # add to total

  return res

# Get equation & strip whitespace
# equation_string = test_input  # test
# print('Running with test equation ' + equation_string)
equation_string = input('Enter equation (Ex: A + B -> AB): ').strip()
while equation_string.find(' ') != -1:  # remove spaces inside equation
  index = equation_string.find(' ')
  equation_string = equation_string[:index] + equation_string[index + 1:]

eq_split = equation_string.split('->')  # split into reactant & product
if len(eq_split) == 2:  # if both the reactant and product exist
  reactant_string = eq_split[0]
  product_string = eq_split[1]
  print('Reactants: ' + reactant_string)
  print('Products: ' + product_string + '\n')
  print('Parts of left side: ' + str(count_elements(reactant_string)))
  print('Parts of right side: ' + str(count_elements(product_string)))
else:
  print('Failure! Reactant and product could not be determined.')