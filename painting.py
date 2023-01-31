from tkinter import *
import tkinter as tk
from tkinter.colorchooser import * ##색깔 선택
from tkinter.simpledialog import * ##간단한 대화창
from tkinter.filedialog import *

###########기존 코드#############

##마우스 클릭시 실행되는 함수
def mouseClick(event):
    global x1,y1,x2,y2
    x1= event.x
    y1 = event.y
##마우스 클릭 해제 시 실행되는 함수
##클릭과 해제만 하니까 직선만 그려짐
def mouseDrop(event):
    global x1,y1,x2,y2, penWidth, penColor
    x2= event.x ##마우스를 떼는 순간 그림이 나옴
    y2=event.y ##x2,y2 를 이벤트가 발생한 좌표값으로 설정
    canvas.create_line(x1,y1,x2,y2,width = penWidth,fill=penColor) ##라인 그림

def getColor():  ##선 색을 바꾸는 함수
    global penColor
    color = askcolor() ##색상 선택하게 해주는 함수
    penColor = color[1] 

def getWidth():
    global penWidth ##askinteger에다가 창을 만드는 것임
    penWidth = askinteger("선 두께","선 두께(1~10)를 입력하세요",minvalue=1, maxvalue=10)

###########캔버스 지우기 코드####

def clearCanvas():
    canvas.delete("all")

###########곡선 그리기코드#######
    
def mouseMove(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1,y1, x1+1, y1+1, width=penWidth, fill = penColor)


def mouseMove2():
    #휠로 바꾸어서 부딪힘이 없도록!!
    canvas.bind("<B2-Motion>", mouseMove)


###########배경 변경 코드 ######
    
#배경 변경하기
def changeBg():
    color2=askcolor()
    bgColor = color2[1] 
    canvas.configure(background=bgColor)

############종료기능 코드#######

def func_exit():
    window.quit()
    window.destroy()
    
############도형 그리기 코드####
    
mode=0

def drawCircle(canvas,x2,y2):
    canvas.create_oval(x1, y1,x2, y2,
                        outline=penColor, width=penWidth)

def drawRectangle(canvas,x2,y2):
    canvas.create_rectangle(x1, y1,x2, y2,
                        outline=penColor, width=penWidth)

def drawC(event):
    x2=event.x
    y2=event.y
    drawCircle(canvas,x2,y2)
    
def drawR(event):
    x2=event.x
    y2=event.y
    drawRectangle(canvas,x2,y2)

def mouseLDown(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
   
    
# 마우스 왼쪽 버튼을 뗐을 때
def mouseLUp(event):
    global x1, y1
    if mode==1:
        drawC(event)
    else:
        drawR(event)

        
def circleButton():
    global mode
    mode=1
    canvas.bind("<Button-1>", mouseLDown)
    canvas.bind("<ButtonRelease-1>", mouseLUp)
   

def recButton():
    global mode
    mode=2
    canvas.bind("<Button-1>", mouseLDown)
    canvas.bind("<ButtonRelease-1>", mouseLUp)
    

def lineButton():
    canvas.bind("<Button-1>", mouseClick) ##마우스 감지
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    
###########텍스트 입력 코드##########
def textIn():
    value = askstring("내용", "내용을 입력하세요")
    value1 = askinteger("X좌표", "X좌표를 입력하세요")
    value2 = askinteger("Y좌표", "Y좌표를 입력하세요")
    canvas.create_text(value1,value2,text=value)

###########스탬프 코드###############
    
def myFunc1():
    global penWidth, penColor
    value1 = askinteger("X좌표", "X좌표를 입력하세요")
    value2 = askinteger("Y좌표", "Y좌표를 입력하세요")
    canvas.create_oval(value1, value2, 150, 250, width = penWidth, outline = penColor,fill=penColor)

def myFunc2():
    global penWidth, penColor
    value1 = askinteger("X좌표", "X좌표를 입력하세요")
    value2 = askinteger("Y좌표", "Y좌표를 입력하세요")
    canvas.create_rectangle(value1, value2, 300, 300, width = penWidth, outline = penColor,fill=penColor)
    
def myFunc3():
    global penWidth, penColor
    value1 = askinteger("X좌표", "X좌표를 입력하세요")
    value2 = askinteger("Y좌표", "Y좌표를 입력하세요")
    canvas.create_line(value1, value2, 200, 200, width = penWidth, fill=penColor)

#############메인####################
    
window = None
canvas = None ##그림을 그리는 영역
x1,y1,x2,y2 = None, None, None, None ##직선만 그림, 시작점과 종점을 설정
penColor = 'black' ##선의 기본색-검정
penWidth = 5 ##선의 기본 굵기 -5

if __name__ == "__main__":
    window = Tk()
    window.title("그림판 비슷한 프로그램")
    canvas = Canvas(window,height = 400 , width = 400)

    canvas.bind("<Button-1>", mouseClick) ##마우스 감지
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack() ##이벤트 패킹

    
##window 생성, 캔버스 추가
##선그리기(좌표 정보, 선그리는 함수create_line)
##메뉴 추가
##색상 선택
##두께 선택 => 단계적인 실행!!
############메뉴바 생성##############
menubar = Menu(window)
window.config(menu=menubar)

#파일 메뉴
fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "종료", command=func_exit)

#선 메뉴
editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "선", menu = editMenu)
editMenu.add_command(label = "선 색상 선택",command = getColor)
editMenu.add_separator()
editMenu.add_command(label="선 두께 설정",command=getWidth)
editMenu.add_separator()
editMenu.add_command(label="곡선그리기",command=mouseMove2)

#스탬프 메뉴
shapeMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "스탬프", menu = shapeMenu)
shapeMenu.add_command(label = "원",command= myFunc1)
shapeMenu.add_separator()
shapeMenu.add_command(label = "사각형" , command = myFunc2)
shapeMenu.add_separator()
shapeMenu.add_command(label = "직선",command = myFunc3)
#배경 메뉴
backgroundMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "배경", menu = backgroundMenu)
backgroundMenu.add_command(label = "배경 색깔 바꾸기", command=changeBg)
#지우기 메뉴
eraseMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "지우개", menu = eraseMenu)
eraseMenu.add_command(label = "모두지우기",command=clearCanvas)
#그림 메뉴
drawMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "그림", menu = drawMenu)
drawMenu.add_command(label = "원",command=circleButton)
drawMenu.add_separator()
drawMenu.add_command(label = "사각형" , command = recButton)
drawMenu.add_separator()
drawMenu.add_command(label = "선" , command = lineButton)
#텍스트 메뉴
textMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "텍스트", menu = textMenu)
textMenu.add_command(label = "텍스트 입력하기",command=textIn)

window.mainloop()
        
