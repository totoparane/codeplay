'''
리스트 = 변수 하나의 공간에 여러 데이터를 넣는 방법
for i range(for 반복문)
while(조건 반복문)
'''

kor = ["사과", "포도", "딸기", "바나나", "토마토", "수박"]
eng = ["apple", "grape", "strawberry", "banana", "tomato", "watermelon"]
score = 0
answer = ""


# 횟수 반복문

for i in range(len(kor)):
    answer = input(f"{kor[i]} 을/를 영어로 하면? : ")
    if answer == eng[i]:
        score = score + 1
        print("정답. 현수같지 않군")
    else:
        print("qttR")
print(f"당신의 점수는 {score}점 입니다")



# running = True
# count = 0


# while running:
#     answer = input(f"{kor[count]} 을/를 영어로 하면? : ")
#     if answer == eng[count]:
#         score += 1
#         print("정답. 현수같지 않군")
#     else:
#         print("qttR")
#     count += 1
#     if count >= len(kor):
#         running = False
# print(f"당신의 점수는 {score}점 입니다")