from typing import ClassVar


class Mobile:
    fp = "Yes"

    @classmethod
    def is_fp(cls):
        print(cls.fp)



realme = Mobile()
redmi  = Mobile()
geek   = Mobile()

print("Class FP", Mobile.fp)
print("RealMe", realme.fp)
print("RedMi", redmi.fp)
print("Geek", geek.fp)

Mobile.fp = "No"

print()
print("Class FP", Mobile.fp)
print("RealMe", realme.fp)
print("RedMi", redmi.fp)
print("Geek", geek.fp)

realme.fp = "Not Working"

print()
print("Class FP", Mobile.fp)
print("RealMe", realme.fp)
print("RedMi", redmi.fp)
print("Geek", geek.fp)