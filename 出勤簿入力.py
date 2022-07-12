from email import message
from tkinter import *
from tkinter import ttk
import tkinter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def submit():
    try:

        ID = IDs.get()
        pw = pws.get()

        days = dayss.get().split(',')

        mon = mons.get().split(',')
        tue = tues.get().split(',')
        wed = weds.get().split(',')
        thu = thus.get().split(',')
        fri = fris.get().split(',')
        sat = sats.get().split(',')

        mon.append(mont.get())
        tue.append(tuet.get())
        wed.append(wedt.get())
        thu.append(thut.get())
        fri.append(frit.get())
        sat.append(satt.get())

        month = int(months.get())
        yurei = yureis.get()

        D = {'月': mon, '火': tue, '水': wed, '木': thu, '金': fri, '土': sat}

        browser = webdriver.Chrome(ChromeDriverManager().install())

        browser.get("http://time.shozemi.com/teacher/calendar")
        sleep(1)
        elem = browser.find_element_by_name('login_id')
        elem.send_keys(ID)
        elem = browser.find_element_by_name('password')
        elem.send_keys(pw)
        elem = browser.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[2]/div/div/div[2]/form/fieldset/input')
        elem.click()
        sleep(1)


        #書き込むカレンダーへ移動
        elem = browser.find_element_by_xpath('//*[@id="header-nav"]/div/ul/li[2]/a')
        elem.click()
        sleep(0.2)
        try:
            elem = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/h2')
            realmonth = elem.text[5:-1]
        
            if month  < int(realmonth):
                elem_login = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[1]/button[1]')
                elem_login.click()

            elem = browser.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[1]')
            elem.click()

        except:
            elem = browser.find_element_by_xpath('//*[@id="main_content"]/div[6]/div/div/div[3]/button[2]')
            elem.click()
            
            elem = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/h2')
            realmonth = elem.text[5:-1]
            
            if month  < int(realmonth):
                elem_login = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[1]/button[1]')
                elem_login.click()
            sleep(0.5)
            elem = browser.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr/td[1]')
            elem.click()

        #書き込む日付に移動
        
        sleep(0.5)
        elem = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/span')
        cm = elem.text.split('/')[1]
        
        while int(cm) != month:
            try:
                elem_next = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/a[2]')
                elem_next.click()
                elem_date = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/span')
                cm = elem_date.text.split('/')[1]
            except:
                sleep(0.5)
                elem = browser.find_element_by_xpath('//*[@id="main_content"]/div[9]/div/div/div[3]/button')
                elem.click()
                sleep(0.5)
                elem_date = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/span')
                cm = elem_date.text.split('/')[1]


        
        #月～土のコマを書く
        date = 1
        while date < 31:
            for day in days:
                if day in elem_date.text:
                    elem_apr = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[2]')
                    print('--------')
                    print(elem_apr.text)
                    if elem_apr.text == '未承認':
                        if day != '土':

                            L = []
                            arrive = ''
                            last = ''
                            for i in D[day][:-1]:
                                if '前' in i:
                                    L.append(5)
                                    last = '18:00'
                                    arrive = '17:00'
                                elif '後' in i:
                                    L.append(6)
                                    last = '18:45'
                                    if not arrive:
                                        arrive = '17:40'
                                elif '5' in i:
                                    L.append(9)
                                    last = '18:45'
                                    if not arrive:
                                        arrive = '17:05'
                                if '6' in i:
                                    L.append(10)
                                    last = '20:25'
                                    if not arrive:
                                        if yurei == day:
                                            arrive = '18:25'
                                        else:
                                            arrive = '18:35'
                                if '7' in i:
                                    L.append(11)
                                    last = '22:20'
                                    if not arrive:
                                        arrive = '20:05'

                        else:
                            L = []
                            arrive = ''
                            last = ''
                            for i in D[day][:-1]:
                                if '小1' in i:
                                    L.append(2)
                                    last = '14:10'
                                    arrive = '13:00'
                                if '小2' in i:
                                    L.append(3)
                                    last = '14:50'
                                    if not arrive:
                                        arrive = '13:45'
                                if '小3' in i:
                                    L.append(4)
                                    last = '15:45'
                                    if not arrive:
                                        arrive = '14:40'
                                elif '3' in i:
                                    L.append(7)
                                    last = '14:50'
                                    if not arrive:
                                        arrive = '13:10'
                                if '小4' in i:
                                    L.append(5)
                                    last = '16:30'
                                    if not arrive:
                                        arrive = '15:25'
                                elif '4' in i:
                                    L.append(8)
                                    last = '16:20'
                                    if not arrive:
                                        arrive = '14:40'
                                if '5' in i:
                                    L.append(9)
                                    last = '18:00'
                                    if not arrive:
                                        arrive = '16:20'
                                if '6' in i:
                                    L.append(10)
                                    last = '19:35'
                                    if not arrive:
                                        arrive = '17:55'
                                if '7' in i:
                                    L.append(11)
                                    last = '21:05'
                                    if not arrive:
                                        arrive = '19:25'
                        sleep(0.2)
                        try:
                            elem_start = browser.find_element_by_xpath('//*[@id="start"]')
                            elem_start.send_keys(arrive)
                        except :
                            sleep(0.2)
                            elem = browser.find_element_by_xpath('//*[@id="main_content"]/div[9]/div/div/div[3]/button')
                            elem.click()
                            sleep(0.2)
                            elem_start = browser.find_element_by_xpath('//*[@id="start"]')
                            elem_start.send_keys(arrive)
                            
                        elem_end = browser.find_element_by_xpath('//*[@id="end"]')
                        elem_end.send_keys(last)

                        checklist = ['//*[@id="group_class_total_time"]','//*[@id="meeting_total_time"]','//*[@id="hokou_total_time"]']
                        for cl in checklist:
                            elem = browser.find_element_by_xpath(cl)
                            if elem.get_attribute("textContent") != '0':
                                sleep(0.5)
                                elem_start.send_keys('13:00')
                                elem_end.send_keys('22:20')

                        for path in L:
                            elem_koma = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[3]/td/table/tbody/tr['+ str(path) +']/td[1]/input')
                            elem_koma.click()
                        #夕礼
                        if  yurei == day:
                            elem_eve = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[2]/tr[1]/td[1]/select')
                            elem_eve.send_keys('5')

                        #交通費
                        elem_eve = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[2]/tr[2]/td/input')
                        elem_eve.send_keys(Keys.CONTROL + "a")
                        elem_eve.send_keys(Keys.DELETE)
                        elem_eve.send_keys(D[day][-1])

                        elem_koma = browser.find_element_by_xpath('//*[@id="confirm_record"]')
                        elem_koma.click()

                        try:
                            sleep(0.5)
                            elem_koma = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button')
                            elem_koma.click()
                            sleep(0.5)
                        except:
                            elem_koma = browser.find_element_by_xpath('//*[@id="main_content"]/div[9]/div/div/div[3]/button')
                            elem_koma.click()
                            sleep(0.5)


            try:
                elem_next = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/a[2]')
                elem_next.click()
            except:
                sleep(0.2)
                elem = browser.find_element_by_xpath('//*[@id="main_content"]/div[9]/div/div/div[3]/button')
                elem.click()
                sleep(0.2)
                elem_next = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/a[2]')
                elem_next.click()

            elem_date = browser.find_element_by_xpath('//*[@id="main_content"]/table/tbody[1]/tr[1]/td[1]/span')
            date += 1
            if date == 30 and str(month) not in elem_date.text.split('/')[1]:
                break
        sleep(5)

    finally:
        browser.close()
        browser.quit()

def keep():
    # データ書き込み
    f = open(textfile, 'w')
    f.write(IDs.get()+ '/' +pws.get()+ '/' +dayss.get()+ '/' +mons.get()+ '/' +mont.get()+ '/' +tues.get()+ '/' +tuet.get()+ '/' +weds.get()+ '/' +wedt.get()+ '/' +thus.get()+ '/' +thut.get()+ '/' +fris.get()+ '/' +frit.get()+ '/' +sats.get()+ '/' +satt.get()+ '/' +months.get() +'/' +yureis.get())
    f.close()

root = Tk()
root.title('出勤簿自動入力アプリ')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label = ttk.Label(frame1, text='ID', padding=(5, 2))
label.grid(row=0, column=0, sticky=E)

label = ttk.Label(frame1, text='Password', padding=(5, 2))
label.grid(row=1, column=0, sticky=E)

label = ttk.Label(frame1, text='', padding=(5, 2))
label.grid(row=2, column=0, sticky=E)

label = ttk.Label(frame1, text='登塾する曜日 ex)月,水,金', padding=(5, 2))
label.grid(row=3, column=0, sticky=E)

label = ttk.Label(frame1, text='中高生は時限の数字のみ', padding=(5, 2))
label.grid(row=4, column=1, sticky=E)

label = ttk.Label(frame1, text='小学生はコマ数の前に前半、後半をつけて', padding=(5, 2))
label.grid(row=5, column=1, sticky=E)

label = ttk.Label(frame1, text='↓交通費(円)', padding=(5, 2))
label.grid(row=5, column=2, sticky=E)

label = ttk.Label(frame1, text='月曜日のコマ ex)5前半,5後半,6,7', padding=(5, 2))
label.grid(row=6, column=0, sticky=E)

label = ttk.Label(frame1, text='火曜日のコマ ex)5,6,7', padding=(5, 2))
label.grid(row=7, column=0, sticky=E)

label = ttk.Label(frame1, text='水曜日のコマ ex)5前半,5後半,6,7', padding=(5, 2))
label.grid(row=8, column=0, sticky=E)

label = ttk.Label(frame1, text='木曜日のコマ ex)5,6,7', padding=(5, 2))
label.grid(row=9, column=0, sticky=E)

label = ttk.Label(frame1, text='金曜日のコマ ex)5前半,5後半,6,7', padding=(5, 2))
label.grid(row=10, column=0, sticky=E)

label = ttk.Label(frame1, text='土曜の小学生は前に小をつけて。', padding=(5, 2))
label.grid(row=11, column=1, sticky=E)

label = ttk.Label(frame1, text='土曜日のコマ ex)小1,小2,3,4,5,6,7', padding=(5, 2))
label.grid(row=12, column=0, sticky=E)

label = ttk.Label(frame1, text='予約する月(数字のみ)', padding=(5, 2))
label.grid(row=13, column=0, sticky=E)

label = ttk.Label(frame1, text='夕礼のある曜日 ex) 水', padding=(5, 2))
label.grid(row=14, column=0, sticky=E)


m = tkinter.Message(
    frame1,
    aspect=200,
    relief="raised",
    text='平日: 5限17:15～18:35         6限 18:45～20:05         7限 20:15～21:35',
    )
m.grid(row=15, column=0, sticky=E)

m = tkinter.Message(
    frame1,
    aspect=150,
    relief="raised",
    text='土曜: 小1限13:10～13:55           小2限13:55～14:40          小3限14:50～15:35        小4限15:35～16:20',
    )
m.grid(row=15, column=1, sticky=E)

m = tkinter.Message(
    frame1,
    aspect=85,
    relief="raised",
    text='土曜: 3限13:20～14:40          4限 14:50～16:10         5限 16:30～17:50          6限 18:05～19:25       7限 19:35～20:55',
    )
m.grid(row=15, column=2, sticky=E)

textfile = '値の記憶を白紙に戻したい場合はこれ削除してください.txt'
if os.path.isfile(textfile):
    f = open(textfile, 'r')
    text = f.read().split('/')
    f.close()
else:
    f = open(textfile, 'w')
    f.write('////////////////')
    f.close()
    f = open(textfile, 'r')
    text = f.read().split('/')
    f.close()


# ID Entry
IDs = StringVar()
IDs_entry = ttk.Entry(
    frame1,
    textvariable=IDs,
    width=20)
IDs_entry.insert(0, text[0])
IDs_entry.grid(row=0, column=1)

# pw Entry
pws = StringVar()
pws_entry = ttk.Entry(
    frame1,
    textvariable=pws,
    width=20)
pws_entry.insert(0, text[1])
pws_entry.grid(row=1, column=1)

# days Entry
dayss = StringVar()
dayss_entry = ttk.Entry(
    frame1,
    textvariable=dayss,
    width=20,)
dayss_entry.insert(0, text[2])
dayss_entry.grid(row=3, column=1)




# mons Entry
mons = StringVar()
mons_entry = ttk.Entry(
    frame1,
    textvariable=mons,
    width=20,)
mons_entry.insert(0, text[3])
mons_entry.grid(row=6, column=1)


mont = StringVar()
mont_entry = ttk.Entry(
    frame1,
    textvariable=mont,
    width=10,)
mont_entry.insert(0, text[4])
mont_entry.grid(row=6, column=2)

# tue Entry
tues = StringVar()
tues_entry = ttk.Entry(
    frame1,
    textvariable=tues,
    width=20,)
tues_entry.insert(0, text[5])
tues_entry.grid(row=7, column=1)

tuet = StringVar()
tuet_entry = ttk.Entry(
    frame1,
    textvariable=tuet,
    width=10,)
tuet_entry.insert(0, text[6])
tuet_entry.grid(row=7, column=2)

# wed Entry
weds = StringVar()
weds_entry = ttk.Entry(
    frame1,
    textvariable=weds,
    width=20,)
weds_entry.insert(0, text[7])
weds_entry.grid(row=8, column=1)

wedt = StringVar()
wedt_entry = ttk.Entry(
    frame1,
    textvariable=wedt,
    width=10,)
wedt_entry.insert(0, text[8])
wedt_entry.grid(row=8, column=2)

# thu Entry
thus = StringVar()
thus_entry = ttk.Entry(
    frame1,
    textvariable=thus,
    width=20,)
thus_entry.insert(0, text[9])
thus_entry.grid(row=9, column=1)

thut = StringVar()
thut_entry = ttk.Entry(
    frame1,
    textvariable=thut,
    width=10,)
thut_entry.insert(0, text[10])
thut_entry.grid(row=9, column=2)

# fri Entry
fris = StringVar()
fris_entry = ttk.Entry(
    frame1,
    textvariable=fris,
    width=20,)
fris_entry.insert(0, text[11])
fris_entry.grid(row=10, column=1)

frit = StringVar()
frit_entry = ttk.Entry(
    frame1,
    textvariable=frit,
    width=10,)
frit_entry.insert(0, text[12])
frit_entry.grid(row=10, column=2)

# sat Entry
sats = StringVar()
sats_entry = ttk.Entry(
    frame1,
    textvariable=sats,
    width=20,)
sats_entry.insert(0, text[13])
sats_entry.grid(row=12, column=1)

satt = StringVar()
satt_entry = ttk.Entry(
    frame1,
    textvariable=satt,
    width=10,)
satt_entry.insert(0, text[14])
satt_entry.grid(row=12, column=2)

# month Entry
months = StringVar()
months_entry = ttk.Entry(
    frame1,
    textvariable=months,
    width=20,)
months_entry.insert(0, text[15])
months_entry.grid(row=13, column=1)

# yurei Entry
yureis = StringVar()
yureis_entry = ttk.Entry(
    frame1,
    textvariable=yureis,
    width=20,)
yureis_entry.insert(0, text[16])
yureis_entry.grid(row=14, column=1)



frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=20, column=1, sticky=W)

button1 = ttk.Button(
    frame2, text='実行(1クリック)',
    command = submit)
button1.pack(side=LEFT)
button2 = ttk.Button(
    frame2, text='値を記憶',
    command = keep)
button2.pack(side=LEFT)
button3 = ttk.Button(frame2, text='Cancel', command=root.quit)
button3.pack(side=LEFT)



root.mainloop()
