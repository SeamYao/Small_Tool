from pypdf import PdfReader, PdfWriter

import tkinter as tk
from tkinter import filedialog

def pdf_add_password():
    pdf_path = pdf_path_stv.get()
    print(pdf_path)

    # 1. 读取原始PDF
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # 2. 将所有页面添加到写入器
    for page in reader.pages:
        writer.add_page(page)

    # 3. 设置密码（核心步骤）
    # 参数可以是用户密码和所有者密码，如果只传一个字符串，则两者相同
    password = password_ent.get()  #修改
    writer.encrypt(password)

    save_path = pdf_path + "_加密.pde"
    print(save_path)

    # 4. 保存加密后的PDF
    with open(save_path, "wb") as output_file:
        writer.write(output_file)

def open_file():
    file_path = filedialog.askopenfilename(title="選擇要打開的文檔",filetypes=[("所有文件", "*.*"), ("文本文件", "*.txt"), ("Word文件", "*.docx")])
    print(file_path)
    pdf_path_stv.set(file_path)

root = tk.Tk()
root.geometry("300x400")
fileMenuList = tk.Menu(root,tearoff=False)
fileMenuList.add_command(label="打開", command=open_file)
menuList = tk.Menu(root)
menuList.add_cascade(label="檔案",menu=fileMenuList)

root.config(menu=menuList)

pdf_path_stv = tk.StringVar

password_ent = tk.Entry(root)
password_ent.pack()

save_btn = tk.Button(root,text="保存",command=pdf_add_password)
save_btn.pack()

root.mainloop()