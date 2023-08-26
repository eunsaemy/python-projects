import random
import hangman_art, hangman_words


def main():
    chosen_word = random.choice(hangman_words.word_list)
    display = []
    end_of_game = False
    lives = 6

    for letter in chosen_word:
        display.append("_")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = chosen_word[i]
        else:
            lives -= 1

        print(hangman_art.stages[lives])
        print(" ".join(display), end="\n\n")

        if "_" not in display:
            end_of_game = True
            print("You win!")

        if lives == 0:
            end_of_game = True
            print("You lose.")


if __name__ == "__main__":
    main()
