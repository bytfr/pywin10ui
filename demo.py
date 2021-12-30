# coding:utf-8
import __init__ as pywin10ui, tkinter.messagebox, pygame, sys


def quit_def():
    if tkinter.messagebox.askokcancel('提示', '要执行此操作吗'):
        pygame.quit()
        sys.exit()


window = pywin10ui.Window("测试", 300, 200, Exit_the_method=quit_def)

button = pywin10ui.Button(window, 150, 1, "Button", 80, 32)
entry = pywin10ui.Entry(window, 1, 25, "Entry", 100, 20)
progress_bar = pywin10ui.Progress_bar(window, 1, 50, 100, 20, 100, 50)
select_box = pywin10ui.Select_box(window, 1, 75, "Select_box")
picture_box = pywin10ui.Picture_box(window, 1, 100, 150, 100, img=None)

window.append_component([button, entry, progress_bar, select_box, picture_box])

while 1:
    window.mainloop()
    window.canvas.fill((240, 240, 240))
    button.mainloop()
    entry.mainloop()
    progress_bar.mainloop()
    select_box.mainloop()
    picture_box.mainloop()

    window.set_tiltle("测试 DEMO")
