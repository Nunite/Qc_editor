import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import DND_FILES, TkinterDnD

class CreatMethod:
    def __init__(self,root):
        self.root = root

    def Notice(self,text):
        print(f"{text.get('1.0','1.end')}")
        text.config(state="normal")
        text.delete("1.0",ttk.END)
        text.insert(ttk.END,"Notice method called")
        text.config(state="disabled")
    
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

class BaseWeight_TextGet:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.TextEntry = None

    def Create(self):
        TextFrame = ttk.Frame(self.root)
        TextFrame.pack(side=ttk.TOP)
        TextLable = ttk.Label(TextFrame, text=f"{self.name}:")
        TextLable.pack(side=ttk.LEFT)
        self.TextEntry = ttk.Entry(TextFrame)
        self.TextEntry.insert(ttk.END, "Start Content")
        self.TextEntry.pack(side=ttk.LEFT)

    def Get(self):
        print(self.TextEntry.get())

    def SetText(self, text):
        # 设置文本框内容
        self.TextEntry.delete(0, ttk.END)
        self.TextEntry.insert(0, text)


def Creatwindow():
    # 使用 TkinterDnD 初始化窗口以支持拖拽
    root = TkinterDnD.Tk()  # 使用 ttkbootstrap 创建窗口
    ttk.Style("darkly")
    root_length = "800"
    root_width = "600"
    putscreen_height = (root.winfo_screenheight() - int(root_length)) // 2
    putscreen_width = (root.winfo_screenwidth() - int(root_width)) // 2
    root.geometry(f"{root_length}x{root_width}+{putscreen_width}+{putscreen_height}")
    root.resizable(False, False)

    # 创建 BaseWeight_TextGet 输入框
    modelname = BaseWeight_TextGet(root, "modelname")
    modelname.Create()

    # 添加按钮，用于测试获取输入框内容
    testbutton = ttk.Button(root, text="TestButton", command=lambda: modelname.Get())
    testbutton.pack(pady=10)

    # 将拖放功能绑定到文本框
    def on_drop(event):
        # 获取拖放的文件路径并设置到文本框中
        file_path = event.data.strip('{}')  # 去除路径中的大括号
        modelname.SetText(file_path)
        print(f"File dropped: {file_path}")

    # 绑定拖拽事件到输入框
    modelname.TextEntry.drop_target_register(DND_FILES)
    modelname.TextEntry.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()


# 调用 Creatwindow 函数
if __name__ == "__main__":
    Creatwindow()
