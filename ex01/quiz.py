import random

def main():
    seikai = shutsudai()
    kaitou(seikai)

def shutsudai():
    Q = [
         {"q":"サザエさんの旦那の名前は？","a":["マスオ", "ますお"]},
         {"q": "カツオの妹の名前は？","a":["ワカメ", "わかめ"]}
         {"q": "タラオはカツオから見てどんな関係？", "a":["甥", "おい", "甥っ子","おいっこ"]},
        ]
    A0 = ["マスオ", "ますお"]
    A1 = ["ワカメ", "わかめ"]
    A2 = ["甥","おい", "甥っ子", "おいっこ"]
    print("問題：")
    r = random.randint(0,2)
    print(Q[r]["q"])
    return Q[r]["a"]

def kaitou(seikai):
    a = input("答えるんだ：")
    if a in seikai:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()

    