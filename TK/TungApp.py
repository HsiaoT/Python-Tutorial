# coding=utf-8



import tkinter as tk
window = tk.Tk() # 如果使用直譯器的話，在這行Enter後就會先看到一個視窗了！
window.title('Title') # 更改視窗的標題
window.geometry('800x400') # 修改視窗大小(寬x高)
window.resizable(False, False) # 如果不想讓使用者能調整視窗大小的話就均設為False

frame1 = tk.Frame(window, bg='red', width=800, height=100)
frame1.pack() # 設定Frame的排版方法，這行完成後才會在視窗上顯現




# =============================================
# =================== Label ===================
# =============================================
label1 = tk.Label(window, text='URL', bg='green', font=('Arial', 12), width=30, height=2)
label1.pack()    # Label內容content區域放置位置，自動調節尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place()

# =============================================
# =================== Entry ===================
# =============================================
e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 顯示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 顯示成明文形式
e1.pack()
e2.pack()

# =============================================
# =================== Button ==================
# =============================================

def webCrawler():
	btnstr.set('Web Crawler ing...')

btnstr = tk.StringVar() # 初始化tk的字串變數
btnstr.set('Web Crawler')
btn = tk.Button(window, bg='violet', fg='white', textvariable=btnstr, command=webCrawler)
btn.pack()


















window.mainloop() # 在一般python xxx.py的執行方式中，呼叫mainloop()才算正式啟動