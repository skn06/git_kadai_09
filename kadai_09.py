import random

# 100から999の範囲でランダムな数字を生成
correct_number = random.randint(100, 999)

print("Guess the number between 100 and 999. You can answer 10 times.")

times = 0
max_times = 10

while times < max_times:
    # ユーザーのキーボード入力を受け取る
    input_number = input("Enter your guess: ")

    # 回答回数をカウントする
    times += 1

    # 正解かどうかを判定
    if input_number < correct_number:
        print("Too low! Try again.")
    elif input_number > correct_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! Your number is correct.")
