data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

simple_data_structure = [1, 2, 3, 4, 5, 'Hello', [1,2,3,4,5], {'a': 4, 'b': 5}]


def calculate_structure_sum(data_structure):
  sum = 0
  for item in data_structure:
    if isinstance(item, list) or isinstance(item, tuple):
      sum = sum + calculate_structure_sum(item)

    elif isinstance(item, dict):
      sum = sum + calculate_structure_sum(item.items())

    elif isinstance(item, set):
      sum = sum + calculate_structure_sum(list(item))

    else:
      if isinstance(item, str):
        sum = sum + len(item)

      else:
        sum = sum + item
  return sum


result = calculate_structure_sum(data_structure)
print(result)