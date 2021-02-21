import random

choices = ['Rock','Paper','Scissors']

# Stat Trackers

rock_choices = ("Rock","r","rock")
scissors_choices = ("scissors","Scissors","s","sc")
paper_choices = ("p","paper","Paper")

games_played_total = 0
games_won_total = 0
games_lost_total = 0
try:
  win_rate_total = round(games_won_total/(games_won_total+games_lost_total), 2)
except ZeroDivisionError:
  win_rate_total = 0

session_played = 0
session_won = 0
session_lost = 0

rock_played = 0
scissors_played = 0
paper_played = 0

win_streak = 0
loss_streak = 0
current_streak = 0

# user_choice = ""
# comp_choice = ""
# win_or_loss = ""
# winner = ""
# loser = ""

# win_messages = [f"{user_choice} > {comp_choice}. Point goes to you!"]

# loss_messages = [f"Computer outplayed you with {comp_choice}. Try again!"]

# draw_messages = [(f"{user_choice} negates {user_choice}. It's a draw!"), (f"You both played {user_choice}. Try again!"), (f"Computer also played {user_choice}. Draw!")]

# wl_messages = [ (f"Computer chose {comp_choice}. You {win_or_loss}!"), (f"{winner} beats {loser}. You {win_or_loss}!")]

def win_game():
  global current_streak, win_streak, loss_streak, session_played, session_won, session_lost, games_played_total, games_won_total
  session_played += 1
  session_won += 1

  games_won_total += 1
  games_played_total += 1
  
  if current_streak > 0:
    current_streak += 1
  else:
    current_streak = 1
  
  # Updating longest win streak - checks if the current streak is bigger than the longest win streak
  if current_streak > win_streak:
    win_streak = current_streak

def lose_game():
  global current_streak, win_streak, loss_streak, session_played, session_won, session_lost, games_played_total, games_lost_total
  session_played += 1
  session_lost += 1

  games_lost_total += 1
  games_played_total += 1

  if current_streak < 0:
    current_streak -= 1
  else:
    current_streak = -1
  
  if current_streak < loss_streak:
    loss_streak = current_streak

play = True

while play is True:
  current_session_games = 0
  current_session_won = 0
  command = input()
  comp_choice = random.choice(choices)
  # seqs_wins = [win_messages, wl_messages]

  if command in ("x","quit","exit"):
    break

  elif command in ("h","help"):
      print("\n*************************************************************\nThe computer will randomly select rock/paper/scissors to play against you. \nYou play your hand by typing in rock/paper/scissors (or r/p/s for short), then the terminal will return a line saying whether you won or not.\n\n'r'/'p'/'s'    | to play the game\n'stats'        | to see overall stats\n'save'         | to save into your existing save file, or create a new one if it doesn't exist yet.\n'quit' or 'x'  | to exit.\n*************************************************************\n") 


  elif command in rock_choices or command in paper_choices or command in scissors_choices:
    if command in (rock_choices):
      user_choice = "Rock"
      rock_played += 1

    elif command in (scissors_choices):
      user_choice = "Scissors"
      scissors_played += 1
    elif command in (paper_choices):
      user_choice = "Paper"
      paper_played += 1
    
    if user_choice == comp_choice:
      print(f"Computer chose {comp_choice}. Draw!")
      games_played_total += 1
      session_played += 1
    elif user_choice == "Rock" and comp_choice == "Scissors":
      win_game()
      print(f"Computer chose {comp_choice}. You win!")
    elif user_choice == "Scissors" and comp_choice == "Paper":
      win_game()
      print(f"Computer chose {comp_choice}. You win!")
    elif user_choice == "Paper" and comp_choice == "Rock":
      win_game()
      print(f"Computer chose {comp_choice}. You win!")
    else:
      lose_game()
      print(f"Computer chose {comp_choice}. You lose!")
    
    # winner = "Rock"
    # loser = "Scissors"
    # win_or_loss = "win"
    # # print(random.choice(random.choices(seqs_wins, weights=map(len, seqs_wins))[0]))
    # print(random.choice(wl_messages))

  # SAVE FILE
  elif command == "save":
    f = open("rpssave.txt","w")

    f.write(f"{games_played_total}/{games_won_total}/{games_lost_total}/{rock_played}/{scissors_played}/{paper_played}/{current_streak}/{win_streak}/{loss_streak}")
    f.close()

  elif command == "load":
    g = open("rpssave.txt", "r")
    gamedata = g.read()

    unpackeddata = []
    unpackeddata = gamedata.split("/")

    games_played_total = unpackeddata[0]
    games_won_total = unpackeddata[1]
    games_lost_total = unpackeddata[2]

    g.close()


  elif command in ("stat","stats"):
    try:
      win_rate_total = round(int(games_won_total)/(int(games_won_total)+int(games_lost_total))*100, 2)
    except ZeroDivisionError:
      win_rate_total = 0
    print(
      f"Total games played = {games_played_total}\n" +
      f"Total games won = {games_won_total}\n" +
      f"Total games lost = {games_lost_total}\n" + 
      f"Total win rate = {win_rate_total}%\n\n" +
      f"Rock played = {rock_played}\n" +
      f"Scissors played = {scissors_played}\n" +
      f"Paper played = {scissors_played}\n\n" +
      f"Current streak = {current_streak}\n" + 
      f"Longest win streak = {win_streak}\n" +
      f"Longest loss streak = {loss_streak}"
    )

  else:
    print("Try again. Type 'help' for commands.")



