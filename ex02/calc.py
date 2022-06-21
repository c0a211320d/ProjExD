
import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    def button_click(event):
        btn = event.widget
        num = btn["text"]
        tkm.showinfo("", f"{num}のボタンがクリックされました")
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x500")

    r, c = 0, 0
    for i in range(9, -1, -1):
        btn = button = tk.Button(root, 
                                text=f"{i}", 
                                width="4", 
                                height="2", 
                                font=("Times New Roman", 30)
                                )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)
        c += 1
        if (i-1) % 3 == 0:
            r += 1
            c = 0

    root.mainloop()