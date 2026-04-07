'''from Function import addiction
print(addiction(2,5))
# for loop
'''

scores = []

for x in range(2):
    student_number = input("SN: ")
    score = float(input("Score: "))
    final_score = [student_number, score]
    scores.append(final_score)

print("scores", len(scores))

for n in scores:
        student_number = n[0]
        score = n[1]
        print ("SN", student_number, "got", score, "of score")

