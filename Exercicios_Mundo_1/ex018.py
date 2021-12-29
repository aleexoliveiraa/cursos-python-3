import math
ângulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tang = math.tan(math.radians(ângulo))

print(f'O Seno do ângulo {ângulo} é {sen:.2f}')
print(f'O Coseno do ângulo {ângulo} é {cos:.2f}')
print(f'E a Tangente do ânuglo {ângulo} é {tang:.2f}')
