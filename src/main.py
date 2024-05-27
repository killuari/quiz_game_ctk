from name import Name
from score import Score

def main():
    print("Hello, Quiz King!")

    # Class Name
    name = Name("Hans")
    print(name)

    # Class Score
    score = Score()
    score.add(3)
    print(score.get())
    score.add(2)
    print(score.get())
    score.reset()
    print(score.get())

if __name__ == "__main__":
    main()
