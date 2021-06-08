"""
Dosya okuma işlemi : 
	open()	:	dosyayı açmak için kullanılır.
	open("dosya.txt")	:	İlk parametre okumak istediğiniz dosyanın adıdır.
	open("dosya.txt", "r") : İkinci parametre dosyayı açma modudur.
	Bazı dosya modları : r, r+, w, w+, a, a+, x, x+
		
		'r'  ==> Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.
		'w'  ==> Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer dosya bulunamadıysa yeni bir dosya oluşturur.
		'a'  ==> Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya oluşturur.
	open("dosya.txt", "r", encoding="utf-8") : Türkçe karakter hatalarını düzeltir

"""

dosya = open("deneme.txt", "r", encoding="utf-8")
icerik = dosya.read() 
print(icerik)				
dosya.close()
#Sonuç : Dosya olmadığı için hata verdi

dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("deneme yazısı 1\n") 			
dosya.close()
#Sonuç : Dosyayı oluşturdu ve deneme yazısı yazdı.

dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("deneme yazısı 2\n")			
dosya.close()

dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("deneme yazısı 3\n")			
dosya.close()

dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("deneme yazısı 4\n")			
dosya.close()

dosya = open("deneme.txt", "r", encoding="utf-8")
icerik = dosya.read() 
print(icerik)				
dosya.close()
#Sonuç : 'deneme yazısı 4'. 
#4 defa deneme yazısı yazdırdığımız halde 'w' modu üstüne yazdığı için sadece sonuncuyu gördük."""

dosya = open("deneme.txt", "a", encoding="utf-8")
dosya.write("deneme yazısı 5\n")
dosya.close()
#Sonuç : Eğer "w" modunu kullansaydık deneme yazısı 4'ü siler deneme yazısı 5 yazardı.
#Ama biz "a" modunu kullandığımız için 'deneme yazısı 4' yazdı, alt satıra geçti ve 'deneme yazısı 5'i yazdı.
