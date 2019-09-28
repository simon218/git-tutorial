import random

ranNum = random.sample(range(1,100), 1)
print("난수 :", ranNum)

testNum= ranNum[0]

print(" 당신의 기억력을 테스트합니다.")
print("준비되셨습니까?")
print("1.yes / 2. no")

inputNum = int(input())
type(inputNum)

if inputNum == 1:
    for i in range(20):
        print()

    print("난수는?")
    myNum = int(input())

    if myNum == testNum:
            print("빙고~ 훌륭합니다.")
    else:
            print("아쉽습니다.")

else:
    print("게임을 종료합니다.")
