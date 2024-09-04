import random

def rock_paper_scissors(user):
    if user == "그만":
        return None
    computer = random.choice(["가위", "바위", "보", "도마뱀", "스포크"])
    if user == computer:
        return "무승부"
    elif (user == "가위" and (computer == "보" or computer == "도마뱀")) or \
         (user == "바위" and (computer == "가위" or computer == "도마뱀")) or \
         (user == "보" and (computer == "바위" or computer == "스포크")) or \
         (user == "도마뱀" and (computer == "보" or computer == "스포크")) or \
         (user == "스포크" and (computer == "가위" or computer == "바위")):
        return "승리"
    else:
        return "패배"

def test_rock_paper_scissors():
    # Test case 1: User wins
    random.seed(1)
    assert rock_paper_scissors("가위") == "패배"
    assert rock_paper_scissors("바위") == "무승부"
    assert rock_paper_scissors("보") == "승리"
    assert rock_paper_scissors("도마뱀") == "패배"
    assert rock_paper_scissors("스포크") == "승리"

    # Test case 2: User loses
    random.seed(2)
    assert rock_paper_scissors("가위") == "승리"
    assert rock_paper_scissors("바위") == "패배"
    assert rock_paper_scissors("보") == "무승부"
    assert rock_paper_scissors("도마뱀") == "승리"
    assert rock_paper_scissors("스포크") == "패배"

    # Test case 3: Draw
    random.seed(3)
    assert rock_paper_scissors("가위") == "무승부"
    assert rock_paper_scissors("바위") == "무승부"
    assert rock_paper_scissors("보") == "무승부"
    assert rock_paper_scissors("도마뱀") == "무승부"
    assert rock_paper_scissors("스포크") == "무승부"

    # Test case 4: User quits
    random.seed(4)
    assert rock_paper_scissors("그만") == None

test_rock_paper_scissors()