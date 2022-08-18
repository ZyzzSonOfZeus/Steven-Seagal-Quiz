print("Welcome to Master-Sifu Steven Seagals Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what martial art does Steven practice/teach? ")
if answer.lower() == "aikido":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is Steven's favourite food? ")
if answer.lower() == "hot wings":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What brand is Steven Seagal's orange tinted glasses? ")
if answer.lower() == "oakley":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What type of hairline does Steven have? ")
if answer.lower() == "receding":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many wives has Steven gone through? ")
if answer.lower() == "four":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")