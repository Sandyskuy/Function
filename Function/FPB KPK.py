#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Function untuk menghitung fpb dari dua bilangan a dan b.
def hitung_fpb(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

#Function untuk menghitung kpk dari dua bilangan a dan b.
def hitung_kpk(a, b):

    kpk = a * b // hitung_fpb(a, b)
    return kpk

# Alur program
pilihan = input("Pilih fpb atau kpk: ") #untuk memilih kpk atau fpb

if pilihan == "fpb": #jika nemilih fpb maka rumus ini akan dijalankan
    bil1 = int(input("Masukkan bilangan pertama: ")) #menginputkan bilangan pertama
    bil2 = int(input("Masukkan bilangan kedua: ")) #menginputkan bilangan kedua
    hasil = hitung_fpb(bil1, bil2) #hasil dari memasukkan bilangan pertama dan kedua
    print("FPB dari", bil1, "dan", bil2, "adalah", hasil) #untuk menampilkan hasil dari perhitungan fpb
    
elif pilihan == "kpk": #jika nemilih kpk maka rumus ini akan dijalankan
    bil1 = int(input("Masukkan bilangan pertama: ")) #menginputkan bilangan pertama
    bil2 = int(input("Masukkan bilangan kedua: ")) #menginputkan bilangan kedua
    hasil = hitung_kpk(bil1, bil2) #hasil dari memasukkan bilangan pertama dan kedua
    print("KPK dari", bil1, "dan", bil2, "adalah", hasil) #untuk menampilkan hasil dari perhitungan kpk
    
else:
    print("Pilihan tidak valid!") #jika memilih diluar fpb dan kpk maka akan muncul pilihan tidak valid


# In[ ]:





# In[ ]:




