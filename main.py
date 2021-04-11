import playTheGame
import alphaBeta

if __name__ == "__main__":

    gameOrAlgo = input("Would you like to play the game or run the algo?")

    if "game" in gameOrAlgo.lower():
        playTheGame()
    elif "algo" in gameOrAlgo.lower():
        print("andre is a bitch")

        # TODO get user inputs.
        #  PNT Player <#tokens> <#taken_tokens> <list_of_taken_tokens> <depth>
        #  this can be done either by asking the user or by taking in a file.
        #  can also just be hard coded... in format like [7,2,3,6,0]

        # TODO run the alphabeta algo
        #  in the alphabeta algo, the prints for the outputs will be done
    else:
        exit()
