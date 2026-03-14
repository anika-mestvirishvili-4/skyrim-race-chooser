from survey import get_user_answer, user_interference
import json

with open("races.json") as f:
    races = json.load(f)

with open("survey.json") as f1:
    survey = json.load(f1)


def display():

    print("\n| -------------------------------------- |")
    print("|  Welcome to the Skyrim Race Chooser!   |")
    print("| -------------------------------------- |\n")



def evaluate_races(races, chosen_skills):

    scores = {}
    for race in races:
        scores[race] = 0

    for skill in chosen_skills:
        for race, race_skill_value in races.items():

            skill_value = race_skill_value.get(skill, 15)

            if skill_value == 25:
                scores[race] += 2
            elif skill_value == 20:
                scores[race] += 1
            else: 
                scores[race] += 0
    return scores

def rank_results(chosen_skills):
    scores = evaluate_races(races, chosen_skills)
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_scores

def statistics(chosen_skills):
    user_answer = input("Would you like to learn more about the result statistics? (y/n)")

    if  user_answer == "y":
        
        for race, score in rank_results(chosen_skills):
            percent = round((score / 7) * 100) 
            print(f"{race}: {score}/7 ({percent}%)")


    elif user_answer == "n":
        pass
    else:
        print("Input is invalid. (y/n)")
        statistics(chosen_skills)

def results():
    chosen_skills = user_interference()

    print("The top results are:")

    for race, score in rank_results(chosen_skills)[:3]:
        print(race, f"(Score: {score})")
    statistics(chosen_skills)




results()