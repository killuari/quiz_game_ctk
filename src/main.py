from name import Name
from score import Score
from lives import Lives

def main():
    print("Hello, Quiz King!")

    # Class Name
    print("\nClass Name")
    name = Name("Hans")
    print(name)

    # Class Score
    print("\nClass Score")
    score = Score()
    score.add(3)
    print(score.get())
    score.add(2)
    print(score.get())
    score.reset()
    print(score.get())

    # Class Lives
    print("\nClass Lives")
    lives = Lives()
    lives.loose_a_life()
    print(lives.get())
    for i in range(5):
        lives.loose_a_life()
    print(lives.get())
    print(lives.is_game_over())


if __name__ == "__main__":
    main()
