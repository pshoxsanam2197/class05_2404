# 9-m
class Dars:
    def boshlash(self):
        print("Dars boshlandi")

    def tushuntirish(self):
        self.boshlash()
        print("Mavzu tushuntirildi")

    def yakunlash(self):
        self.tushuntirish()
        print("Dars tugadi")

d1 = Dars()
d1.boshlash()
print("-----------")
d1.tushuntirish()
print("-----------")
d1.yakunlash()

# 10-m
class Kompyuter :
    def yoq(self):
        print("Kompyuter yoqildi")

    def ishla(self):
        self.yoq()
        print("Kompyuter ishlamoqda")

    def ochir(self):
        self.ishla()
        print("Kompyuter o‘chirildi")

d1 = Kompyuter ()
d1.yoq()
print("-----------")
d1.ishla()
print("-----------")
d1.ochir()
