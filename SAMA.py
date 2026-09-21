print("===== SAMA or =====")
print("~Student Academic & Marks Analyzer~")
#Input
name=input("Enter student name: ")
num_of_subjects=int(input("Enter number of subjects: "))
max_marks=int(input("Enter Maximum marks for the exam:"))
subjects=[]
marks=[]
#Process
for i in range(num_of_subjects):
    subject = input("Enter subject name: ")
    mark = float(input("Enter marks for subject: "))

    subjects.append(subject)
    marks.append(mark)

total = sum(marks)
avg= total/num_of_subjects
percentage=(avg/max_marks)*100
highest_mark = max(marks)
lowest_mark = min(marks)

most_scoring_subject = ""
lowest_scoring_subject = ""

for i in range(num_of_subjects):
    if marks[i] == highest_mark:
        most_scoring_subject = subjects[i]

    if marks[i] == lowest_mark:
        lowest_scoring_subject = subjects[i]

print("~===== ACADEMIC REPORT =====~")
print("Student:",name)

for i in range(num_of_subjects):
    print(subjects[i], ":", marks[i])
#Output:
print("Total Marks:", total)
print("Average Marks:", avg)
print("Percentage:", percentage, "%")
print("Highest Scoring Subject is:", most_scoring_subject)
print("Least Scoring Subject is :", lowest_scoring_subject)
