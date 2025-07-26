import tkinter as tk
import time

#定义更新时钟
def update_time():
    week_map = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期日'
    }
    week_en = time.strftime('%A')
    week_cn = week_map.get(week_en, week_en)
    time_str = time.strftime('%H∶%M∶%S')
    date_str = time.strftime('%Y年%m月%d日，') + week_cn
    label_time.config(text=time_str)
    label_date.config(text=date_str)
    root.after(150, update_time)

#定义移动
def start_move(event):
    global x_offset, y_offset, win_x, win_y
    x_offset = event.x_root
    y_offset = event.y_root
    win_x = root.winfo_x()
    win_y = root.winfo_y()

def do_move(event):
    x = win_x + (event.x_root - x_offset)
    y = win_y + (event.y_root - y_offset)
    root.geometry(f"450x200+{x}+{y}")

#创建主窗口
root = tk.Tk()
root.title("Clock")  #名称
root.overrideredirect(True)  # 无边框
root.attributes('-topmost', True)  # 置顶
root.attributes('-alpha', 0.95)  # 设置透明度
root.geometry("450x200+1420+795")  # 大小和位置（适用于1080P）

main_frame = tk.Frame(root, bg='#199CF7')
main_frame.pack(fill='both', expand=True)

# 标签填满Frame
label_time = tk.Label(main_frame, font=('微软雅黑 Light', 48), fg='white', bg='#199CF7', justify='left', anchor='w')
label_time.pack(fill='x', padx=35, pady=(30,0), anchor='w')
label_date = tk.Label(main_frame, font=('微软雅黑 Light', 22), fg='white', bg='#199CF7', justify='left', anchor='w')
label_date.pack(fill='x', padx=35, pady=(0,20), anchor='w')

#绑定移动
label_time.bind('<Button-1>', start_move) 
label_time.bind('<B1-Motion>', do_move)
label_date.bind('<Button-1>', start_move)
label_date.bind('<B1-Motion>', do_move)
root.bind('<Button-1>', start_move)
root.bind('<B1-Motion>', do_move)

update_time()
root.mainloop()