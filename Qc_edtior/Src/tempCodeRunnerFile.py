    # 创建一个Frame小部件，用于放置Text和Scrollbar
    frame = ttk.Frame(root)
    frame.pack()

    # 创建一个Scrollbar小部件
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # 创建一个Text小部件，并将其与Scrollbar关联
    text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.pack(side=tk.LEFT, fill=tk.BOTH)

    # 将Scrollbar与Text关联
    scrollbar.config(command=text.yview)

    # 设置初始的文本内容
    text.insert(tk.END, "这是初始的文本内容\n")
