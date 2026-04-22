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
        if score < 50: return "F"
        elif score < 60: return "E"
        elif score < 70: return "D"
        elif score < 80: return "C"
        elif score < 90: return "B"
        else: return "A"

    def find(self, target_score):
        # Najde indexy studentů, kteří mají daný počet bodů
        found_indices = []
        for idx, score in enumerate(self.scores):
            if score == target_score:
                found_indices.append(idx)
        return found_indices

    def get_sorted(self):
        # Používáme .copy(), aby se nezměnilo původní pole self.scores
        new_list = self.scores.copy()
        n = len(new_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if new_list[j] > new_list[j + 1]:
                    new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
        return new_list

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    
    # Opraveno results.count -> results.count()
    print(f"Počet studentů: {results.count()}")
    
    for student_id in range(results.count()):
        print(f"Student {student_id}: {results.get_by_index(student_id)} bodů – {results.get_grade(student_id)}")
    
    print(f"Indexy studentů s plným počtem (100): {results.find(100)}")
    print(f"Seřazené výsledky: {results.get_sorted()}")
    print(f"Původní seznam (beze změny): {results.scores}")

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
