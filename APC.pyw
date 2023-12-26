import tkinter as tk

def calculate_time_and_rate(event=None):
    cadr_value = float(entry_cadr.get())
    room_volume = float(entry_volume.get())

    time_required = room_volume / cadr_value * 60
    air_changes_per_hour = 60 / time_required

    result_label.config(text=f"换气一遍所需时间：{time_required:.2f} 分钟\n每小时换气次数：{air_changes_per_hour:.2f} 次")

def calculate_cadr(event=None):
    room_volume = float(entry_volume_cadr.get())
    air_changes_per_hour = float(entry_changes_per_hour.get())

    cadr_value = room_volume * air_changes_per_hour

    result_label_cadr.config(text=f"所需CADR值：{cadr_value:.2f} m³/h")

root = tk.Tk()
root.title("空净计算器")

window_width = 300
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

label_cadr = tk.Label(root, text="CADR值（m³/h）:")
label_cadr.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_cadr = tk.Entry(root)
entry_cadr.grid(row=0, column=1, padx=10, pady=10)
entry_cadr.bind('<Return>', calculate_time_and_rate)

label_volume = tk.Label(root, text="空间体积（m³）:")
label_volume.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_volume = tk.Entry(root)
entry_volume.grid(row=1, column=1, padx=10, pady=10)
entry_volume.bind('<Return>', calculate_time_and_rate)

calculate_button = tk.Button(root, text="计算换气时间和次数", command=calculate_time_and_rate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

label_volume_cadr = tk.Label(root, text="空间体积（m³）:")
label_volume_cadr.grid(row=4, column=0, padx=10, pady=10, sticky="e")

entry_volume_cadr = tk.Entry(root)
entry_volume_cadr.grid(row=4, column=1, padx=10, pady=10)
entry_volume_cadr.bind('<Return>', calculate_cadr)

label_changes_per_hour = tk.Label(root, text="每小时换气次数:")
label_changes_per_hour.grid(row=5, column=0, padx=10, pady=10, sticky="e")

entry_changes_per_hour = tk.Entry(root)
entry_changes_per_hour.grid(row=5, column=1, padx=10, pady=10)
entry_changes_per_hour.bind('<Return>', calculate_cadr)

calculate_button_cadr = tk.Button(root, text="计算所需CADR值", command=calculate_cadr)
calculate_button_cadr.grid(row=6, column=0, columnspan=2, pady=10)

result_label_cadr = tk.Label(root, text="")
result_label_cadr.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
