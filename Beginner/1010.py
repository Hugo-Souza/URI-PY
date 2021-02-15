PROD1 = input().split(" ")
PROD2 = input().split(" ")

COD1, QTD1, VAL1 = PROD1
COD2, QTD2, VAL2 = PROD2

total = (int(QTD1) * float(VAL1)) + (int(QTD2) * float(VAL2))

print("VALOR A PAGAR: R$ %0.2f" %total)