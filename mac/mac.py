import pyautogui
# print(pyautogui.position()) #좌표확인
from time import sleep
from cv2 import cv2
import pyperclip


##################################readme.txt#####################################################
# pyautogui.moveTo() #이동
# pyautogui.moveRel() #평행이동 

# pyautogui.click()Hello world!
# pyautogui.doubleClick

# variable = pyautogui.locateCenterOnScreen('path') #이미지에 좌표 찍기 
# pyautogui.write('Hello world!') #메세지 적기Hello world! -> 이거 안씀 키입력방식이라 별로임

# 첫번째는 플로우대로 쭉 만들어보기
# 두번쨰는 묶을 수 있을것 같은 기능 모아보기
# 세번째는 모듈화시켜서 재사용하기
# 


# 코드에 필터가 아무거라도 무조건 있어야됌 T자모양 아이콘이 활성화된 상태여야함
# 렉걸리면 답이없네? -> 데이터 불러오는 단계에서는 최소 3초이상 딜레이 걸어주자
#
#
#
#
#
#
#
#
# ####################함수###################################################

def selectFilter():
    # 필터 누르기
    tableI= cv2.imread(r'mac\IMAGE\table.png')
    tableI2= cv2.imread(r'mac\IMAGE\table1.png')
    tableI3= cv2.imread(r'mac\IMAGE\table2.png')
    table1 = pyautogui.locateCenterOnScreen(tableI)
    table2 = pyautogui.locateCenterOnScreen(tableI2)
    table3 = pyautogui.locateCenterOnScreen(tableI3)
    if table1 != None:
        print(table1)
        pyautogui.moveTo(table1)
        pyautogui.click()
        sleep(1)

    elif table2 != None:
        print(table2)
        pyautogui.moveTo(table2)
        pyautogui.click()
        sleep(1)
    elif table3 != None:
        print(table3)
        pyautogui.moveTo(table3)
        pyautogui.click()
        sleep(1)

def textClear():
    # 텍스트 초기화
    queryI = cv2.imread(r'mac\IMAGE\queryI.png')
    queryI = pyautogui.locateCenterOnScreen(queryI)
    pyautogui.moveTo(queryI)
    pyautogui.moveRel(0,100)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a') 
    pyautogui.hotkey('del') 

def writeContext():
    # 로그 출력
    print(f'''"출동안전센터 지역대" = '{i}119안전센터' AND 
    "신고년월일 (년)" = {j}   
    {n}'''+'가 복사되었습니다.')

    #복사 & 붙여넣기 & 확인
    pyperclip.copy(
    f'''"출동안전센터 지역대" = '{i}119안전센터' AND 
    "신고년월일 (년)" = {j}  
    {n}''')
    sleep(1)
    pyautogui.hotkey('ctrl','v')
    queryI2 = cv2.imread(r'mac\IMAGE\queryI2.png')
    queryI2 = pyautogui.locateCenterOnScreen(queryI2)
    # print(queryI2)
    pyautogui.moveTo(queryI2)
    pyautogui.moveRel(-90,0)
    pyautogui.click()

def makeShape():
            sleep(1)
            # 최소 경계 도형 선택
            toolBox1= cv2.imread(r'mac\IMAGE\toolbox.png')
            toolBox2= cv2.imread(r'mac\IMAGE\toolbox2.png')
            toolBox3= cv2.imread(r'mac\IMAGE\toolbox3.png')
            toolboxA= pyautogui.locateCenterOnScreen(toolBox1)
            toolboxB= pyautogui.locateCenterOnScreen(toolBox2)
            toolboxC= pyautogui.locateCenterOnScreen(toolBox3)
            if toolboxA != None:
                # print(toolboxA)
                pyautogui.moveTo(toolboxA)
                pyautogui.click()
                sleep(1)

            elif toolboxB != None:
                # print(toolboxB)
                pyautogui.moveTo(toolboxB)
                pyautogui.click()
                sleep(1)

            else:
                # print(toolboxC)
                pyautogui.moveTo(toolboxC)
                pyautogui.click()
                sleep(1)
            pyautogui.doubleClick()
            sleep(2)
            #도형유형 선택
            shapeType = cv2.imread(r'mac\IMAGE\stype.png')
            shapeTypeA= pyautogui.locateCenterOnScreen(shapeType)
            pyautogui.moveTo(shapeTypeA)
            pyautogui.moveRel(0,20)
            pyautogui.click()
            sleep(0.2)
            pyautogui.moveRel(0,60,0.1)
            pyautogui.click()
            sleep(0.5)

            #### 실행하기 인식이 안됌? 이상함 그래서 걍 상대값 찾아서 넣음 ??? 이거 진짜 왜 안돌아가지??
            #### practice = cv2.imread(r'mac\IMAGE\prac.png')
            #### practiceA= pyautogui.locateCenterOnScreen(practice)
            #### pyautogui.moveTo(practiceA)

            # 실행하기 상대값 좌표 (창크기가 바뀌면 절대 안됌 사이즈를 알아서 맞춰주어야함)
            pyautogui.moveRel(600,355)
            pyautogui.click()
            sleep(2)
            pyautogui.hotkey('esc')

def exportFile(a):
    #레이어 기준점
    layer= cv2.imread(r'mac\IMAGE\ex1.png')
    layer1 = pyautogui.locateCenterOnScreen(layer)
    pyautogui.moveTo(layer1)

    #내보내기(단축키가 없어서 이런 노가다가 없네 ㅡㅡ) 이부분 함수로 다시 만드는거 가능할듯 
    fileName = ['5분','7분','10분']

    pyautogui.moveRel(0,25) #도형1
    pyautogui.rightClick()
    pyautogui.moveRel(50,360,0.2)
    sleep(0.2)
    pyautogui.moveRel(300,0,0.2)
    pyautogui.click()
#원래코드는 무빙에 문제가 있어서 보류
    # if fileName[a] == '5분':
    #     pyautogui.moveRel(0,25) #도형1
    #     pyautogui.rightClick()
    #     pyautogui.moveRel(50,360,0.2)
    #     sleep(0.2)
    #     pyautogui.moveRel(300,0,0.2)
    #     pyautogui.click()
        

    # elif fileName[a] == '7분':
    #     pyautogui.moveRel(0,40) #도형2
    #     pyautogui.rightClick()
    #     pyautogui.moveRel(50,380,0.2)
    #     sleep(0.2)
    #     pyautogui.moveRel(300,0,0.2)
    #     pyautogui.click()
    # else:
    #     pyautogui.moveRel(0,60) #도형3
    #     pyautogui.rightClick()
    #     pyautogui.moveRel(50,380,0.2)
    #     sleep(0.2)
    #     pyautogui.moveRel(300,0,0.2)
    #     pyautogui.click()

    pyperclip.copy(
    f'{i}_{j}_'+fileName[a])
    sleep(1)
    pyautogui.hotkey('ctrl','v')
    check= cv2.imread(r'mac\IMAGE\check.png')
    checkI = pyautogui.locateCenterOnScreen(check)
    pyautogui.moveTo(checkI)
    pyautogui.click()
    sleep(0.5)
    pyautogui.hotkey('enter')


def deleteLayer():
    # 도형 지우기
    layer= cv2.imread(r'mac\IMAGE\ex1.png')
    layer1 = pyautogui.locateCenterOnScreen(layer)
    pyautogui.moveTo(layer1)
    pyautogui.moveRel(0,25) #도형1
    pyautogui.click()
    # pyautogui.keyDown('shift')
    # pyautogui.moveRel(0,35) #도형3
    # pyautogui.click()
    # pyautogui.keyUp('shift')
    pyautogui.rightClick()
    remove= cv2.imread(r'mac\IMAGE\remove.png')
    removeI = pyautogui.locateCenterOnScreen(remove)
    pyautogui.moveTo(removeI)
    pyautogui.click()
    pyautogui.press('enter')
    print('레이어가 삭제 되었습니다.')

def useFilter():
    selectFilter()
    textClear()
    writeContext()


# #######################사용코드####################################
fire = ['가야','감만','감전','강동','광안','괴정','구포','금곡','기장','기장','남산','녹산','다대','당감','대연','대저','동삼','만덕','망미','모라','반송','반여','범일','부곡','부두','부민',
'부암','부전','사직','산성','산성산악','삼락','서동','센텀','송도','송정','수안','수정','신평','신호','양정','연산','영선','온천','용당','우동','일광','장안','정관','좌동','주례',
'중동','중앙','지사','창선','청학','초량','충무','하단','학장','화명']
                                                         
year = [2017,2018,2019]
min = ['AND "5분" = 1','AND "10분" != 1','']

# print(len(min))

for i in fire:
    for j in year:
        for n in min:
            sleep(1)
            useFilter()
            makeShape()
            exportFile(min.index(n))

            #없어도 되는 로그 
            fileName1 = ['5분','7분','10분']
            print(f'{i}_{j}_'+fileName1[min.index(n)]+'을 내보냈습니다.')

            deleteLayer()


