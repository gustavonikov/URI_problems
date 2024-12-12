def find_gcd(a, b):
  while b:
    a, b = b, a % b
  return a

n, q = map(int, input().split())
vector = list(map(int, input().split()))

for test_case in range(q):
  query = map(int, input().split())
  query_type, a, b = query[0], query[1], query[2]
  a, b = a - 1, b - 1
  vector_indexes = len(vector) - 1

  if a > vector_indexes and b > vector_indexes:
    next
  elif a <= vector_indexes and b > vector_indexes:
    b = vector_indexes

  if query_type == 1:
    v = query[3]

  elif query_type == 2:
    if vector_indexes == 1:
      print(vector_indexes[0])
    else:
      initial_gcd_numbers = vector[a:final]
      n1, n2 = initial_gcd_numbers
      print(find_gcd(n1, n2))
    