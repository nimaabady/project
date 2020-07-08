def fibonachi():
    print('fibonachi is called: ')
    n1 = 1
    n2 = 1
    print(n1, end=' ')
    print(n2, end=' ')
    counter = 0
    while counter < 10:
        counter += 1
        print(n1 + n2, end=' ')
        temp = n1
        n1 = n2
        n2 = temp + n2


# Main
fibonachi()
