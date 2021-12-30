# PyWin10UI

官网:http://pywin10ui.grmine.cn/

邮箱:2678509244@qq.com

作者:bytfr



**本模块依赖Pygame，所以本模块可以跟Pygame交互**



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
import pywin10ui

window = pywin10ui.Window("DEMO",200,200)

canvas = window.create()

button = pywin10ui.Button(canvas,1,1,"Button",100,20)
entry = pywin10ui.Entry(canvas,1,25,"Entry",100,20)
progress_bar = pywin10ui.Progress_bar(canvas,1,50,100,20,100,50)
select_box = pywin10ui.Select_box(canvas,1,75,"Select_box")

while 1:
    canvas.fill((240,240,240))
    button.mainloop()
    entry.mainloop()
    progress_bar.mainloop()
    select_box.mainloop()
    window.mainloop()
```

