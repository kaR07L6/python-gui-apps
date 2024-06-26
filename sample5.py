import tkinter as tk

# ↓↓↓お約束のコード↓↓↓
window = tk.Tk()
window.title("西暦 / 和暦変換アプリ")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレイ
fg_color = "#FFFFFF"  # 白
window.configure(bg=fg_color)
# 　↑↑↑お約束のコード ↑↑↑


def deta():
    num = int(entry1.get())
    if num >= 1868 and num <= 1911:
        if (num - 1867) == 1:
            label1.config(text=f"西暦{num}年は明治元年")
        else:
            label1.config(text=f"西暦{num}年は明治{num - 1867}年")

    elif num >= (1912 and num <= 1925):
        if (num - 1911) == 1:
            label1.config(text=f"西暦{num}年は大正元年")
        else:
            label1.config(text=f"西暦{num}年は大正{num - 1911}年")

    elif num >= (1926 and num <= 1988):
        if (num - 1925) == 1:
            label1.config(text=f"西暦{num}年は昭和元年")
        else:
            label1.config(text=f"西暦{num}年は昭和{num - 1988}年")

    elif num >= (1989 and num <= 2018):
        if (num - 1988) == 1:
            label1.config(text=f"西暦{num}年は平成元年")
        else:
            label1.config(text=f"西暦{num}年は平成{num - 1988}年")

    elif num >= (2029 and num <= 2050):
        if (num - 2018) == 1:
            label1.config(text=f"西暦{num}年は平和元年")
        else:
            label1.config(text=f"西暦{num}年は令和{num - 1988}年")

    else:
        label1.config(text=f"西暦{num}年は変換されていません。")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=deta)
button1.pack(pady=10)

# 出力ラベル
label1 = tk.Label(window, text="西暦を入力してください", bg=fg_color, fg=bg_color)
label1.pack(pady=10)

# 　↓↓↓ お約束のコード　↓↓↓
window.mainloop()
# 　 ↓↓↓ お約束のコード  ↓↓↓


