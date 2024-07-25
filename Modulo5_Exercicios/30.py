#Faça programas para calcular as seguintes sequências:
#(1 + 2 + 3 + … + n)
#(1 - 2 + 3 - 4 …)
#(1 + 3 + 5 + 7...)

n = int(input('Insira um número: '))

soma = 0
r = 0
final = 0

for i in range(1, n + 1):
    soma = soma + i

for i in range (1, 1 + n):
    if i % 2 == 1:
        r = r + i
    else:
        r = r - i

for i in range (1, 2*n, 2):
    final = final + i
print(f'A primeira é {soma}, a segunda é {r} e a terceira é {final}')

'''n = int(input('Digite um numero: '))
resultado = 0
 
for i in range(1, n + 1):
    if i % 2 == 0:
        print(resultado)
    else:
        resultado += i
        print(resultado)
 
print(f'A soma é {resultado}')'''