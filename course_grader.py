def course_grader(test_scores):
    avg =(sum(test_scores)) / (len(test_scores))
    
    for num in test_scores:
        if num < 50:
            return("fail")
    if avg >= 70:
        return("pass")
    if avg < 70:
        return ("fail")
def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()
