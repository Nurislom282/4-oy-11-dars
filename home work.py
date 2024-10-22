#6
import asyncio

def a_and_b(ism):
    i = 0
    yangi_ism = ""
    while i < len(ism):
        harf = ism[i]
        if harf == "ab":
            yangi_ism += '@'
        else:
            yangi_ism += harf
        i += 1
    return yangi_ism

ism = input("Ism kiriting:")
new = a_and_b(ism)
print(new)
