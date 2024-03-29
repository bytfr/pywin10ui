# PyWin10UI

官网:http://pywin10ui.grmine.cn/

邮箱:2678509244@qq.com

作者:bytfr



**本模块依赖Pygame，所以本模块可以跟Pygame交互**
**需要额外安装EasyGUI和Pygame模块**

## 依赖模块安装命令

```shell
pip install pygame
pip install easygui
```

## Window() 窗口类

- ### 参数

  - title  窗口标题
  - width  窗口宽
  - height  窗口高
  - icon  窗口图标(需用pygame.image.load("图片链接"))

- ### 方法

  - #### create

    - 创建窗口

  - #### mainloop

    - 显示窗口

  - #### append_component

    - 添加组件 (在显示组件(mainloop)前必须先添加组件!!!)



## FillText() 文字类

- ### 参数

  - canvas  窗口
  - text  文本
  - x  x坐标
  - y  y坐标
  - font  字体(需自行加载)
  - rgb  字体RGB颜色
  - gjc  抗锯齿  bool类型
  - quyu  显示文本区域(可空)

- ### 方法

  - #### paint

    - 绘画



## Rectangula() 矩形类

- ### 参数

  - canvas  窗口
  - text  文本
  - x  x坐标
  - y  y坐标
  - rgb  矩形RGB颜色
  - gjc  抗锯齿  bool类型
  - alpha  不透明度(最大255)

- ### 方法

  - #### paint

    - 绘画

# 例子 DEMO

```python
# coding:utf-8
import pywin10ui, tkinter.messagebox, pygame, sys


def quit_def():
    if tkinter.messagebox.askokcancel('提示', '要执行此操作吗'):
        pygame.quit()
        sys.exit()


def button_commond():
    print("button down")


window = pywin10ui.Window("测试", 300, 200, Exit_the_method=quit_def)

button = pywin10ui.Button(window, 150, 1, "Button", 80, 32, common=button_commond)
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



```

