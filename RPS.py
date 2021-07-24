class Game:
    print("Enter Abhinav's input: ")
    abhinav_input = input()
    print("Enter Anjali's input: ")
    anjali_input = input()
    expected_input = ["Rock", "Paper", "Scissors"]
    if not abhinav_input in expected_input:
        print("Invalid input for Abhinav: "+str(abhinav_input))
    if not anjali_input in expected_input:
        print("Invalid input for Anjali: "+str(anjali_input))

    if anjali_input == abhinav_input:
        print("Tie")
    elif abhinav_input == expected_input[0]:
        if anjali_input == expected_input[1]:
            print("Anjali Wins")
        elif anjali_input == expected_input[2]:
            print("Abhinav Wins")
    elif abhinav_input == expected_input[1]:
        if anjali_input == expected_input[2]:
            print("Anjali Wins")
        elif anjali_input == expected_input[0]:
            print("Abhinav Wins")
    elif abhinav_input == expected_input[2]:
        if anjali_input == expected_input[0]:
            print("Anjali Wins")
        elif anjali_input == expected_input[1]:
            print("Abhinav Wins")