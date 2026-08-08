import tkinter as tk
from tkinter import messagebox

#密码逼
CORRECT_PASSWORD = "#1980000"
#神秘小网站
UNLOCK_URL = "We are together"

def verify_password():
    """验证"""
    entered_password = password_var.get()
    if entered_password == CORRECT_PASSWORD:
        #NBbro
        hint_label.config(text="哎呀，空间界面出错啦，这些是从里面捡的文件", fg="#420000")
        result_label.config(text=UNLOCK_URL, fg="green")
        password_entry.delete(0, tk.END)
    else:
        # False
        password_entry.delete(0, tk.END)
        messagebox.showerror("错误", "这个密码不能匹配该用户下的任何空间或隐私空间")




def on_enter_key(event):
    """轻按Enter验证"""
    verify_password()


#主窗口
root = tk.Tk()
root.title("Kookoo furre APP(Offline)")
root.geometry("520x380")
root.resizable(False, False)
root.configure(bg="#F0F0F0")  # 纯色背景（浅灰白）

#小菜
menubar = tk.Menu(root)

#菜单
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="账户", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="编辑", menu=edit_menu)

insert_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="插入", menu=insert_menu)

td_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="连接", menu=td_menu)

script_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="脚本", menu=script_menu)

option_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="选项", menu=option_menu)

root.config(menu=menubar)

# TIPs
# Sl）
label_account = tk.Label(root, text="账户:JF-Vjg nghv dgjkpf", font=("微软雅黑", 14),
                         fg="#272727", bg="#F0F0F0")
label_account.pack(pady=(25, 5))

# Fl
label_title = tk.Label(root, text="离线状态仅限密码解锁", font=("微软雅黑", 14, "bold"),
                       fg="black", bg="#F0F0F0")
label_title.pack(pady=(30, 5))

# Look in my eyes!
input_frame = tk.Frame(root, bg="#F0F0F0")
input_frame.pack()

password_var = tk.StringVar()
password_entry = tk.Entry(input_frame, textvariable=password_var, show="●",
                          font=("微软雅黑", 12), width=25, bd=2, relief="solid")
password_entry.pack(side=tk.LEFT, padx=(0, 10))
password_entry.bind("<Return>", on_enter_key)  #验证

verify_button = tk.Button(input_frame, text="解锁", command=verify_password,
                          font=("微软雅黑", 10), bg="#4A90D9", fg="white",
                          activebackground="#357ABD", padx=15)
verify_button.pack(side=tk.LEFT)


#强强强
hint_label = tk.Label(root, text="", font=("微软雅黑", 11),
                      fg="#420000", bg="#F0F0F0", wraplength=480, justify="center")
hint_label.pack(pady=(15,5))
result_label = tk.Label(root, text="", font=("微软雅黑", 11, "underline"),
                        fg="green", bg="#F0F0F0", wraplength=480, justify="center")
result_label.pack(pady=30)

root.mainloop()
