#문자열 인덱싱 - (변수[꺼내올 숫자])
#문자열 포맷팅 - (f"{변수}글씨")
#문자열 슬라이싱 - [시작:끝:방향 및 건너뛰기]
#. 문자열 인덱싱 : 글자 중 특정위치의 것 하나를 꺼내거나 사용
#. 문자열 포맷팅 : 변수와 상수를 한꺼번에
#. 데이터 입력 : input()
# type()하고 ()안에 넣으면 종류 알려줌
# % 나머지만 보여준다
#//뒤에 있는 소수 무시









# eng = "abcdefg"
# kor = "가나다라마바사"

# print(eng[3])
# print(f"{kor[-1:-3:-1]}! 이자식아!") #문자열 슬라이싱 + 포맷팅

# print(eng[::-1]) #0번째 부터 7번째 직전인 6번째까지 가져와라





# name = ""
# gender = ""
# age = 0

# print(name, len(name), age - 10)

# name = input("이름을 입력하세요 : ")
# ender = input("성별을 입력하세요 (남/여 둘 중 하나만 골라) : ")
# age = input("나이를 입력하세요 : ")

# print(name + "님 반갑습니다. 지옥에 오신것을 환영합니다!")
# if gender == "남":
#     gender = "Mr."
# elif gender == "여":
#     gender = "Ms."

# print(f"Welcome {gender}{name[0]}!. This is fantastic hell.")
# if int(age) <= 18:
#     print("당신은 미성년자시군요. 미성년자 지옥으로 가세요")
# elif int(age) >= 19:
#     print("당신은 성인이군요 성인용 지옥으로 가세요")





# name = ""
# age = 0

# name = input("이름은? : ")
# age = input("나이는? : ")

# if int(age) < 16:
#     print(f"{name[1:]} 너 임마 까불지마. ")    #슬라이싱

# elif int(age) > 16:
#     print(f"{name[0]}사장님 너무 멋지시다~ 굽신굽신~ . ")    #인덱싱





# import random

# name = "못생긴손현수" #문자열
# call = ["바보", "천재", "미남", "추남", "또라이"] #리스트

# print(f"역시! {name[3:]} {call[random.randint(0, 4)]}!")





a = "코딩쌤"
b = 30
c = True
d = 25.5
e = ["불친절", "못생김", "현수 같은", "안멋짐"]

print(a, type(a), b, type(b), c, type(c), d, type(d), e, type(e))
print(b + d)
print(1+1, 10-1, 2*2, 3/2, 4/2, 3//2, 4//2, 3%2)