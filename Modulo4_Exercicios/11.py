num = int(input('Digite um numero: '))
 
if num >= 0:
    soma = sum(int(num) for num in str(num))
    print(f"A soma dos algarismos é {soma}")
else:
    print("Número inválido. Digite um número inteiro maior do que zero.")
 
 