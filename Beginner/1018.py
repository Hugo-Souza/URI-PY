valor = int(input())
print("{}".format(valor))

N100 = valor//100
valor = valor - N100*100

N50 = valor//50
valor = valor - N50*50

N20 = valor//20
valor = valor - N20*20

N10 = valor//10
valor = valor - N10*10

N5 = valor//5
valor = valor - N5*5

N2 = valor//2
valor = valor - N2*2

N1 = valor//1
valor = valor - N1*1

print("{} nota(s) de R$ 100,00".format(N100))
print("{} nota(s) de R$ 50,00".format(N50))
print("{} nota(s) de R$ 20,00".format(N20))
print("{} nota(s) de R$ 10,00".format(N10))
print("{} nota(s) de R$ 5,00".format(N5))
print("{} nota(s) de R$ 2,00".format(N2))
print("{} nota(s) de R$ 1,00".format(N1))