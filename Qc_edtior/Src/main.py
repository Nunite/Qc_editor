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
    def __init__(self, root, name, entry_width=12, font_size=20):
        self.root = root
        self.name = name
        self.TextEntry = None
        self.drag_and_drop_enabled = False  # 添加拖拽功能开关
        self.entry_width = entry_width  # 文本框宽度
        self.font_size = font_size  # 字体大小

    def Create(self):
        TextFrame = ttk.Frame(self.root)
        TextFrame.pack(side=ttk.TOP)

        # 标签
        TextLable = ttk.Label(TextFrame, text=f"{self.name}:",font=("Arial", self.font_size))
        TextLable.pack(side=ttk.LEFT)

        # 设置文本框宽度和字体大小
        self.TextEntry = ttk.Entry(TextFrame, width=self.entry_width, font=("Arial", self.font_size))
        self.TextEntry.pack(side=ttk.LEFT)

        # 根据拖拽功能开关来决定是否绑定拖拽事件
        if self.drag_and_drop_enabled:
            self.TextEntry.drop_target_register(DND_FILES)
            self.TextEntry.dnd_bind('<<Drop>>', self.on_drop)

    def Get(self):
        print(self.TextEntry.get())

    def SetText(self, text):
        # 设置文本框内容
        self.TextEntry.delete(0, ttk.END)
        self.TextEntry.insert(0, text)

    def on_drop(self, event):
        # 获取拖放的文件路径并设置到文本框中
        file_path = event.data.strip('{}')  # 去除路径中的大括号
        self.SetText(file_path)
        print(f"File dropped: {file_path}")

def Creatwindow():
    # 使用 TkinterDnD 初始化窗口以支持拖拽
    root = TkinterDnD.Tk()  # 使用 ttkbootstrap 创建窗口
    root.title("Qcreator")
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
    modelname.drag_and_drop_enabled = True


    root.mainloop()



# 调用 Creatwindow 函数
if __name__ == "__main__":
    Creatwindow()
