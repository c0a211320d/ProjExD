import random
def main():
    shutsudai()
    
def shutsudai():
    Q = [0, 1, 2]
    A1 = ["マスオ", "ますお"]
    A2 = ["ワカメ", "わかめ"]
    A3 = ["甥","おい", "甥っ子", "おいっこ"]
    if random.choice(Q) == 0:
        input("サザエさんの旦那の名前は？")
        a = input("答えるんだ：")
        if a == A1:
            print("正解！！！")
        else:
            print("出直してこい")
    elif random.choice(Q) == 1:
        input("カツオの妹の名前は？")
        a = input("答えるんだ：")
        if a == A2:
            print("正解！！！")
        else:
            print("でなおしてこい")
    elif random.choice(Q) == 2:
        input("タラオはカツオから見てどんな関係？")
        a = input("答えるんだ：")
        if a == A3:
            print("正解！！！")
        else:
            print("出直してこい")