tagihan = float(input("masukkan tagihan : "))
if tagihan >= 100000:
    pajak = tagihan * 0.10
else:
    pajak = 0
total = tagihan + pajak
print("total bayar bersama : ",total)
totalMasing = total/3
print("total bayar masing-masing : ",totalMasing)
pajakMasing = totalMasing * 0.10
totalPajakMasing = totalMasing + pajakMasing
print("total akhirnya : ",totalPajakMasing)


