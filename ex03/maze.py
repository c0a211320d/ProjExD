import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, key
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
    elif key == "Up":
        tkm.showwarning("警告", "上は壁です")
    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
    elif key == "Down":
        tkm.showwarning("警告", "下は壁です")
    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1
    elif key == "Right":
        tkm.showwarning("警告", "右は壁です")
    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
    elif key == "Left":
         tkm.showwarning("警告", "左は壁です")
    key = ""
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)

    #print(maze_bg)

    tori = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    label = tk.Label(root, text="S", font=("Time New Roman" , 50), width=150, height=150)
    label.pack()
    main_proc()
    root.mainloop()