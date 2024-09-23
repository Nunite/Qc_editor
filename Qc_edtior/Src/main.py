import tkinter as tk

def myfunction1():
    print("Hello World")
    #更改button0的颜色
    button0.config(text='already clicked')

def myfunction2():
    print("Goodbye World")

window = tk.Tk()
window.title("My First GUI")
window.geometry("900x800")

# 创建第一个按钮
button0 = tk.Button(window, text='1: 根据标记内容生成', fg='red',command=myfunction1)
button1 = tk.Button(window, text='2: 根据手动输入生成', command=myfunction2)
button0.pack(pady=10) 
# 创建第二个按钮
button1.pack(pady=10)
window.mainloop()