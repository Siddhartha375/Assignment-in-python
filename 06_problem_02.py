def game():
    return 1
score=game()

with open("highscore.txt") as f:
    highscore=f.read()
if highscore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))
    if highscore<score:
        with open('highscore.txt','w') as f:
            f.write(str(score))
