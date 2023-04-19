
# ja = ""
# n1 = 0
# n2 = 0
# result = 0

# while True:
#     ja = input("무슨계산 할래? 기호로만 적어 (+, -, *, /)")
#     n1 = int(input("첫번째 숫자를 말해라"))
#     n2 = int(input("두번째 숫자를 말해라"))
#     if ja == "+":
#         result = n1 + n2
#     elif ja == "-":
#         result = n1 - n2
#     elif ja == "*":
#         result = n1 * n2
#     elif ja == "/":
#         result = n1 / n2
#     else:
#         print("다시 다시! 다시!!!!! 다시 해!")
#         continue
#     print(f"{n1} {ja} {n2} = {result}")

#똑계

gyesan = ""
result = 0
running = True
show = True

while running:
    show = True
    gyesan = input("계산기입니다. 물어보세요 : ")
    if "+" in gyesan:
        result = int(gyesan.split("+")[0])  + int(gyesan.split("+")[1])
    elif "-" in gyesan:
        result = int(gyesan.split("-")[0])  - int(gyesan.split("-")[1])
    elif "*" in gyesan:
        result = int(gyesan.split("*")[0])  * int(gyesan.split("*")[1])
    elif "/" in gyesan:
        result = int(gyesan.split("/")[0])  / int(gyesan.split("/")[1])
    elif "q" in gyesan:
        print("잘가라 주인놈 ㅋㅋㅋㅋ")
        running = False
        show = False
    else:
        print("연산식 이상 다시해")  
        show = False
        continue  
    if show:
        print(f"{gyesan} = {result}")
