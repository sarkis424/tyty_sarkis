import random
secret_number = random.randint(0, 100)
attempts = 0

print("Я загадал число от 0 до 100. Попробуй угадать!")
while True:
  user_input = input("Введите число: ")

  if not user_input.isdigit():
    print("Пожалуйста, введите целое число.")
    continue

  guess = int(user_input)
  attempts += 1


  if guess < secret_number:
    print("Больше!")
  elif guess > secret_number:
    print("Меньше")
  else:
    print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
    break