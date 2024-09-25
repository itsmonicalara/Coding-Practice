def current_solution(n):
    print('Current solution - Not ideal')
    for ele in range(0, n):
        squared_num = ele * ele
        ele = ele + 1
        print(squared_num)

def past_solution(n):
    print('Previous solution - Better')
    for i in range(0, n):
            print(i * i)


if __name__ == '__main__':
    n = int(input())
    current_solution(n)
    past_solution(n)