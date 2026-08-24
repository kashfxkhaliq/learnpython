import json

FILE_NAME = "votes.json"

def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Save data to JSON
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def show_candidates(data):
    print("\nCandidates")
    for i in data["candidates"]:
        print("ID:", i["id"])
        print("Name:", i["name"])

def cast_votes(data):

    print(".....Voting System.....")

    show_candidates(data)

    vote_id = int(input("Enter the Candidate ID :: "))

    for i in data["candidates"]: # check the candidates
        if i["id"] == vote_id: # matched ID
            i["votes"] += 1 # Votes add 1
            data["total_votes"] += 1 # total_votes add 1 
            print("\nVote Cast Successfully")
            return

    print("\nInvalid Candidate ID")

def voting_result(data):

    print("\n....Voting Result....")

    for i in data["candidates"]:
        print("ID:", i["id"], "Name:", i["name"], "Votes:", i["votes"])
      
    print("Total Votes:", data["total_votes"])


def winner_candidate(data):
    
    winner = data["candidates"][0]  # first candidate as winner

    for i in data["candidates"]:
        if i["votes"] > winner["votes"]:
            winner = i # 

    print("\n....Winning Candidate....")
    print("ID:", winner["id"], "Name:", winner["name"])
    print("Votes:", winner["votes"])


def main():

    data = load_data()

    while True:
        print("\n....MENU....\n")
        print("1.Cast Votes\n2.View Results\n3.Winning Candidate\n4.Save Data\n5.Exit\n")

        choice = int(input("Enter The Choice :: "))

        if choice == 1:
            cast_votes(data)

        elif choice == 2:
            voting_result(data)

        elif choice == 3:
            winner_candidate(data)

        elif choice == 4:
            save_data(data)
            print("Data Saved in JSON File")

        elif choice == 5:
            exit()

        else:
            print("Invalid Choice")

    # Run program
if __name__ == "__main__":
    main()
            