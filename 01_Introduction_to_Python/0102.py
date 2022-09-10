 #region n t raws
 
 # invoke

#print()

# print("ecodation")
# print() # bir satır boş
# print("eğitim")
# print()
# print("kurumları")
# print("ecodation\neğitim\nkurumları")
# print("ecodation\teğitim\tkurumları")
# print("ecodation\t\teğitim\t\tkurumları")
# print("istanbul\nteknokent\tecodation\teğitim\tkurumları")
# print("merhaba \"ecodation\"")
# print('merhaba "ecodation"')
# print("\"")
# print(34)
# print(True)
# print('Merhaba Ece\'nin Dünyası')
# print('Türkiyen\'nin Başkenti Ankara\'dır')


# raw_string

# 2. çözüm
# print(r"C:\Windows\System32\networklist")

# endregion 

#region end sep keyword

# end keyword?
"""
print("Hayatta", "En", "Hakiki")
print("Mürşit", "İlimdir")
print("----------------")

print("Hayatta", "En", "Hakiki", end="****")
print("Mürşit", "İlimdir")
print("----------------")
"""


# sep keyword?
"""
print("Hayatta", "En", "Hakiki", "Mürşit", "İlimdir")
print("----------------")
print("Hayatta", "En", "Hakiki", "Mürşit", "İlimdir", sep="+")
"""



"""
istanbul-teknopark
ecodation>>eğitim>>kurumları.
"""

print("istanbul", "teknopark", sep="-")
print("ecodation","eğitim", "kurumları", sep=">>", end=".")
print("ben neredeyim?")
#endregion

#region comment line → yorum satırı
"""
1- sen bu satırı/satırları görmezden gel"!
2- runtime da iken bu satırı yorumlama"!
3- bu bir kod değil, bu kendim için yazdığım bir hatırlatma"! dersiniz.
"""
#tek satır
"""
çoklu yorum satırı
budur
"""
'''
buda olabilir
'''

# yazı ile 
print("otuz dört")
# sayı ile
print(34)
#endregion

#region ornek_1
"""
Dünya'nın♥En♥Güzel♥Şehri→İstanbul.

alt+3  ♥
alt + 26 →


print("Dünya'nın", "En", "Güzel", "Şehri", sep="♥", end="→")
print("İstanbul", end=".")
"""
#endregion

#region ornek_2
"""
"Ege'nin"☼"İncisi"☼"İzmir"!

alt+15  ☼
"""
print("\"Ege'nin\"", "\"İncisi\"", "\"İzmir!\"", sep="☼")
#endregion

#region int
# ilk veri tipimiz → integer
print(1400)
print(85)
print(33)
print(38)
print(10000)
print(20)
print(19)
print(50)
#endregion

#region float
# ikinci veri tipimiz → float
print(3.14)
print(1.70)
print(0.1)
print(15.8)
#endregion

#region string
# üçüncü veri tipimiz → string
print("ecodation")
print("istanbul")
print("python")
print("17545396534")
#endregion

#region boolean
# dördümcü veri tipimiz → boolean
print(True)
#lütfen  print(true)  ile yazmayın → case sensitive
print(False)
#ürün satışta mi
#endregion

#region type
#  → parantez içindeki değerin tipi geri döngürür

print(type(2020))           #<class 'int'>
print(type(34.4))           #<class 'float'>
print(type("ecodation"))    #<class 'str'> 
print(type(True))           #<class 'bool'>
 #endregion

#region aritmetik-operatorler
# aritmetik operatörler
"""
1→  +   toplama
2→  -   çıkarma
3→  *   çarpma
4→  /   bölme
5→  //  tam bölme
6→  **  üst alma
7→  %   mod alma
"""
#endregion

#region +/- binary
"""
print(3+3)
print(6-3)
print(3-6)
print(0.15 - 15)
print(.15 - 15)
"""
#endregion

#region +/- unary işaret
"""
print(+2)
print(-2)
"""
#endregion

#region */ 
"""
print(4*4)
print(.4*4)
print(type(.4*4))
print(9/3)
print(9/2)
print(type(9/2))
print(17/.4)
print(10/0)
"""
#endregion

#region ** üst alma
"""
print(4**4)
print(2**4)
print(16**0.5)
print(16**(1/2))
print(type(16**0.5))
"""
#endregion

#region // - tam bölme
"""
print(12/7)
print(12//7)
print(12//7.)
print(-13/5)
print(-13//5) #*****
"""
#endregion

#region % - mod alma - kalanı bulma
"""
print(15%4)
print(15%2) #**********
print(8%3)
print(15%0)
"""
#endregion

#region operator_oncelikleri
"""
1→  +, -        unary
2→  **          üst alma
3→  *, /, %     çarpma, bölme, mod alma
4→  +,-         toplama çıkarma
"""
"""
print(3+4*5)
print(15%4*2)   #% left-side binding
print(15%4%2)   #% left-side binding
print(2**2**3)  #** right-side binding
"""
#endregion










