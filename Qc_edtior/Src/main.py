import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def b1_click():
    print("Button 1 clicked")
def b2_click():
    print("Button 2 clicked")


root = ttk.Window(themename='darkly')
root.geometry("400x200")
ovalues = ['选项1', '选项2']
menubox = ttk.OptionMenu(root, ttk.StringVar(), ovalues[0], *ovalues)
menubox.pack(padx=10, pady=10)
menubox.pack(padx=10,pady=10)


b1 = ttk.Button(root, text="Submit", bootstyle="warning",command=b1_click)
b1.pack(padx=5, pady=10)
b2 = ttk.Button(root, text="Submit", bootstyle="danger-link",command=b2_click)
b2.pack(padx=5, pady=10)
combox = ttk.Combobox(root,state='readonly',style='danger')
values = [f'qc{i+1}' for i in range(10)]
combox['values']= values
combox.current(0)
combox.pack(padx=5,pady=10)
# 定义回调函数
def on_combobox_change(*args):
    current_value = combox['values'][combox.current()]
    print(f'当前combox值为: {current_value}')

# 监听 current 属性的变化
combox.bind('<<ComboboxSelected>>', on_combobox_change)



root.mainloop()