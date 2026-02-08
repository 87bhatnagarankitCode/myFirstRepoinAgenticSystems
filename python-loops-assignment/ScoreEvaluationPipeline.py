
Student_scores = [72, 45, 89, 30, 60]

#for score in Student_scores:
#    if score >= 50:
#        print("pass")
#    else:
#        print("fail")    

for mark in range(len(Student_scores))  :
    if Student_scores[mark] >= 50:
        print("pass : "  , Student_scores[mark])
    else:
        print("fail : "  , Student_scores[mark])  
