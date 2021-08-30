#21번
# 학생들의 시험 점수가 주어졌을 때, n번 학생이 몇 등인지 구하려 합니다. 학번은 0번부터 시작하며,
# 시험 점수는 학번순으로 주어집니다.
# ~~~
# 1. n번 학생의 점수를 변수에 저장합니다.
# 2. 점수를 내림차순으로 정렬합니다.
# 3. 리스트의 첫 번째 원소부터 마지막 원소까지 순회하며 n번 학생의 점수를 찾습니다.
#   3-1. 1번 단계에서 저장해둔 점수와 같은 점수를 찾으면 등수를 return 합니다.
# ~~~
#
# 학생들의 시험 점수가 번호순으로 들은 리스트 scores와 학번 n이 solution 함수의 매개변수로 주어질 때, n번 학생의 등수를 return 하도록 solution 함수를 작성하려 합니다. 위 구조를 참고하여 코드가 올바르게 동작하도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.
def func_a(scores,score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0
def func_b(arr):
    arr.sort(reverse = True)
def func_c(arr,n):#n은 학번
    return arr[n]
def solution(scores,n):
    score = func_c(scores,n)
    func_b(scores)
    answer = func_a(scores,score)
    return answer
#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] #점수가 들어간 score배열
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
# 22번
# 모 학교에서는 학기가 끝날 때마다 장학금을 줍니다.
# 이때 장학생이 몇 명인지 구하려고 합니다. 장학금을 주는 조건은 다음과 같습니다.
# 1. 이번 학기 성적이 80점 이상(100점 만점)이면서 석차가 상위 10% 이내인 학생
# 2. 이번 학기 성적이 80점 이상이면서 1등인 학생
# 3. 직전 학기 대비 성적이 가장 많이 오른 학생(여러 명인 경우 해당 학생 전부)
#
# 단, 동점인 학생들은 등수가 같으며, 중복 수혜는 불가합니다.
#
# 장학생이 몇 명인지 구하기 위해 다음과 같이 프로그램 구조를 작성했습니다.
#
# ~~~
# 1. 이번 학기 성적을 기준으로 학생별 석차를 구합니다.
# 2. 각 학생의 (이번 학기 성적 - 직전 학기 성적) 중 최댓값을 구합니다.
# 3. 아래 조건을 만족하는 학생을 발견하면, 장학생 수를 1 증가시킵니다.
#  3-1. 이번 학기 성적이 80점 이상이고, 석차가 상위 10% 이내인 경우
#  3-2. 또는 이번 학기 성적이 80점 이상이고, 석차가 1등인 경우
#  3-3. 또는 (이번 학기 성적 - 직전 학기 성적)이 2단계에서 구한 값과 같고, 그 값이 양수인 경우
# 4. 장학생 수를 return 합니다.
# ~~~
def func_a(current_grade,last_grade,rank,max_diff_grade):
    arr_length = len(current_grade)
    count = 0
    for i in range(arr_length):
        if current_grade[i]>=80 and rank[i] <= arr_length // 10:
            count += 1
        elif current_grade[i]>=80 and rank[i] == 1:
            count += 1
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            count += 1
        return count
    def func_b(current_grade):
        arr_length = len(current_grade)
        rank = [1] * arr_length
        for i in range(arr_length):
            for j in range(arr_length):
                if current_grade[i]<current_grade[j]:
                    rank[i] += 1
        return rank
    def func_c(current_grade,last_grade):
        max_diff_grade = 1
        for i in range(len(current_grade)):
            max_diff_grade = max(max_diff_grade[i]-last_grade[i])
            return max_diff_grade
        def solution(current_grade,last_grade):
            rank = func_b(current_grade)
            max_diff_grade = func_c(current_grade,last_grade)
            answer = func_a(current_grade,last_grade,max_diff_grade)
            return answer
#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
        current_grade = [70, 100, 70, 80, 50, 95]
        last_grade = [35, 65, 80, 50, 20, 60]
        ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

# 25번
# 여행객들의 총 교통비를 계산하려고 합니다. 교통편은 "Bus", "Ship", "Airplane" 총 3가지입니다. 나이가 20살 이상이면 어른 요금을, 그렇지 않으면 어린이 요금을 받습니다. 각 교통편별 가격은 다음과 같습니다.
#
# |   | 어른 | 어린이 |
# |---|---|---|
# | Bus | 40,000원  | 15,000원 |
# | Ship |  30,000원 | 13,000원 |
# | Airplane | 70,000원 | 45,000원 |
#
# 여행객들이 10명 이상인 경우 연령에 따라 할인을 받습니다.
#
# | 어른 | 어린이 |
# |---|---|
# | 10% | 20% |
#
# 여행객들의 나이를 담고 있는 리스트 member_age와 교통편인 transportation이 매개변수로 주어질 때, 총 교통비를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.
def soultion(member_age,transprtation):
    if transprtation == "Bus":
        adult_expense = 40000
        child_expense = 15000
    elif transprtation == "Ship":
        adult_expense = 30000
        child_expense = 13000
    elif transprtation == "Airplane":
        adult_expense = 70000
        child_expense = 13000
    if len(member_age) >=10:
        adult_expense = int(adult_expense*0.9)
        child_expense = int(child_expense*0.8)
    total_expenses = 0
    for age in member_age:
        if age >= 20:
            total_expenses += adult_expense
        else:
            total_expenses += child_expense

    return total_expenses
# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")








