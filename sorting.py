from itertools import count
import matplotlib.pyplot as plt

from main import random_numbers as ran

def selection_sort(list):
    new_list = list.copy()
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

def bubble_sort(list):
    new_list = list.copy()
    # plt.ion()
    # plt.show()
    counter_while = 0
    while counter_while < len(new_list):
        swap = False
        for idx in range(len(new_list) - 1 - counter_while):
            # index_highlight1 = idx
            # index_highlight2 = idx + 1
            # colors = ["steelblue"] * len(new_list)
            # colors[index_highlight1] = "tomato"
            # colors[index_highlight2] = "tomato"
            # plt.clf()
            # plt.bar(range(len(new_list)), new_list, color=colors)
            # plt.title("Bubble Sort")
            # plt.pause(0.1)
            if new_list[idx] > new_list[idx + 1]:
                new_list[idx], new_list[idx + 1] = new_list[idx + 1], new_list[idx]
                swap = True
        if not swap:
            break
        counter_while += 1
        # plt.ioff()
        # plt.show()
    return new_list




def main():
    random_list = ran(10)
    print(selection_sort(random_list))
    print(bubble_sort(random_list))
    # bubble_sort(random_list)
    print(sorted(random_list))


if __name__ == "__main__":
    main()
