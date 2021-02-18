'''
    Question: [3] Digit Hangman
    Author: Passawit Riewthong
'''


class QuestDigit:
    # Class of Digit with value and correction flag
    def __init__(self, value):
        self.value = value
        self.isCorrect = False


quest = input().split(' ')  # Get question input
quest = list(map(QuestDigit, quest))  # Map question digit
wrongAns = []
print('_ _ _ _ _ _ _ _ _ _ _ _')

# Start game
for _ in range(5):
    ans = input()  # Get answer
    isCorrect = False  # Declare correction flag
    for digit in quest:
        # Check answer for each question digits
        if not digit.isCorrect:
            print(digit.value if digit.value ==
                  ans else '_', end=' ')  # Print answer
            if digit.value == ans:
                # Set isCorrect
                isCorrect = True
                digit.isCorrect = True
        else:
            print(digit.value, end=' ')  # Print previous correct answer

    if not isCorrect:
        wrongAns.append(ans)  # Append worng answer

    # Print worng answer
    for digit in wrongAns:
        print(digit, end=' ')
    print()

# Sum total score
score = sum(digit.isCorrect for digit in quest)
print(score)
