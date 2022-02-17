def arithmetic_arranger(problems, check = False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  top = ''
  bottom = ''
  dashes = ''
  result = ''
  output = ''

  for i in problems:
    pie = i.split()
    if pie[0].isnumeric() == False:
      return 'Error: Numbers must only contain digits.'
    if pie[2].isnumeric() == False:
      return 'Error: Numbers must only contain digits.'

    info1 = int(pie[0])
    info2 = int(pie[2])
    operator = pie[1]

    if operator == '+':
      num = info1 + info2
    elif operator == '-':
      num = info1 - info2
    else:
      return "Error: Operator must be '+' or '-'."

    if len(pie[0]) > 4 or len(pie[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if len(pie[0]) >= len(pie[2]):
      width = len(pie[0]) + 2
    else:
      width = len(pie[2]) + 2

    line1 = str(info1).rjust(width)
    line2 = operator + str(info2).rjust(width - 1)
    line3 = '-'.rjust(width, '-') # '-' * width
    line4 = str(num).rjust(width)

    if i != problems[-1]:
      top = top + line1 + '    '
      bottom = bottom + line2 + '    '
      dashes = dashes + line3 + '    '
      result = result + line4 + '    '
    else:
      top = top + line1
      bottom = bottom + line2
      dashes = dashes + line3
      result = result + line4

  if check:
    output = top + '\n' + bottom + '\n' + dashes + '\n' + result
  else:
    output = top + '\n' + bottom + '\n' + dashes
  return output
