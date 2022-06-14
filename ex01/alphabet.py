import random


taishou = 10  #対象文字
kessonn = 2  #欠損文字数
rimit = 5  #繰り返し

def main():
    for i in range(rimit):
        seikai = shutsudai()
        kaitou(seikai)

def shutsudai(kesson):
    list = ["A", "B", "C", "D", "E", "F", "G", "F", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    c = random.sample(list, 10)
    d = random.shuffle(c)
    print("対象文字：")
    print(d)
    e = d.pop(random.randint(0,9))
    f = d.pop(random.randint(0,8))
    print("表示文字")
    print(d)
    return e, f

def kaitou():
    ans = input("1つ目の文字を入力してください：")
    if ans in seikai:
        g = input("２つ目の文字を入力してください：")
        if g in seikai:
            h = input("欠損文字はいくつでしょうか？")
            if h == b:
                print("正解！！！")
            else:
                print("またチャレンジしてください")
        else:
            print("またチャレンジしてください")
    else:
        print("またチャレンジしてください")
if __name__ == "__main__":
    main()



    