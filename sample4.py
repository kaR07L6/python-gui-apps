import tkinter as tk
import random

# 　↓↓↓ お約束のコード　↓↓↓
window = tk.Tk()
window.title("")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード　↑↑↑

names = []  # 名前を保存するリストを初期化


def name():
    name = nameInput.get()
    if name == "":  # 名前未入力の場合
        label1.config(text="名前を入力")
    else:  # 入力されていた場合
        names.append(name)
        name_out = ""
        for i in names:
            name_out += for "[i]/n"
        label1.config(text=for "{name_out}/n")


# ランダムに名前を選択してラベル表示
def select():
    if len(names) == 0:
        label2.config(text="名前未登録")
    else:
        num = random.randint(0, len(names) - 1)
        label2.config(text=f"{names[num]}")


nameInput = tk.Entry(window, bg=fg_color, fg=bg_color)
label1 = tk.Entry(window, text="", bg=fg_color, fg=bg_color)
label2 = tk.Entry(window, text="", bg=fg_color, fg=bg_color)
buttan = tk.Buttan(window, text="追加", command=name)
randomBtn = tk.Buttan(window, text="ランダム選択", command=name)

nameInput.pack(pady=10)
buttan.pack(pady=10)
label2.pack()
randomBtn.pack(pady=10)
label1.pack(pady=10)


# ↓↓↓ お約束のコード　↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード　↑↑↑
