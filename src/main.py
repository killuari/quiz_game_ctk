from name import Name
from score import Score
from lives import Lives
from player import Player

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

    # Class Player
    print("\nClass Player")
    player = Player("Peter")
    print(f"Name: {player.name()}")
    print(f"Amount of Lives: {player.lives().get()}")
    print(f"Current Score of {player.name()}: {player.score().get()}")
    player.score().add(5)
    print(f"Current Score of {player.name()}: {player.score().get()}")
    player.reset()
    print(f"Current Score of {player.name()}: {player.score().get()}")

if __name__ == "__main__":
    main()
