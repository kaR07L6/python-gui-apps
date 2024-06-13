import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑




def button_acyion():
    user_input = entry1.get()
    ladel.config(text=f"Hello, {user_input}!")


entry1 = tk.Entry(window, bg=fg_color)
entry1.park(pady=10)

int_input = int(input())
 
if(int_input >= 1868 and int_input <=1911):
    str_nengo = "明治"
    int_year = int_input - 1867
    if(int_year == 1):
        int_lastYear = int_input - 1864
        str_lastYear = ""
        print("西暦", int_input , "年" , str_nengo, "元年(", str_lastYear, int_lastYear )
    else:
        print("西暦", int_input , "年", str_nengo, int_year, "年" )
    
elif(int_input >=1912 and int_input <=1925):
    str_nengo = "大正"
    int_year = int_input - 1911
    if(int_year ==1):
        int_lastYaer = int_input - 1867
        str_lastYaer = "明治"
        print("西暦", int_input, "年", str_nengo, "元年(", str_lastYaer, int_lastYear )
    else:
        print("西暦", int_input, "年", str_nengo,int_year, "年")

elif(int_input >=1926 and int_input <=1988):
    str_nengo = "昭和"
    int_year = int_input - 1925
    if(int_year == 1):
        int_lastYear = int_input -1911
        str_lastYear = "大正"
        print("西暦", int_input, "年", str_nengo, "元年")

        

#入力フィールド
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

#ボタンの作成
button1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
button1.pack(pady=10)

#出力ラベル
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
