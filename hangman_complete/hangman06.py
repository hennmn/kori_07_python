import random
import hangman_arts     # 이게 파일명이라는 사실에 주목
import hangman_word_list    # 해야겠네요
# 즉 logo / stages와 같은 변수는 아닙니다.

# 외부의 hangman_word_list에 있는 word_list를 참조해서 저희는 chosen_word를 만들 필요가 있습니다.
chosen_word = random.choice(hangman_word_list.word_list)
print(chosen_word)

logo = hangman_arts.logo

lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)

end_of_game = False
print(logo)
while not end_of_game:
    print(hangman_arts.stages[lives])
    guess = input('알파벳 입력 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
        print(display)
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(hangman_arts.stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if'_' not in display:
        print('정답입니다.')
        end_of_game = True
        print(f'정답은 {chosen_word}입니다.')

    print(''.join(display))