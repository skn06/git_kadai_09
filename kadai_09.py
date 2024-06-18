import random

# 100から999の範囲でランダムな数字を生成
correct_number = random.randint(100, 999)

print("Guess the number between 100 and 999. You can answer 10 times.")

times = 0
max_times = 10

while times < max_times:
    # ユーザーのキーボード入力を受け取る
    input_number = input("Enter your guess: ")

    #input_numberを整数に変換する
    user_number = int(input_number)

    # 回答回数をカウントする
    times += 1

    # 正解かどうかを判定する
    if user_number < (correct_number - 100 ):
        print("Too low! Try again.")
    elif user_number < correct_number:
        print("A little Low! Try again.")
    elif user_number > (correct_number + 100):
        print("Too high! Try again.")
    elif user_number > correct_number:
        print("A little High! Try again.")
    elif user_number > (correct_number - 5) and user_number < (correct_number + 5):
        print("Close! Tri again.")
    else:
        print("Congratulations! Your number is correct.")

    # 残りの回答回数を表示する
    print(f"You have {max_times - times} times to guess.")