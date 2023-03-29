#문자열 포맷팅 - (f"{변수}글씨")
#문자열 인덱싱 - (변수[꺼내올 숫자])
#문자열 슬라이싱 -


name = ""
gender = ""
age = 0





# print(name, len(name), age - 10)

name = input("이름을 입력하세요 : ")
gender = input("성별을 입력하세요 (남/여 둘 중 하나만 골라) : ")
age = input("나이를 입력하세요 : ")

# print(name + "님 반갑습니다. 지옥에 오신것을 환영합니다!")
if gender == "남":
    gender = "Mr."
elif gender == "여":
    gender = "Ms."

print(f"Welcome {gender}{name[0]}!. This is fantastic hell.")
if int(age) <= 18:
    print("당신은 미성년자시군요. 미성년자 지옥으로 가세요")
elif int(age) >= 19:
    print("당신은 성인이군요 성인용 지옥으로 가세요")