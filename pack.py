print("팩맨 게임을 시작합니다")
print("유령이 나타났다!")
print(
    "1.도망간다 2.아이템쓴다 3.싸운다"
    )
number = int(input ("숫자를 입력하세요:"))

# 유저가 입력한 글자를 출력
#유저입력값 1=도망 
if number == 1:
    print("도망간다")
#유저입력값 2=아이템
if number == 2:
    print("아이템사용")
#유저입력값 3=싸운다
if number == 3:
    print("싸운다")

