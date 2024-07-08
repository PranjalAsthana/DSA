n = int(input())
c = f'{n:04b}'
c = c[::-1]
print(int(f'{c}',2))
