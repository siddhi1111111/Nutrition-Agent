score = 0

q1 = input("What is the capital of India? (a) Mumbai (b) Delhi: ")
if q1.lower() == "b": score += 1

q2 = input("What is the Earth's natural satellite? (a) Moon (b) Sun: ")
if q2.lower() == "a": score += 1

q3 = input("Who is known as the father of computers? (a) Charles Babbage (b) Newton: ")
if q3.lower() == "a": score += 1

print("Your score:", score, "/ 3")
