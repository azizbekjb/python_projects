from pywebio.output import put_text, put_buttons
import pywebio
from time import sleep
import random
def sontop_pc(x=10):
    pywebio.output.clear(scope=str(-1))
    global quyi, yuqori, taxmin
    quyi = 1
    yuqori = x
    put_text(f"1 da {x} gacha son o'ylang.\nSizga 3 soniya vaqt!")
    for i in [3, 2, 1, 'Boshladik!']:
        put_text(str(i))
        sleep(1)
    def guess():
        pywebio.output.clear(scope=str(-1))
        global taxmin
        taxmin = random.randint(quyi, yuqori)
        put_text(f"Siz {taxmin} sonini o'yladingiz!")
        put_buttons(['Kattaroq', 'Togri', 'Kichikroq'], onclick=[katta, bingo, kichik])
        pywebio.session.hold()
    def kichik():
        global yuqori
        yuqori = taxmin - 1
        guess()
    def katta():
        global yuqori
        yuqori = taxmin + 1
        guess()
    def bingo():
        put_text("Men yutdim!")

    guess()