entrada = input().split(" ")

a, b, c = entrada

maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2

maiorBC = (int(b)+int(c)+abs(int(b)-int(c)))/2

maior = (maiorAB+maiorBC+abs(maiorAB-maiorBC))/2

print("%d eh o maior" %maior)