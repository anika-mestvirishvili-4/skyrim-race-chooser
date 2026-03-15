from survey import user_interference
from scoring import rank_results
from statistics import statistics

def display():

    print("\n| ---------------------------------- |")
    print("|  Welcome to Skyrim Race Chooser!   |")
    print("| ---------------------------------- |\n")

def main():
    display()
    chosen_skills = user_interference()

    results = rank_results(chosen_skills)

    print("The top results are:")
    for race, _ in results[:3]:    #So _ is used when we intentionally disregard a value
        print(race)
       

    statistics(chosen_skills)

if __name__ == "__main__":
    main()