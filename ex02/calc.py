
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
        btn = event.widget
        num = btn["text"]
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
        if num == "=":
            eq = entry.get()
            re = eval(eq)
            entry.delate(0, tk.END)
            entry.insert(tk.END, re)
        else:
            entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x600")

    entry = tk.Entry(root,
                    justify = "right",
                    width = "10",
                    font = ("Time New Roman" , 40)
                    )
    entry.grid(row=0, column=0, columnspan=3)

    r = 1;c = 0
    for num,i in enumerate([9,8,7,6,5,4,3,2,1,0,"+", "="]):
        button = tk.Button(root, 
                                text=i, 
                                width="4", 
                                height="2", 
                                font=("Times New Roman", 30)
                                )
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if (num+1) % 3 == 0:
            r += 1
            c = 0
    

    root.mainloop()