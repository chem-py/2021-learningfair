from tkinter import*
import tkinter as tk
import tkinter.ttk as ttk


# BMI 측정
def func1():
    win1 = Toplevel(win)
    win1.geometry("800x600")
    win1.title("BMI")
    win1.option_add("*Font", "함초롬돋움 18")

    def bmical():
        height = int(ent1.get())
        weight = int(ent2.get())
        BMI = (weight / (height*height)) * 10000
        lab8.config(text = "%.2f" %BMI)
        if BMI >= 40 :
            lab9.config(text = "당신은 현재 심각한 비만 상태입니다...")
        elif BMI >= 30 :
            lab9.config(text = "당신은 지금 비만입니다. 운동하세요!")
        elif BMI >= 25 :
            lab9.config(text = "당신은 비만에 접어들었습니다. 관리하세요.")
        elif BMI >= 23:
            lab9.config(text = "당신은 과체중입니다.")
        elif BMI >= 18.5:
            lab9.config(text = "당신은 현재 정상입니다.")
        elif BMI < 18.5 :
            lab9.config(text = "당신은 현재 저체중입니다. 많이 드세요!")

    lab1 = Label(win1, text = "BMI 측정", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "lightcoral")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win1, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "lightcoral")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win1, text = "- 키(cm)를 입력해주세요.")
    lab3.place(x = 30, y = 150)

    lab4 = Label(win1, text = "- 몸무게(kg)를 입력해주세요.")
    lab4.place(x = 390, y = 150)

    lab5 = Label(win1, text = "cm")
    lab5.place(x = 190, y = 200)

    lab6 = Label(win1, text = "kg")
    lab6.place(x = 550, y = 200)

    lab7 = Label(win1, text = ">> 당신의 BMI는\t\t입니다.", font = ("함초롬돋움", 22, "bold"))
    lab7.config(bg = "white")
    lab7.place(x = 40, y = 390)

    lab8 = Label(win1, font = ("함초롬돋움", 22, "bold"))
    lab8.config(fg = "red")
    lab8.config(bg = "white")
    lab8.place(x = 300, y = 390)

    lab9 = Label(win1, font = ("함초롬돋움", 20))
    lab9.place(x = 85, y = 445)

    lab10 = Label(win1, font = ("함초롬돋움", 20))
    lab10.config(text = "-------------------------------------------------------")
    lab10.config(fg = "red")
    lab10.place(x = 40, y = 300)


    ent1 = Entry(win1, bd = 3, width = 10)
    ent1.place(x = 40, y = 210)
    
    ent2 = Entry(win1, bd = 3, width = 10)
    ent2.place(x = 400, y = 210)

    btn = Button(win1, text = "계산", font = ("함초롬돋움", 18, "bold"))
    btn.config(bg = "white")
    btn.config(fg = "indianred")
    btn.config(text = "계산")
    btn.config(command = bmical)
    btn.place(x = 710, y = 200)

    win1.mainloop()

# 우울증 자가진단
def func2():
    win2 = Toplevel(win)
    win2.geometry("800x600")
    win2.title("우울증 자가진단")

    lab1 = Label(win2, text = "우울증 자가진단", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "yellowgreen")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win2, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "yellowgreen")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win2, font = ("함초롬돋움", 20))
    lab3.config(text = "우울증 자가진단 테스트를 시작합니다.\n\n각 질문들을 자세히 읽어보시고, \n최근 3~4주 이내 얼마나 자주 그렇게 경험하고 느꼈는지\n 자신의 상태를 가장 잘 나타낸다고 \n생각되는 답변을 선택해주세요.")
    lab3.place(x = 70, y = 170)

    def nextpage():

        win2.destroy()
        win2_1 = Toplevel(win)
        win2_1.geometry("800x600")
        win2_1.title("우울증 자가진단")
        win2_1.option_add("*Font", "함초롬돋움 14")
        
        lab1_1 = Label(win2_1, text = "우울증 자가진단", font = ("함초롬돋움", 30, "bold"))
        lab1_1.config(bg = "yellowgreen")
        lab1_1.config(fg = "white")
        lab1_1.config(width = 35, height = 2)
        lab1_1.place(x = 0, y = 0)

        lab2_1 = Label(win2_1, text = "chem.py", font = ("함초롬돋움", 15))
        lab2_1.config(width = 66, height = 2, anchor = SE)
        lab2_1.config(bg = "yellowgreen")
        lab2_1.place(x = 0, y = 540)

        lab3_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab3_1.config(text = "1. 미래에 대한 희망이 없다.")
        lab3_1.place(x = 20, y = 150)

        lab4_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab4_1.config(text = "2. 이유없이 죄책감이 든다.")
        lab4_1.place(x = 20, y = 195)

        lab5_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab5_1.config(text = "3. 하루종일 우울한 기분이 든다.")
        lab5_1.place(x = 20, y = 240)

        lab6_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab6_1.config(text = "4. 나만 소외되는 느낌이 든다.")
        lab6_1.place(x = 20, y = 285)

        lab7_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab7_1.config(text = "5. 별일 아닌 것에 대해서도 눈물이 자주난다.")
        lab7_1.place(x = 20, y = 330)

        lab8_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab8_1.config(text = "6. 갑자기 체중증가 또는 감소 증상이 나타났다.")
        lab8_1.place(x = 20, y = 375)

        lab9_1 = Label(win2_1, font = ("함초롬돋움", 15))
        lab9_1.config(text = "7. 열등감이 생기고 그로 인해 스트레스를 받는다.")
        lab9_1.place(x = 20, y = 420)

        lab10_1 = Label(win2_1, font = ("함초롬돋움", 15, "bold"), width = 50)
        lab10_1.config(fg = "red")
        lab10_1.config(bg = "white")
        lab10_1.place(x = 30, y = 480)

        lab11_1 = Label(win2_1, font = ("함초롬돋움", 13, "bold"))
        lab11_1.config(fg = "blue")
        lab11_1.config(text = "1번: 해당되지 않는다. / 2번: 가끔그렇다. / 3번: 자주 그렇다. / 4번: 항상 그렇다.")
        lab11_1.place(x = 100, y = 115)

        def result():
            sum = var1.get() + var2.get() + var3.get() + var4.get() + var5.get() + var6.get() + var7.get()
            btn1_1.config(text = "점수: %d" %sum)
            if sum >= 21:
                 lab10_1.config(text = "당신은 우울증이 매우 심각하여, 전문가와의 상담치료가 필요합니다.")
            elif sum >= 15 :
                lab10_1.config(text = "당신은 심한 우울증이 의심되며 주변 지인들의 도움이 필요합니다.")
            elif sum >= 8:
                lab10_1.config(text = "당신은 우울증 초기여서, 가끔 우울하지만 극복 가능한 상태입니다.")
            elif sum >= 0:
                lab10_1.config(text = "당신은 일반적인 상태로, 우울증이 아닙니다.")
                 
        btn1_1 = Button(win2_1, text = "결과 확인", bd = 5, font = ("함초롬돋움", 15, "bold"))
        btn1_1.config(bg = "white")
        btn1_1.config(fg = "green")
        btn1_1.place(x = 660, y = 470)
        btn1_1.config(command = result)

        var1 = IntVar()
        rd1_1 = Radiobutton(win2_1, text = "1번", variable = var1, value = 0, bg = "white")
        rd1_1.place(x = 530, y = 150)
        rd1_2 = Radiobutton(win2_1, text = "2번", variable = var1, value = 1, bg = "white")
        rd1_2.place(x = 590, y = 150)
        rd1_3 = Radiobutton(win2_1, text = "3번", variable = var1, value = 2, bg = "white")
        rd1_3.place(x = 650, y = 150)
        rd1_4 = Radiobutton(win2_1, text = "4번", variable = var1, value = 3, bg = "white")
        rd1_4.place(x = 710, y = 150)

        var2 = IntVar()
        rd2_1 = Radiobutton(win2_1, text = "1번", variable = var2, value = 0, bg = "white")
        rd2_1.place(x = 530, y = 195)
        rd2_2 = Radiobutton(win2_1, text = "2번", variable = var2, value = 1, bg = "white")
        rd2_2.place(x = 590, y = 195)
        rd2_3 = Radiobutton(win2_1, text = "3번", variable = var2, value = 2, bg = "white")
        rd2_3.place(x = 650, y = 195)
        rd2_4 = Radiobutton(win2_1, text = "4번", variable = var2, value = 3, bg = "white")
        rd2_4.place(x = 710, y = 195)

        var3 = IntVar()
        rd3_1 = Radiobutton(win2_1, text = "1번", variable = var3, value = 0, bg = "white")
        rd3_1.place(x = 530, y = 240)
        rd3_2 = Radiobutton(win2_1, text = "2번", variable = var3, value = 1, bg = "white")
        rd3_2.place(x = 590, y = 240)
        rd3_3 = Radiobutton(win2_1, text = "3번", variable = var3, value = 2, bg = "white")
        rd3_3.place(x = 650, y = 240)
        rd3_4 = Radiobutton(win2_1, text = "4번", variable = var3, value = 3, bg = "white")
        rd3_4.place(x = 710, y = 240)

        var4 = IntVar()
        rd4_1 = Radiobutton(win2_1, text = "1번", variable = var4, value = 0, bg = "white")
        rd4_1.place(x = 530, y = 285)
        rd4_2 = Radiobutton(win2_1, text = "2번", variable = var4, value = 1, bg = "white")
        rd4_2.place(x = 590, y = 285)
        rd4_3 = Radiobutton(win2_1, text = "3번", variable = var4, value = 2, bg = "white")
        rd4_3.place(x = 650, y = 285)
        rd4_4 = Radiobutton(win2_1, text = "4번", variable = var4, value = 3, bg = "white")
        rd4_4.place(x = 710, y = 285)

        var5 = IntVar()
        rd5_1 = Radiobutton(win2_1, text = "1번", variable = var5, value = 0, bg = "white")
        rd5_1.place(x = 530, y = 330)
        rd5_2 = Radiobutton(win2_1, text = "2번", variable = var5, value = 1, bg = "white")
        rd5_2.place(x = 590, y = 330)
        rd5_3 = Radiobutton(win2_1, text = "3번", variable = var5, value = 2, bg = "white")
        rd5_3.place(x = 650, y = 330)
        rd5_4 = Radiobutton(win2_1, text = "4번", variable = var5, value = 3, bg = "white")
        rd5_4.place(x = 710, y = 330)

        var6 = IntVar()
        rd6_1 = Radiobutton(win2_1, text = "1번", variable = var6, value = 0, bg = "white")
        rd6_1.place(x = 530, y = 375)
        rd6_2 = Radiobutton(win2_1, text = "2번", variable = var6, value = 1, bg = "white")
        rd6_2.place(x = 590, y = 375)
        rd6_3 = Radiobutton(win2_1, text = "3번", variable = var6, value = 2, bg = "white")
        rd6_3.place(x = 650, y = 375)
        rd6_4 = Radiobutton(win2_1, text = "4번", variable = var6, value = 3, bg = "white")
        rd6_4.place(x = 710, y = 375)

        var7 = IntVar()
        rd7_1 = Radiobutton(win2_1, text = "1번", variable = var7, value = 0, bg = "white")
        rd7_1.place(x = 530, y = 420)
        rd7_2 = Radiobutton(win2_1, text = "2번", variable = var7, value = 1, bg = "white")
        rd7_2.place(x = 590, y = 420)
        rd7_3 = Radiobutton(win2_1, text = "3번", variable = var7, value = 2, bg = "white")
        rd7_3.place(x = 650, y = 420)
        rd7_4 = Radiobutton(win2_1, text = "4번", variable = var7, value = 3, bg = "white")
        rd7_4.place(x = 710, y = 420)
        
        win2_1.mainloop()
                        
    btn1 = Button(win2, text = "다음", bd = 5, font = ("함초롬돋움", 18, "bold"))
    btn1.config(bg = "white")
    btn1.config(fg = "green")
    btn1.place(x = 680, y = 450)
    btn1.config(command = nextpage)

    win2.mainloop()

    
# 불면증 자가진단
def func3():
    win3 = Toplevel(win)
    win3.geometry("800x600")
    win3.title("불면증 자가진단")
    win3.option_add("*Font", "함초롬돋움 18")

    lab1 = Label(win3, text = "불면증 자가진단", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "mediumturquoise")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win3, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "mediumturquoise")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win3, font = ("함초롬돋움", 20))
    lab3.config(text = "불면증 자가진단 테스트를 시작합니다.\n\n각 질문들을 자세히 읽어보시고, \n최근 3~4주 이내 얼마나 자주 그렇게 경험하고 느꼈는지\n 자신의 상태를 가장 잘 나타낸다고 \n생각되는 답변을 선택해주세요.")
    lab3.place(x = 70, y = 170)

    def nextpage():

        win3.destroy()
        win3_1 = Toplevel(win)
        win3_1.geometry("800x600")
        win3_1.title("불면증 자가진단")
        win3_1.option_add("*Font", "함초롬돋움 15")
        
        lab1_1 = Label(win3_1, text = "불면증 자가진단", font = ("함초롬돋움", 30, "bold"))
        lab1_1.config(bg = "mediumturquoise")
        lab1_1.config(fg = "white")
        lab1_1.config(width = 35, height = 2)
        lab1_1.place(x = 0, y = 0)

        lab2_1 = Label(win3_1, text = "chem.py", font = ("함초롬돋움", 15))
        lab2_1.config(width = 66, height = 2, anchor = SE)
        lab2_1.config(bg = "mediumturquoise")
        lab2_1.place(x = 0, y = 540)

        lab3_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab3_1.config(text = "1. 잠에 들기까지 많은 시간이 걸리거나 전혀 잘 수 없다.")
        lab3_1.place(x = 7, y = 120)

        lab4_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab4_1.config(text = "2. 밤에 자다 깨면 전혀 다시 잘 수 없어 곤란하다.")
        lab4_1.place(x = 7, y = 165)

        lab5_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab5_1.config(text = "3. 전체적인 수면의 질에 불만족한다.")
        lab5_1.place(x = 7, y = 210)

        lab6_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab6_1.config(text = "4. 최근 매일의 기분이 가라앉아있거나 우울하다.")
        lab6_1.place(x = 7, y = 255)

        lab7_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab7_1.config(text = "5. 최근 신체적 정신적 활동이 어려울 만큼 심각하게 떨어졌다.")
        lab7_1.place(x = 7, y = 300)

        lab8_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab8_1.config(text = "6. 낮 동안 매우 심한 졸음이 있다.")
        lab8_1.place(x = 7, y = 345)

        lab9_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab9_1.config(text = "7. 낮잠을 포함하여 충분한 수면시간(6~7시간)을 가지지 못했다.")
        lab9_1.place(x = 7, y = 390)

        lab10_1 = Label(win3_1, font = ("함초롬돋움", 15))
        lab10_1.config(text = "8. 원하는 시간보다 일찍 깨서 이후 잠들 수 없었던 적이 있었다.")
        lab10_1.place(x = 7, y = 435)

        lab11_1 = Label(win3_1, font = ("함초롬돋움", 16, "bold"), width = 50)
        lab11_1.config(fg = "red")
        lab11_1.config(bg = "white")
        lab11_1.place(x = 15, y = 485)

        def result():
            sum = int(cb1.get()[0]) + int(cb2.get()[0]) + int(cb3.get()[0]) + int(cb4.get()[0]) + int(cb5.get()[0]) + int(cb6.get()[0]) + int(cb7.get()[0]) + int(cb8.get()[0])
            btn1_1.config(text = "점수: %d" %sum)
            if 3>=sum>=0:
                lab11_1.config(text = "좋은 수면을 취하고 있습니다.")
            elif 7>=sum>=4:
                lab11_1.config(text = "초기 불면증을 의심할 수 있습니다.")
            elif sum>=8:
                lab11_1.config(text = "불면증일 가능성이 높습니다. 전문가와 상담해보세요")
                 
        btn1_1 = Button(win3_1, text = "결과 확인", bd = 5, font = ("함초롬돋움", 15, "bold"))
        btn1_1.config(bg = "white")
        btn1_1.config(fg = "darkcyan")
        btn1_1.place(x = 680, y = 475)
        btn1_1.config(command = result)

        cblist = ["0. 전혀 그렇지 않다.", "1. 그렇지 않다.", "2. 그렇다.", "3. 매우 그렇다."]
        
        cb1 = ttk.Combobox(win3_1, width = 18)
        cb1.config(values = cblist)
        cb1.place(x = 570, y = 120)

        cb2 = ttk.Combobox(win3_1, width = 18)
        cb2.config(values = cblist)
        cb2.place(x = 570, y = 165)

        cb3 = ttk.Combobox(win3_1, width = 18)
        cb3.config(values = cblist)
        cb3.place(x = 570, y = 210)

        cb4 = ttk.Combobox(win3_1, width = 18)
        cb4.config(values = cblist)
        cb4.place(x = 570, y = 255)

        cb5 = ttk.Combobox(win3_1, width = 18)
        cb5.config(values = cblist)
        cb5.place(x = 570, y = 300)

        cb6 = ttk.Combobox(win3_1, width = 18)
        cb6.config(values = cblist)
        cb6.place(x = 570, y = 345)

        cb7 = ttk.Combobox(win3_1, width = 18)
        cb7.config(values = cblist)
        cb7.place(x = 570, y = 390)        

        cb8 = ttk.Combobox(win3_1, width = 18)
        cb8.config(values = cblist)
        cb8.place(x = 570, y = 435)  

        win3_1.mainloop()

    btn1 = Button(win3, text = "다음", bd = 5, font = ("함초롬돋움", 18, "bold"))
    btn1.config(bg = "white")
    btn1.config(fg = "darkcyan")
    btn1.place(x = 680, y = 450)
    btn1.config(command = nextpage)
    
    win3.mainloop()
  
# ADHD 자가진단
def func4():
    win4 = Toplevel(win)
    win4.geometry("800x600")
    win4.title("ADHD 자가진단")
    win4.option_add("*Font", "함초롬돋움 18")

    lab1 = Label(win4, text = "ADHD 자가진단", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "cornflowerblue")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win4, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "cornflowerblue")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win4, font = ("함초롬돋움", 20))
    lab3.config(text = "ADHD\n (주의력 결핍 및 과잉 행동 장애)\n 자가진단 테스트를 시작합니다.\n\n각 질문들을 자세히 읽어보시고, \n살면서 얼마나 자주 그렇게 경험하고 느꼈는지 \n 자신의 상태를 가장 잘 나타낸다고 \n생각되는 답변을 선택해주세요.")
    lab3.place(x = 120, y = 160)

    def nextpage():

        win4.destroy()
        win4_1 = Toplevel(win)
        win4_1.geometry("800x600")
        win4_1.title("ADHD 자가진단")
        win4_1.option_add("*Font", "함초롬돋움 15")
        
        lab1_1 = Label(win4_1, text = "ADHD 자가진단", font = ("함초롬돋움", 30, "bold"))
        lab1_1.config(bg = "cornflowerblue")
        lab1_1.config(fg = "white")
        lab1_1.config(width = 35, height = 2)
        lab1_1.place(x = 0, y = 0)

        lab2_1 = Label(win4_1, text = "chem.py", font = ("함초롬돋움", 15))
        lab2_1.config(width = 66, height = 2, anchor = SE)
        lab2_1.config(bg = "cornflowerblue")
        lab2_1.place(x = 0, y = 540)

        lab3_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab3_1.config(text = "1. 말을 너무 많이 한다.")
        lab3_1.place(x = 15, y = 120)

        lab4_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab4_1.config(text = "2. 자기 순서를 기다리지 못한다.")
        lab4_1.place(x = 15, y = 165)

        lab5_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab5_1.config(text = "3. 질문을 끝까지 듣지 않고 대답한다.")
        lab5_1.place(x = 15, y = 210)

        lab6_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab6_1.config(text = "4. 다른 사람을 방해하고 간섭한다.")
        lab6_1.place(x = 15, y = 255)

        lab7_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab7_1.config(text = "5. 외부자극에 의해 쉽게 산만해진다.")
        lab7_1.place(x = 15, y = 300)

        lab8_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab8_1.config(text = "6. 가만히 앉아 있지 못하고 계속 움직이거나 꿈틀거린다.")
        lab8_1.place(x = 15, y = 345)

        lab9_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab9_1.config(text = "7. 과제나 놀이를 할 때 지속적으로 집중하기 어렵다.")
        lab9_1.place(x = 15, y = 390)

        lab10_1 = Label(win4_1, font = ("함초롬돋움", 15))
        lab10_1.config(text = "8. 자신이 해야할 일을 끝마치지 못한다.")
        lab10_1.place(x = 15, y = 435)

        lab11_1 = Label(win4_1, font = ("함초롬돋움", 16, "bold"), width = 55)
        lab11_1.config(fg = "red")
        lab11_1.config(bg = "white")
        lab11_1.place(x = 10, y = 480)

        def result():
            sum = int(cb1.get()[0]) + int(cb2.get()[0]) + int(cb3.get()[0]) + int(cb4.get()[0]) + int(cb5.get()[0]) + int(cb6.get()[0]) + int(cb7.get()[0]) + int(cb8.get()[0])
            btn1_1.config(text = "점수: %d" %sum)
            if sum<=10:
                lab11_1.config(text = "당신은 ADHD와 거리가 멉니다. 안심하셔도 좋습니다.")
            elif 20>=sum>=11:
                lab11_1.config(text = "크게 문제될 것이 없습니다. 그러나 급속한 변화를 보일 수 있으므로 \n추후에도 ADHD 자가진단을 하며 관심을 가지시는 것이 좋을 것 같습니다.")
            elif sum>=21:
                lab11_1.config(text = "ADHD일 가능성이 있습니다. 많은 경우 학습이나 관계에서 다양한\n 문제가 발생할 소지가 있으므로 정확한 진단을 해보시는 것이 좋습니다.")
                 
        btn1_1 = Button(win4_1, text = "결과 확인", bd = 5, font = ("함초롬돋움", 15, "bold"))
        btn1_1.config(bg = "white")
        btn1_1.config(fg = "navy")
        btn1_1.place(x = 680, y = 475)
        btn1_1.config(command = result)

        cblist = ["1. 전혀 그렇지 않다.", "2. 그렇지 않다.", "3. 그렇다.", "4. 매우 그렇다."]
        
        cb1 = ttk.Combobox(win4_1)
        cb1.config(values = cblist)
        cb1.place(x = 525, y = 120)

        cb2 = ttk.Combobox(win4_1)
        cb2.config(values = cblist)
        cb2.place(x = 525, y = 165)

        cb3 = ttk.Combobox(win4_1)
        cb3.config(values = cblist)
        cb3.place(x = 525, y = 210)

        cb4 = ttk.Combobox(win4_1)
        cb4.config(values = cblist)
        cb4.place(x = 525, y = 255)

        cb5 = ttk.Combobox(win4_1)
        cb5.config(values = cblist)
        cb5.place(x = 525, y = 300)

        cb6 = ttk.Combobox(win4_1)
        cb6.config(values = cblist)
        cb6.place(x = 525, y = 345)

        cb7 = ttk.Combobox(win4_1)
        cb7.config(values = cblist)
        cb7.place(x = 525, y = 390)        

        cb8 = ttk.Combobox(win4_1)
        cb8.config(values = cblist)
        cb8.place(x = 525, y = 435)  

        win4_1.mainloop()

    btn1 = Button(win4, text = "다음", bd = 5, font = ("함초롬돋움", 18, "bold"))
    btn1.config(bg = "white")
    btn1.config(fg = "navy")
    btn1.place(x = 680, y = 450)
    btn1.config(command = nextpage)

    win4.mainloop()
  
# 대인기피증 자가진단
def func5():
    win5 = Toplevel(win)
    win5.geometry("800x600")
    win5.title("대인기피증 자가진단")
    win5.option_add("*Font", "함초롬돋움 18")

    lab1 = Label(win5, text = "대인기피증 자가진단", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "orange")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win5, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "orange")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win5, font = ("함초롬돋움", 20))
    lab3.config(text = "대인기피증 자가진단 테스트를 시작합니다.\n\n각 질문들을 자세히 읽어보시고, \n최근 1년간 얼마나 자주 그렇게 경험하고 느꼈는지 \n 자신의 상태를 가장 잘 나타낸다고 \n생각되는 답변을 선택해주세요.")
    lab3.place(x = 110, y = 180)

    def nextpage():
        
        win5.destroy()
        win5_1 = Toplevel(win)
        win5_1.geometry("800x600")
        win5_1.title("대인기피증 자가진단")
        win5_1.option_add("*Font", "함초롬돋움 15")
                
        lab1_1 = Label(win5_1, text = "대인기피증 자가진단", font = ("함초롬돋움", 30, "bold"))
        lab1_1.config(bg = "orange")
        lab1_1.config(fg = "white")
        lab1_1.config(width = 35, height = 2)
        lab1_1.place(x = 0, y = 0)

        lab2_1 = Label(win5_1, text = "chem.py", font = ("함초롬돋움", 15))
        lab2_1.config(width = 66, height = 2, anchor = SE)
        lab2_1.config(bg = "orange")
        lab2_1.place(x = 0, y = 540)

        lab3_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab3_1.config(text = "1. 당신은 낯선 사람과의 눈 맞춤이 힘들게 느껴집니까?")
        lab3_1.place(x = 15, y = 170)

        lab4_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab4_1.config(text = "2. 당신은 발표 자리에서 아무 말도 하지 못한 경험이 있습니까?")
        lab4_1.place(x = 15, y = 220)

        lab5_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab5_1.config(text = "3. 당신은 대화할 때 입술이나 손에 떨림이 느껴지십니까?")
        lab5_1.place(x = 15, y = 270)

        lab6_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab6_1.config(text = "4. 당신은 스스로 공포감을 느낀다고 생각하십니까?")
        lab6_1.place(x = 15, y = 320)

        lab7_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab7_1.config(text = "5. 당신은 새로운 장소와 새로운 사람을 가능한 피하십니까?")
        lab7_1.place(x = 15, y = 370)

        lab8_1 = Label(win5_1, font = ("함초롬돋움", 15))
        lab8_1.config(text = "6. 당신은 이런 증상들로 인해 일상생활에 불편함을 느끼십니까?")
        lab8_1.place(x = 15, y = 420)

        lab9_1 = Label(win5_1, font = ("함초롬돋움", 16, "bold"), width = 50)
        lab9_1.config(fg = "red")
        lab9_1.config(bg = "white")
        lab9_1.place(x = 20, y = 475)

        lab10_1 = Label(win5_1, font = ("함초롬돋움", 15, "bold"))
        lab10_1.config(text = "자신에게 해당되는 항목만을 체크해주세요.")
        lab10_1.config(fg = "blue")
        lab10_1.place(x = 30, y = 120)

        def result():
            sum = CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get() + CheckVar5.get() + CheckVar6.get()
            btn1_1.config(text = "점수: %d" %sum)
            if sum <= 1:
                lab9_1.config(text = "당신은 정상적인 범위 내에서 생활하고 계십니다.")
            elif 2<= sum <= 3:
                lab9_1.config(text = "대인기피증 증상이 약간 보이나, 일상생활에 큰 지장은 없습니다.")
            elif sum>=4:
                lab9_1.config(text = "대인기피증이 의심됩니다.\n 일상생활에 꽤 많은 영향을 끼치고 있는 것으로 보입니다.")
                         
        btn1_1 = Button(win5_1, text = "결과 확인", bd = 5, font = ("함초롬돋움", 15, "bold"))
        btn1_1.config(bg = "white")
        btn1_1.config(fg = "orangered")
        btn1_1.place(x = 660, y = 470)
        btn1_1.config(command = result)

        CheckVar1 = IntVar()
        cb1 = Checkbutton(win5_1, text = "check", variable = CheckVar1)
        cb1.place(x = 670, y = 170)

        CheckVar2 = IntVar()
        cb2 = Checkbutton(win5_1, text = "check", variable = CheckVar2)
        cb2.place(x = 670, y = 220)

        CheckVar3 = IntVar()
        cb3 = Checkbutton(win5_1, text = "check", variable = CheckVar3)
        cb3.place(x = 670, y = 270)

        CheckVar4 = IntVar()
        cb4 = Checkbutton(win5_1, text = "check", variable = CheckVar4)
        cb4.place(x = 670, y = 320)

        CheckVar5 = IntVar()
        cb5 = Checkbutton(win5_1, text = "check", variable = CheckVar5)
        cb5.place(x = 670, y = 370)

        CheckVar6 = IntVar()
        cb6 = Checkbutton(win5_1, text = "check", variable = CheckVar6)
        cb6.place(x = 670, y = 420)

        win5_1.mainloop()

    btn1 = Button(win5, text = "다음", bd = 5, font = ("함초롬돋움", 18, "bold"))
    btn1.config(bg = "white")
    btn1.config(fg = "orangered")
    btn1.place(x = 680, y = 460)
    btn1.config(command = nextpage)

    win5.mainloop()
  
# 휴대폰 중독 자가진단
def func6():
    win6 = Toplevel(win)
    win6.geometry("800x600")
    win6.title("휴대폰 중독 자가진단")
    win6.option_add("*Font", "함초롬돋움 18")

    lab1 = Label(win6, text = "휴대폰 중독 자가진단", font = ("함초롬돋움", 30, "bold"))
    lab1.config(bg = "mediumpurple")
    lab1.config(fg = "white")
    lab1.config(width = 35, height = 2)
    lab1.place(x = 0, y = 0)

    lab2 = Label(win6, text = "chem.py", font = ("함초롬돋움", 15))
    lab2.config(width = 66, height = 2, anchor = SE)
    lab2.config(bg = "mediumpurple")
    lab2.place(x = 0, y = 540)

    lab3 = Label(win6, font = ("함초롬돋움", 20))
    lab3.config(text = "휴대폰 중독 자가진단 테스트를 시작합니다.\n\n각 질문들을 자세히 읽어보시고, \n최근 6개월간 얼마나 자주 휴대폰을 사용했는지 \n 자신의 상태를 가장 잘 나타낸다고 \n생각되는 답변을 선택해주세요.")
    lab3.place(x = 110, y = 190)

    def nextpage():

        win6.destroy()
        win6_1 = Toplevel(win)
        win6_1.geometry("800x600")
        win6_1.title("휴대폰 중독 자가진단")
        win6_1.option_add("*Font", "함초롬돋움 15")
        
        lab1_1 = Label(win6_1, text = "휴대폰 중독 자가진단", font = ("함초롬돋움", 30, "bold"))
        lab1_1.config(bg = "mediumpurple")
        lab1_1.config(fg = "white")
        lab1_1.config(width = 35, height = 2)
        lab1_1.place(x = 0, y = 0)

        lab2_1 = Label(win6_1, text = "chem.py", font = ("함초롬돋움", 15))
        lab2_1.config(width = 66, height = 2, anchor = SE)
        lab2_1.config(bg = "mediumpurple")
        lab2_1.place(x = 0, y = 540)

        lab3_1 = Label(win6_1, font = ("함초롬돋움", 15))
        lab3_1.config(text = "1. 스마트폰 이용시간을 조절 하는 것이 어렵다.")
        lab3_1.place(x = 10, y = 140)

        lab4_1 = Label(win6_1, font = ("함초롬돋움", 15))
        lab4_1.config(text = "2. 스마트폰 이용 때문에 친구 혹은 동료, 사회적 관계에서 \n심한 갈등을 경험한 적이 있다.")
        lab4_1.place(x = 10, y = 200)

        lab5_1 = Label(win6_1, font = ("함초롬돋움", 15))
        lab5_1.config(text = "3. 스마트폰 이용 때문에 건강에 문제가 생긴 적이 있다.")
        lab5_1.place(x = 10, y = 280)

        lab6_1 = Label(win6_1, font = ("함초롬돋움", 15))
        lab6_1.config(text = "4. 스마트폰을 이용하고 싶은 충동을 강하게 느낀다.")
        lab6_1.place(x = 10, y = 340)

        lab7_1 = Label(win6_1, font = ("함초롬돋움", 15))
        lab7_1.config(text = "5. 스마트폰 때문에 업무(학업 혹은 직업 등) 수행에 어려움이 있다.")
        lab7_1.place(x = 10, y = 400)

        lab8_1 = Label(win6_1, font = ("함초롬돋움", 16, "bold"), width = 50)
        lab8_1.config(fg = "red")
        lab8_1.config(bg = "white")
        lab8_1.place(x = 20, y = 470)

        def result():
            sum = int(cb1.get()[0]) + int(cb2.get()[0]) + int(cb3.get()[0]) + int(cb4.get()[0]) + int(cb5.get()[0])
            btn1_1.config(text = "점수: %d" %sum)
            if 5 <= sum <= 9:
                lab8_1.config(text = "당신은 일반 사용자군입니다.")
            elif 10<= sum <= 14:
                lab8_1.config(text = "당신은 잠재적위험성 단계에 있습니다.")
            elif sum>=15:
                lab8_1.config(text = "당신은 고위험 단계에 있습니다.")
                 
        btn1_1 = Button(win6_1, text = "결과 확인", bd = 5, font = ("함초롬돋움", 15, "bold"))
        btn1_1.config(bg = "white")
        btn1_1.config(fg = "darkslateblue")
        btn1_1.place(x = 650, y = 460)
        btn1_1.config(command = result)

        cblist = ["1. 전혀 그렇지 않다.", "2. 그렇지 않다.", "3. 그렇다.", "4. 매우 그렇다."]
        
        cb1 = ttk.Combobox(win6_1, width = 15)
        cb1.config(values = cblist)
        cb1.place(x = 600, y = 140)

        cb2 = ttk.Combobox(win6_1, width = 15)
        cb2.config(values = cblist)
        cb2.place(x = 600, y = 200)

        cb3 = ttk.Combobox(win6_1, width = 15)
        cb3.config(values = cblist)
        cb3.place(x = 600, y = 280)

        cb4 = ttk.Combobox(win6_1, width = 15)
        cb4.config(values = cblist)
        cb4.place(x = 600, y = 340)

        cb5 = ttk.Combobox(win6_1, width = 15)
        cb5.config(values = cblist)
        cb5.place(x = 600, y = 400)

        win6_1.mainloop()

    btn1 = Button(win6, text = "다음", bd = 5, font = ("함초롬돋움", 18, "bold"))
    btn1.config(bg = "white")
    btn1.config(fg = "darkslateblue")
    btn1.place(x = 680, y = 460)
    btn1.config(command = nextpage)
    
    win6.mainloop()
  
# 메인화면 구성

win = Tk()
win.geometry("800x600")
win.title("자가진단 프로그램")
win.config(bg = "white")

lab1 = Label(win, text = "건강 자가진단 프로그램", font = ("함초롬돋움", 30, "bold"))
lab1.config(width = 35, height = 2)
lab1.config(bg = "lightskyblue")
lab1.place(x = 0, y = 0)

lab2 = Label(win, text = "chem.py", font = ("함초롬돋움", 15))
lab2.config(width = 66, height = 2, anchor = SE)
lab2.config(bg = "lightskyblue")
lab2.place(x = 0, y = 540)

btn1 = Button(win, text = "BMI", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn1.config(bg = "indianred")
btn1.config(fg = "white")
btn1.config(width = 9, height = 2)
btn1.place(x = 45, y = 155)
btn1.config(command = func1)

btn2 = Button(win, text = "우울증", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn2.config(bg = "yellowgreen")
btn2.config(fg = "white")
btn2.config(width = 9, height = 2)
btn2.place(x = 305, y = 155)
btn2.config(command = func2)

btn3 = Button(win, text = "불면증", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn3.config(bg = "mediumturquoise")
btn3.config(fg = "white")
btn3.config(width = 9, height = 2)
btn3.place(x = 565, y = 155)
btn3.config(command = func3)

btn4 = Button(win, text = "ADHD", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn4.config(bg = "royalblue")
btn4.config(fg = "white")
btn4.config(width = 9, height = 2)
btn4.place(x = 45, y = 355)
btn4.config(command = func4)

btn5 = Button(win, text = "대인기피증", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn5.config(bg = "darkorange")
btn5.config(fg = "white")
btn5.config(width = 9, height = 2)
btn5.place(x = 305, y = 355)
btn5.config(command = func5)

btn6 = Button(win, text = "휴대폰\n중독", bd = 10, font = ("함초롬돋움", 25, "bold"))
btn6.config(bg = "slateblue")
btn6.config(fg = "white")
btn6.config(width = 9, height = 2)
btn6.place(x = 565, y = 355)
btn6.config(command = func6)

win.mainloop()
