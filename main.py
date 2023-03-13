import pyperclip, glob, os
from tkinter import *

sell, buy = [0], [0]
m_j = ''
m_p = ''


def FILES():
    list_of_files = glob.glob(r'*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def PRICE():
    global sell, buy
    k1 = 0
    f = open(FILES(), 'r', encoding='utf8')
    for line in f:
        if ('False' in line) and ('60003760' in line) and (k1 == 0):
            k1 += 1
            line1 = line.split(',')
            sell[0] = line1[0]
        elif 'True' in line:
            line2 = line.split(',')
            if int(line2[13]) <= 1:
                if int(line2[13]) == 1:
                    if int(line2[3]) >= 1:
                        buy[0] = line2[0]
                        break
                else:
                    buy[0] = line2[0]
                    break
    f.close()
    return sell, buy


# def MARGIN_jita():
#     global sell, buy, m_j
#
#     sell[0] = float(sell[0])
#     buy[0] = float(buy[0])
#
#     jita = round(100 - (sell[0] - ((sell[0] / 100) * 4.88) + ((buy[0] / 100) * 1.28)) / sell[0] * 100, 1)
#     return str(jita)


def MARGIN_perimeter():
    global sell, buy, m_p

    sell[0] = float(sell[0])
    buy[0] = float(buy[0])

    perimeter = round(((sell[0] - (sell[0] * 0.0488 + buy[0] * 0.01 + buy[0])) / sell[0] * 100), 2)
    return str(perimeter)


def COPY_change_sell():
    global sell
    sell_c = float(sell[0])
    sell_c_6 = str(sell_c).split('.')

    if len(str(sell_c)) == 4:
        return sell_c - 0.01
    elif len(str(sell_c)) == 7:
        return sell_c - 10
    elif len(str(sell_c)) == 8:
        return sell_c - 100
    elif len(str(sell_c)) == 9:
        return sell_c - 1000
    elif len(str(sell_c)) == 10:
        return sell_c - 10000
    elif len(str(sell_c)) == 11:
        return sell_c - 100000
    elif len(str(sell_c)) == 12:
        return sell_c - 1000000
    elif len(str(sell_c)) == 13:
        return sell_c - 10000000
    elif len(sell_c_6[0]) == 3:
        return sell_c - 0.1
    elif len(sell_c_6[0]) == 4:
        return sell_c - 1


def COPY_change_buy():
    global buy
    buy_c = float(buy[0])
    buy_c_6 = str(buy_c).split('.')

    if len(str(buy_c)) == 4:
        return buy_c + 0.01
    elif len(str(buy_c)) == 7:
        return buy_c + 10
    elif len(str(buy_c)) == 8:
        return buy_c + 100
    elif len(str(buy_c)) == 9:
        return buy_c + 1000
    elif len(str(buy_c)) == 10:
        return buy_c + 10000
    elif len(str(buy_c)) == 11:
        return buy_c + 100000
    elif len(str(buy_c)) == 12:
        return buy_c + 1000000
    elif len(str(buy_c)) == 13:
        return buy_c + 10000000
    elif len(buy_c_6[0]) == 3:
        return buy_c + 0.1
    elif len(buy_c_6[0]) == 4:
        return buy_c + 1


def chislo(h):
    if int(h) >= 0:
        h = h[::-1]
        h = h.split()
        k = 0
        sp1 = []
        for i in range(len(h[0])):
            if k == 3:
                sp1.append('.')
                sp1.append(h[0][i])
                k = 1
            else:
                sp1.append(h[0][i])
                k += 1
        return (''.join(sp1))[::-1]
    elif int(h) < 0:
        h = h[::-1]
        h = h[:len(h) - 1]
        h = h.split()
        k = 0
        sp1 = []
        for i in range(len(h[0])):
            if k == 3:
                sp1.append('.')
                sp1.append(h[0][i])
                k = 1
            else:
                sp1.append(h[0][i])
                k += 1
        return '-' + (''.join(sp1))[::-1]


def COPY_sell():
    pyperclip.copy(COPY_change_sell())


def COPY_buy():
    pyperclip.copy(COPY_change_buy())


def TABLE():
    global sell, buy

    sell[0] = float(sell[0])
    buy[0] = float(buy[0])
    price_for_label = round((sell[0] - (sell[0] * 0.0488 + buy[0] * 0.01 + buy[0])), 0)
    price_for_label1 = round((sell[0] - (sell[0] * 0.0488 + buy[0] * 0.01 + buy[0])), 2)
    price_for_label = str(price_for_label).split('.')
    price_for_label = int(price_for_label[0])

    lbl2 = Label(text='      1 || ' + chislo(str(price_for_label)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl2.place(x=0, y=40)

    lbl3 = Label(text='      5 || ' + chislo(str(price_for_label * 5)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl3.place(x=0, y=67)

    lbl4 = Label(text='    10 || ' + chislo(str(price_for_label * 10)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl4.place(x=0, y=94)

    lbl5 = Label(text='    50 || ' + chislo(str(price_for_label * 50)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl5.place(x=0, y=121)

    lbl6 = Label(text='  100 || ' + chislo(str(price_for_label * 100)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl6.place(x=0, y=148)

    lbl7 = Label(text='  500 || ' + chislo(str(price_for_label * 500)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl7.place(x=0, y=175)

    lbl8 = Label(text='    1k || ' + chislo(str(price_for_label * 1000)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl8.place(x=0, y=202)

    lbl9 = Label(text='  10k || ' + chislo(str(price_for_label * 10000)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl9.place(x=0, y=229)

    lbl10 = Label(text='100k || ' + chislo(str(price_for_label * 100000)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl10.place(x=0, y=256)

    lbl11 = Label(text='  1kk || ' + chislo(str(price_for_label * 1000000)), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl11.place(x=0, y=283)


def click_btn1():
    PRICE()
    COPY_sell()
    TABLE()
    lbl1 = Label(text=MARGIN_perimeter(), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl1.place(x=110, y=5)


def click_btn2():
    PRICE()
    COPY_buy()
    TABLE()
    lbl1 = Label(text=MARGIN_perimeter(), font=0, bg="#2F4F4F", fg='#FFFFFF')
    lbl1.place(x=110, y=5)


window = Tk()
window.title("EVE MARGIN")
window.geometry('220x320')
window.configure(bg='#2F4F4F')
window.attributes("-topmost", True)

btn1 = Button(text="Sell",
              background="#2F4F4F",
              foreground="#FFFFFF",
              font="16",
              command=click_btn1)
btn1.place(x=0, y=0)

btn2 = Button(text="Buy",
              background="#2F4F4F",
              foreground="#FFFFFF",
              font="16",
              command=click_btn2)
btn2.place(x=50, y=0)

window.mainloop()

# c3 = Checkbutton(window, text='Sell', command=cp1)
# c3.grid(column=4, row=0)
#
# c4 = Checkbutton(window, text='Buy', command=cp2)
# c4.grid(column=4, row=1)
# while True:
#     PRICE()
#     lbl = Label(window, text=MARGIN_perimeter(), font=("Arial", 14))
#     lbl.grid(column=0, row=0)
#
#     lbl = Label(window, text=MARGIN_jita(), font=("Arial", 14))
#     lbl.grid(column=0, row=1)


# c3 = Checkbutton(window, text='Sell', command=cp1)
# c3.grid(column=4, row=0)
#
# c4 = Checkbutton(window, text='Buy', command=cp2)
# c4.grid(column=4, row=1)
