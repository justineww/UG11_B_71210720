x = input("Masukkan kalimat awal: ")
y = input("Masukkan kata untuk disisipkan: ")
z = int(input("Masukkan index: "))

def sisip(x,y,z):
    print(x[:z]+y+x[z:])
sisip(x,y,z)
