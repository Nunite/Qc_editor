import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CreatMethod:
    def __init__(self,root):
        self.root = root

    def Notice(self,test):
        print("Notice method called"+test)
    
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

def Creatwindow(root):
    root.geometry('500x400')
    
    # 示例：添加一个标签
    label = ttk.Label(root, text="Hello, TtkBootstrap!")
    label.pack(pady=20)
    #place button
    creat_method = CreatMethod(root)
    Noticebutton = ttk.Button(root,text="Notice",command=lambda:creat_method.Notice("Again hello word"))
    Noticebutton.pack(pady=20)
    root.mainloop()

# 创建一个实例并调用 Creatwindow 函数
if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    Creatwindow(root)
