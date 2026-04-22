from main import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score < 50:
            return "F"
        elif 50 <= score < 60:
            return "E"
        elif 60 <= score < 70:
            return "D"
        elif 70 <= score < 80:
            return "C"
        elif 80 <= score < 90:
            return "B"
        elif 90 <= score <= 100:
            return "A"
    def find(self, score):
        new_list = self.scores
        counter_while = 0
        while counter_while < len(new_list):
            minimum_number = min(new_list[counter_while:])
            for idx, i in enumerate(new_list[counter_while:]):
                if i == minimum_number:
                    real_idx = idx + counter_while
                    new_list[counter_while], new_list[real_idx] = new_list[real_idx], new_list[counter_while]
                    break
            counter_while += 1
        return new_list

    def get_sorted(self):
        new_list = self.scores
        counter_while = 0
        while counter_while < len(new_list):
            swap_Bool = False
            for idx in range(len(new_list) - 1 - counter_while):
                if new_list[idx] > new_list[idx + 1]:
                    new_list[idx], new_list[idx + 1] = new_list[idx + 1], new_list[idx]
                    swap_Bool = True
            if not swap_Bool:
                break
            counter_while += 1
        return new_list

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count)
    for student_id in range(results.count()):
        print(f"Student {student_id}: {results.get_by_index(student_id)} points – {results.get_grade(student_id)}")
    print(f"Plny počet měli studenti: {results.find(100)}")
    print(f"seznam vysledky: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    #
    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny