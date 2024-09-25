import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CreatMethod:
    def __init__(self,root):
        self.root = root

    def Notice(self,text):
        print("Notice method called")
        text.delete("1.0",ttk.END)
        text.insert(ttk.END,"Notice method called")
    
    def Modlelname(self):
        print("Modlelname method called")
    
    def Cd(self):
        print("Cd method called")
    
    def Cdtexture(self):
        print("Cdtexture method called")
    
    def Cliptotextures(self):
        print("Cliptotextures method called")
    
    def Scale(self):
        print("Scale method called")
    
    def Texrendermode(self):
        print("Texrendermode method called")
    
    def Gamma(self):
        print("Gamma method called")
    
    def Origin(self):
        print("Origin method called")
    
    def Bbbox(self):
        print("Bbbox method called")
    
    def Cbox(self):
        print("Cbox method called")
    
    def Hbox(self):
        print("Hbox method called")
    
    def Eeyposition(self):
        print("Eeyposition method called")
    
    def Body(self):
        print("Body method called")
    
    def Body_group(self):
        print("Body_group method called")
    
    def Flags(self):
        print("Flags method called")
    
    def Texturegroup(self):
        print("Texturegroup method called")
    
    def Sequence(self):
        print("Sequence method called")


def Creatwindow():
    root = ttk.Window(themename="darkly")
    root_length = "400"
    root_width = "200"
    putscreen_height = (root.winfo_screenheight()-int(root_length))//2
    putscreen_width = (root.winfo_screenwidth()-int(root_width))//2
    root.geometry(f"{root_length}x{root_width}+{putscreen_width}+{putscreen_height}")
    root.resizable(False, False)
    # 示例：添加一个标签
    label = ttk.Label(root, text="Hello, TtkBootstrap!")
    label.pack(pady=20)
    #place button
    creat_method = CreatMethod(root)
    Noticebutton = ttk.Button(root,text="Notice",command=lambda:creat_method.Notice(text))
    Noticebutton.pack(pady=10)
    # 创建一个Frame小部件，用于放置Text和Scrollbar
    frame = ttk.Frame(root)
    frame.pack()

    # 创建一个Scrollbar小部件
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)

    # 创建一个Text小部件，并将其与Scrollbar关联
    text = ttk.Text(frame, wrap=ttk.WORD, yscrollcommand=scrollbar.set)
    text.pack(side=ttk.LEFT, fill=ttk.BOTH)

    # 将Scrollbar与Text关联
    scrollbar.config(command=text.yview)

    # 设置初始的文本内容
    text.insert(ttk.END, "这是初始的文本内容\n")

    root.mainloop()

# 调用 Creatwindow 函数
if __name__ == "__main__":
    Creatwindow()
