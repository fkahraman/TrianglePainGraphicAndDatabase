"""
        FATİH KAHRAMAN          31.05.2018

        fatih.khrmn@hotmail.com
"""

from pylab import *         #grafik ve sayısal işlem birleşik kütüphane
import sys                  #sistem kütüphanesi


if __name__ == '__main__':

    a_acilari = []
    b_acilari = []
    c_acilari = []

    grafik_uzunluk = int(input("Grafik uzunluğunu giriniz: "))

    ct = 0
    try:
        while(ct < grafik_uzunluk):

            print ("Sırasıyla üçgenin kenarlarını giriniz: ")
            kenar_a = int(input("1. Kenarı giriniz: "))
            kenar_b = int(input("2. kenarı giriniz: "))
            kenar_c = int(input("3. kenarı giriniz: "))
            print("\n")

            k = (kenar_b * kenar_b) + (kenar_c * kenar_c) - (kenar_a * kenar_a)
            l = k / (2 * kenar_b * kenar_c)
            val = 180 / 3.14159265
            a_acisi = math.acos(l) * val
            print("a acisi: ", round(a_acisi, 2), "derecedir.")

            m = (kenar_a * kenar_a) + (kenar_c * kenar_c) - (kenar_b * kenar_b)
            n = m / (2 * kenar_a * kenar_c)
            b_acisi = math.acos(n) * val
            print("b acisi: ", round(b_acisi, 2), "derecedir.")

            p = (kenar_a * kenar_a) + (kenar_b * kenar_b) - (kenar_c * kenar_c)
            r = p / (2 *  kenar_b * kenar_a)
            c_acisi = math.acos(r) * val
            print("c acisi: ", round(c_acisi, 2), "derecedir.")

            if(0 <= a_acisi and a_acisi <= 180 and 0 <= b_acisi and b_acisi <= 180 and 0 <= c_acisi and c_acisi <= 180):
                print("Böyle bir üçgen vardır.")
                c_acilari.append(c_acisi)
                b_acilari.append(b_acisi)
                a_acilari.append(a_acisi)

            else:
                print("Böyle bir üçgen yoktur.")

            ct += 1
    except ValueError:
        print("Böyle bir üçgen olamayacağından program sonlandırıldı.")
        sys.exit()

    grid(True)
    title("SIRASIYLA GIRILEN KENARLARA GORE ACILARIN DEGISIM")
    xlabel("UCGEN NO")
    ylabel("ACI")

    x = arange(1, grafik_uzunluk+1, 1)

    dt_c = array(c_acilari)
    dt_b = array(b_acilari)
    dt_a = array(a_acilari)

    plot(x, dt_c, "-g") #kırmızı
    plot(x, dt_c, "og", label = 'c acilari')

    plot(x, dt_b, "-b") #mavi
    plot(x, dt_b, "ob", label = 'b acilari')

    plot(x, dt_a, "-r") #yeşil
    plot(x, dt_a, "or", label = 'a acilari')

    legend()
    show()