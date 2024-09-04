# 가위 바위 보 게임 작성해줘
# 1. 사용자에게 가위, 바위, 보 중 하나를 입력받아요
# 2. 컴퓨터는 랜덤하게 가위, 바위, 보 중 하나를 선택해요
# 3. 사용자와 컴퓨터의 선택을 비교해서 누가 이겼는지 출력해요
# 4. 사용자가 이기면 "승리", 비기면 "무승부", 지면 "패배"를 출력해요
# 5. 사용자가 "그만"을 입력할 때까지 게임을 반복해요
# 6. 게임이 끝나면 전적을 출력해요
# 위의 기능 순서대로 파이썬 코드를 작성해줘

from rcp import rock_paper_scissors

win = 0
draw = 0
lose = 0

while True:
    user = input("가위, 바위, 보, 도마뱀, 스포크 중 하나를 입력하세요: ")
    if user == "그만":
        break
    result = rock_paper_scissors(user)
    if result == "무승부":
        print("무승부")
        draw += 1
    elif result == "승리":
        print("승리")
        win += 1
    else:
        print("패배")
        lose += 1

print(f"전적: {win}승 {draw}무 {lose}패")
