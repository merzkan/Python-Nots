#re module
'''
Python'daki re modülü, düzenli ifadeler (regular expressions, kısaca regex) ile çalışmak için kullanılan bir modüldür. 
Düzenli ifadeler, metin içinde belirli bir desenin aranması, bulunması veya değiştirilmesi için kullanılan güçlü bir araçtır.
re modülü, metin verisini işleme ve analiz etme konusunda son derece kullanışlıdır. 
Bu modül sayesinde, karmaşık arama ve değiştirme işlemleri kolayca gerçekleştirilebilir.

Düzenli İfadeler (Regex) Nedir?
Düzenli ifadeler, bir metni belirli desenlere göre analiz etmek için kullanılan sembollerin bir kombinasyonudur.
Örneğin, bir e-posta adresini, telefon numarasını veya tarih formatını tanımak için kullanılabilir. 
Regex, karakterlerin dizisini tanımlamak ve metinde bu dizilere karşılık gelen verileri bulmak için kullanılır.
'''
import re

#result = dir(re)
#print(result)

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#re.findall()
result1 = re.findall("Python",str)
#['Python', 'Python']
result2 = len(result1)
#2
print(result1)
print(result2)

print("****************************************************")

#re.split()
result3 = re.split(" ",str)
#['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberiniz', '|', '40', 'saat']
result4 = re.split("R",str)
#['Python Kursu: Python Programlama ', 'ehberiniz | 40 saat']

print(result3)
print(result4)

print("****************************************************")

#re.sub()  # değiştirme
result4 = re.sub(" ","-",str)
#Python-Kursu:-Python-Programlama-Rehberiniz-|-40-saat
result5 = re.sub("\s","-",str)#\s boşluk karakterlerini belirtiyor
#Python-Kursu:-Python-Programlama-Rehberiniz-|-40-saat

print(result4)
print(result5)

print("****************************************************")

# re.search()

result6 = re.search("Python",str)
#<re.Match object; span=(0, 6), match='Python'>
result7 = result6.span()
#(0, 6)
result8 = result6.start()
#0
result9 = result6.end()
#6
result10 = result6.group()
#Python
result11 = result6.string
#Python Kursu: Python Programlama Rehberiniz | 40 saat

print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)

print("****************************************************")
print("****************************************************")

# regular expression 

"""
    []  Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""

result12 = re.findall("[abc]",str)
#['a', 'a', 'a', 'b', 'a', 'a']
result13 = re.findall("[sat]",str)
#['t', 's', 't', 'a', 'a', 'a', 's', 'a', 'a', 't']
result14 = re.findall("[a-e]", str)
#['a', 'a', 'a', 'e', 'b', 'e', 'a', 'a']
result15 = re.findall("[a-z]", str)
#['y', 't', 'h', 'o', 'n', 'u', 'r', 's', 'u', 'y', 't', 'h', 'o', 'n', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', 'e', 'h', 'b', 'e', 'r', 'i', 'n', 
#'i', 'z', 's', 'a', 'a', 't']
result16 = re.findall("[0-5]", str)
#['4', '0']
result17= re.findall("[^abc]", str)
#['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'm', 'l', 'm', ' ', 'R', 
#'e', 'h', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', '4', '0', ' ', 's', 't']
result18 = re.findall("[^0-9]", str)
#['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 
#'a', ' ', 'R', 'e', 'h', 'b', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', ' ', 's', 'a', 'a', 't']

print(result12)
print(result13)
print(result14)
print(result15)
print(result16)
print(result17)
print(result18)

print("****************************************************")

"""
    .   Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

"""

result19 = re.findall("...", str)
#['Pyt', 'hon', ' Ku', 'rsu', ': P', 'yth', 'on ', 'Pro', 'gra', 'mla', 'ma ', 
#'Reh', 'ber', 'ini', 'z |', ' 40', ' sa']
result20 = re.findall("Py..on", str)
#['Python', 'Python']

print(result19)
print(result20)

print("****************************************************")

"""
    ^   Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result21 = re.findall("^P",str)
#['P']

print(result21)

print("****************************************************")

"""
    $   Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result22 = re.findall("t$",str)
result23 = re.findall("saat$",str)
result24= re.findall("saatt$",str)

print(result22)
#['t']
print(result23)
#['saat']
print(result24)
#[]

print("****************************************************")

"""
     *  Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result25 = re.findall("sa*t",str)
#['saat']

print(result25)

print("****************************************************")

"""
     +  Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result26 = re.findall("sa+t",str)
#['saat']
print(result26)

print("****************************************************")

"""
    ?   Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma?n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result27 = re.findall("sa?t",str)
[]
print(result27)

print("****************************************************")

"""
    {}  Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result28 = re.findall("a{2}", str)
#['aa']
result29 = re.findall("[0-9]{2}", str)
#['40']

print(result28)
print(result29)

print("****************************************************")

"""
    |   alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

print("****************************************************")

"""
    ()  gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

print("****************************************************")



"""
    \   Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A  Belirtilen karakter string in başında mı ?
         \Athe => the string in başında mı 

    \Z  Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı

    \b  Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B  Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d  [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D  [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s  Boşluk karakterlerini arar.  
    \S  Boşluk karakterleri dışındakiler.
    \w  Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W  \w nin tam tersi
    
"""