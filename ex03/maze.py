import tkinter as tk
import maze_maker as mm

def main_proc():
    global cx, cy, key, mx, my
    if (key == "Up"):
        my -= 1
    if (key == "Down"):
        my += 1
    if (key == "Left"):
        mx -= 1
    if (key == "Right"):
        mx += 1
    cx = 50 + mx * 100
    cy = 50 + my * 100
    Canvas.coords("Kouka", cx, cy)

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym
    main_proc()
    print(key)

if __name__ == "__main__":
    cx = 150
    cy = 150
    mx = 1
    my = 1
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    Canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    maze = mm.make_maze(15,9)
    mm.show_maze(Canvas, maze)
    image = tk.PhotoImage(file="fig/0.png")
    Canvas.create_image(cx, cy, image=image, tag="Kouka")
    Canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()