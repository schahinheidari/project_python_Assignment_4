#Assignment 4
def count_word():
    m = str(input("please input your text: "))
    count = 0
    for i in m:
        if i == " ":
            count = count + 1
    print(count)

count_word()