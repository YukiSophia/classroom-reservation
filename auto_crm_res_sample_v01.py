from tkinter import *
from tkinter import ttk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

def submit():
    try:
        ID = []
        ADS = []

        url = URL.get()
        print(url)
        text = clubname.get()
        ID.append(text)
        text = username.get()
        ID.append(text)
        text = Number.get()
        ID.append(text)

        ins = institution.get()
        crm = insnum.get().split(',')

        year = yearnum.get()
        month = monthnum.get()
        date = datenum.get().split(',')
        time = timenum.get()

        text = mail.get()
        ADS.append(text)
        text = call.get()
        ADS.append(text)

        for d in date:
            for c in crm:
                count = 1
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(url)
                sleep(2)

                #サークル名、名前、学籍番号
                for id in ID:
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div['+ str(count) +']/div/div[3]/div/div/input')
                    element.send_keys(id)
                    count += 1

                #資料読んだか
                for n in ['4','5']:
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div['+ n +']/div/div[3]/div/div/div/label/input')
                    element.click()

                count = 1
                if '11' in ins:
                    #使いたい施設（11）
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[3]/div/label/input')
                    element.click()
                    sleep(0.5)
                    L = ['205','209','215','221','305','311','320','321','325','326','405','411','419','428','505','511','519','528','603','606','609','612','615','618','621','624','625','628','704','719','726']
                    for i in L:
                        if i in c:
                            element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div['+ str(count) +']/div/label/input')
                            element.click()
                            sleep(0.5)
                            break
                        else:
                            count += 1

                elif '14' in ins:
                    #使いたい施設（14）
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[3]/div/label/input')
                    element.click()
                    sleep(0.5)
                    L = ['101','106','201','206','207','309','310']
                    for i in L:
                        if i in c:
                            element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div['+ str(count) +']/div/label/input')
                            element.click()
                            sleep(0.5)
                            break
                        else:
                            count += 1

                elif '紀' in ins or 'k' in ins:
                    #使いたい施設（紀尾井）
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[4]/div/label/input')
                    element.click()
                    sleep(0.5)
                    L = ['101','103','104','105','107','108','109','111','112','113','115']
                    for i in L:
                        if i in c:
                            element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div['+ str(count) +']/div/label/input')
                            element.click()
                            sleep(0.5)
                            break
                        else:
                            count += 1

                elif '1' in ins:
                    #使いたい施設（1）
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[1]/div/label/input')
                    element.click()
                    sleep(1)
                    L = ['201','202','301','302','401','402','407','408']
                    for i in L:
                        if i in c:
                            element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div['+ str(count) +']/div/label/input')
                            element.click()
                            sleep(0.5)
                            break
                        else:
                            count += 1

                else:
                    print('1,11,14号館と紀尾井坂ビルのみに対応しています')


                #カレンダー
                if len(month) == 1:
                    month = '0' + month

                if len(d) == 1:
                    d = '0' + d

                
                element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div/input[1]')
                text = year +'/'+ month +'/' + d
                element.send_keys(text)
                sleep(5)
                #時間
                element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[9]/div/div[3]/div/div/input')
                element.send_keys(time)

                #共同で使うか(NO)
                element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[10]/div/div[3]/div/div[2]/div/label/input')
                element.click()

                #メアド、電話番号
                count = 12
                for ads in ADS:
                    element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div['+ str(count) +']/div/div[3]/div/div/input')
                    element.send_keys(ads)
                    count += 1

                sleep(5)
                #送信
            #  element = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
            #  element.click()

                sleep(2)
    finally:
        driver.close()
        driver.quit()

def keep():
    # 値の記憶
    f = open(textfile, 'w')
    f.write(URL.get()+ '彁' +clubname.get()+ '彁' +username.get()+ '彁' +Number.get()+ '彁' +institution.get()+ '彁' +insnum.get()+ '彁' +yearnum.get()+ '彁' +monthnum.get()+ '彁' +datenum.get()+ '彁' +timenum.get()+ '彁' +mail.get()+ '彁' +call.get())
    f.close()

root = Tk()
root.title('Entry Test')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='申請フォームのURL', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

label1 = ttk.Label(frame1, text='', padding=(5, 2))
label1.grid(row=1, column=0, sticky=E)

label1 = ttk.Label(frame1, text='サークル名', padding=(5, 2))
label1.grid(row=2, column=0, sticky=E)

label2 = ttk.Label(frame1, text='名前(姓と名の間に全角スペースを入れること)', padding=(5, 2))
label2.grid(row=3, column=0, sticky=E)

label3 = ttk.Label(frame1, text='学籍番号', padding=(5, 2))
label3.grid(row=4, column=0, sticky=E)

label4 = ttk.Label(frame1, text='', padding=(5, 2))
label4.grid(row=5, column=0, sticky=E)

label5 = ttk.Label(frame1, text='使用したい施設名(1,11,14号館,紀尾井坂ビルのみ)', padding=(5, 2))
label5.grid(row=6, column=0, sticky=E)

label6 = ttk.Label(frame1, text='教室名(複数選択可) 例)115,112', padding=(5, 2))
label6.grid(row=7, column=0, sticky=E)

label7 = ttk.Label(frame1, text='年(半角数字) 例)2022', padding=(5, 2))
label7.grid(row=8, column=0, sticky=E)

label8 = ttk.Label(frame1, text='月(半角数字) 例)4', padding=(5, 2))
label8.grid(row=9, column=0, sticky=E)

label9 = ttk.Label(frame1, text='日(半角数字)(複数選択可) 例)1,8,15', padding=(5, 2))
label9.grid(row=10, column=0, sticky=E)

label9 = ttk.Label(frame1, text='時間(半角文字) 例)17:20~21:00', padding=(5, 2))
label9.grid(row=11, column=0, sticky=E)

label9 = ttk.Label(frame1, text='学外団体との合同使用は自動で無になります！', padding=(5, 2))
label9.grid(row=12, column=1, sticky=E)

label9 = ttk.Label(frame1, text='メールアドレス', padding=(5, 2))
label9.grid(row=13, column=0, sticky=E)

label9 = ttk.Label(frame1, text='電話番号', padding=(5, 2))
label9.grid(row=14, column=0, sticky=E)

textfile = '値の記憶を白紙に戻したい場合はこれを削除してください.txt'
if os.path.isfile(textfile):
    f = open(textfile, 'r')
    text = f.read().split('彁')
    f.close()
else:
    f = open(textfile, 'w')
    f.write('彁彁彁彁彁彁彁彁彁彁彁彁')
    f.close()
    f = open(textfile, 'r')
    text = f.read().split('彁')
    f.close()


# URL Entry
URL = StringVar()
URL_entry = ttk.Entry(
    frame1,
    textvariable=URL,
    width=20)
URL_entry.insert(0, text[0])
URL_entry.grid(row=0, column=1)

# Clubname Entry
clubname = StringVar()
clubname_entry = ttk.Entry(
    frame1,
    textvariable=clubname,
    width=20)
clubname_entry.insert(0, text[1])
clubname_entry.grid(row=2, column=1)

# Username Entry
username = StringVar()
username_entry = ttk.Entry(
    frame1,
    textvariable=username,
    width=20,)
username_entry.insert(0, text[2])
username_entry.grid(row=3, column=1)

# Number Entry
Number = StringVar()
Number_entry = ttk.Entry(
    frame1,
    textvariable=Number,
    width=20,)
Number_entry.insert(0, text[3])
Number_entry.grid(row=4, column=1)



# institution Entry
institution = StringVar()
institution_entry = ttk.Entry(
    frame1,
    textvariable=institution,
    width=20,)
institution_entry.insert(0, text[4])
institution_entry.grid(row=6, column=1)

# insnum Entry
insnum = StringVar()
insnum_entry = ttk.Entry(
    frame1,
    textvariable=insnum,
    width=20,)
insnum_entry.insert(0, text[5])
insnum_entry.grid(row=7, column=1)

# year Entry
yearnum = StringVar()
yearnum_entry = ttk.Entry(
    frame1,
    textvariable=yearnum,
    width=20,)
yearnum_entry.insert(0, text[6])
yearnum_entry.grid(row=8, column=1)

# month Entry
monthnum = StringVar()
monthnum_entry = ttk.Entry(
    frame1,
    textvariable=monthnum,
    width=20,)
monthnum_entry.insert(0, text[7])
monthnum_entry.grid(row=9, column=1)

# date Entry
datenum = StringVar()
datenum_entry = ttk.Entry(
    frame1,
    textvariable=datenum,
    width=20,)
datenum_entry.insert(0, text[8])
datenum_entry.grid(row=10, column=1)

# time Entry
timenum = StringVar()
timenum_entry = ttk.Entry(
    frame1,
    textvariable=timenum,
    width=20,)
timenum_entry.insert(0, text[9])
timenum_entry.grid(row=11, column=1)

# mail Entry
mail = StringVar()
mail_entry = ttk.Entry(
    frame1,
    textvariable=mail,
    width=20,)
mail_entry.insert(0, text[10])
mail_entry.grid(row=13, column=1)

# call Entry
call = StringVar()
call_entry = ttk.Entry(
    frame1,
    textvariable=call,
    width=20,)
call_entry.insert(0, text[11])
call_entry.grid(row=14, column=1)



frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=20, column=1, sticky=W)

button1 = ttk.Button(
    frame2, text='OK',
    command = submit)
button1.pack(side=LEFT)
button2 = ttk.Button(
    frame2, text='値を記憶',
    command = keep)
button2.pack(side=LEFT)
button3 = ttk.Button(frame2, text='Cancel', command=root.quit)
button3.pack(side=LEFT)



root.mainloop()
