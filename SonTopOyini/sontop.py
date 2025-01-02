import random
def sontop(x = 10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 da {x} gacha son o'yladim. Topa olasizmi?", end='\n')

    while True:
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kichikroq son ayting")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting")
        else:
            print("Yutdingiz")
            break