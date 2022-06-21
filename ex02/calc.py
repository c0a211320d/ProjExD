
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
        btn = event.widget
        num = btn["text"]
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
        if num == "=":
            eq = entry.get()
            re = eval(eq)
            entry.delete(0, tk.END)
            entry.insert(tk.END, re)
            if num == "/":
                if num == 0:
                    entry.deelte(0, tk.END)
                    entry.insert(tk.END, 0)

        elif num == "C":
            entry.delete(0, tk.END)
        
        else:
            entry.insert(tk.END, num)

#def button_click0(event):
    #btn = event.widget
    #txt = btn["注意"]
   # tkm.shoeinfo(txt, f"0で割ることはできません")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x600")

    entry = tk.Entry(root,
                    justify = "right",
                    width = "10",
                    font = ("Time New Roman" , 40)
                    )
    entry.insert(tk.END, "数値を入力してください")
    entry.grid(column=0, columnspan=5)

    r = 1;c = 0
    for num,i in enumerate(["+","-","*","/",9,8,7,6,5,4,3,2,1,0, "C", "="]):
        button = tk.Button(root, 
                                text=i, 
                                width="4", 
                                height="2", 
                                font=("Times New Roman", 30)
                                )
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if (num+1) % 4 == 0:
            r += 1
            c = 0
    

    root.mainloop()