import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요.
lives = 6
# todo - 2 : hangman03을 참조하여 while 반복문 바깥을 완성하시오.
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display.append('_')
# todo - 3 : while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 작성하시오.
end_of_game = False

print(chosen_word)

while not end_of_game:
    guess = input('알파벳 입력 >>> ').lower()
    # if lives == 0 or ''.join(display) == chosen_word:
    #     end_of_game = True
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    # 틀렸을 때 lives를 1씩 감하고 0이 되었을 때 game over 시키는 부분
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
        print(display)
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if'_' not in display:
        print('정답입니다.')
        end_of_game = True  # 이 시점에 end_of_game이 True 가 되었으므로 다음 반복 문이 실행되지 않음 -> 112번 코드 라인이 실행된다는 것을 의미합니다.
        break  # 바로 반복문 정지 -> 105번 코드라인이 실행 x
        print(f'정답은 {chosen_word}입니다.')

    # 현재 상황이 콘솔창에 출력돼서 user에게 안내가 가면 좋겠네요.
    print(''.join(display))


# todo - 4 : lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때마다 올바른 stages의 element가 출력될 수 있도록 작성하시오.
print('')

# 현재 기준에서 아까 완성판과 차이점 : loge유무 /  word_list가 부족함 / 혹시나 리팩토링이 가능한지 여부
# hangman05 파일 생성 -> 필요한 부분들 다 복사하고 주석들 좀 다 지워서 정리해놓겠습니다.
# logo를 text to ascii arts를 검색해서 하나 받아와서 맨 처음에 로고를 출력할 수 있도록 코드를 작성하겠습니다.
