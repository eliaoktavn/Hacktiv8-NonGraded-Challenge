str_input = input("angka:")
angka = int(str_input)
for i in range(1, angka+1):
    jumlah_spasi = angka - i
    jumlah_bintang = 2*i - 1
    kalimat = ""
    for j in range(0, jumlah_spasi):
        kalimat = kalimat + " "
    for j in range(0, jumlah_bintang):
        kalimat = kalimat + "*"
    print(kalimat)

for i in range (1, angka):
    jumlah_spasi = i
    jumlah_bintang = 2*(angka-i) - 1
    kalimat = ""
    for j in range(0, jumlah_spasi):
        kalimat = kalimat + " "
    for j in range(0, jumlah_bintang):
        kalimat = kalimat + "*"
    print(kalimat)
a = 5
b = 3
print(f"Variabel a, bernilai: {a + b}")








# 
#input
# 1

# output
# *

# input 2
#  *
# ***
#  *
    
# input 3
#   *
#  ***
# *****   
#  ***
#   *
    
# input 4
#    *
#   ***
#  *****
# *******  
#  *****
#   ***
#    * 

# input 5
#     *
#    ***
#   *****
#  ******* 
# *********  
#  *******
#   *****
#    ***
#     *