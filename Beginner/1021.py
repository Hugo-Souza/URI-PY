valor = float(input())

N100 = valor//100
valor = valor - (N100*100)

N50 = valor//50
valor = valor - (N50*50) 

N20 = valor//20
valor = valor - (N20*20)

N10 = valor//10
valor = valor - (N10*10)

N5 = valor//5
valor = valor - (N5*5)

N2 = valor//2
valor = valor - (N2*2)

M1 = valor//1
valor = valor - (M1*1)

M50 = valor//0.50
valor = valor - (M50*0.50)

M25 = valor//0.25
valor = valor - (M25*0.25)

M10 = valor//0.10
valor = valor - (M10*0.10)

M5 = valor//0.05
valor = valor - (M5*0.05)

M01 = valor


print("NOTAS:")
print("{%d} nota(s) de R$ 100,00".format(N100))
print("{%d} nota(s) de R$ 50,00".format(N50))
print("{%d} nota(s) de R$ 20,00".format(N20))
print("{%d} nota(s) de R$ 10,00".format(N10))
print("{%d} nota(s) de R$ 5,00".format(N5))
print("{%d} nota(s) de R$ 2,00".format(N2))
print("MOEDAS:")
print("{%d} moeda(s) de R$ 1,00".format(M1))
print("{%d} moeda(s) de R$ 0,50".format(M50))
print("{%d} moeda(s) de R$ 0,25".format(M25))
print("{%d} moeda(s) de R$ 0,10".format(M10))
print("{%d} moeda(s) de R$ 0,05".format(M5))
print("{%d} moeda(s) de R$ 0,01".format(M01))
