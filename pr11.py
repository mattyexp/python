import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Калькулятор
def calculator():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    action = operator_memory.get()

    result = 0

    if action == '+':
        result = num1 + num2
    elif action == '-':
        result = num1 - num2
    elif action == '*':
        result = num1 * num2
    elif action == '/':
        if num2 == 0:
            result_label.config(text="Ошибка: деление на ноль")
            return
        else:
            result = num1 / num2
    result_label.config(text=f"Результат: {result}")

# Чекбокс
def show_selection():
    selected = []
    if check1_memory.get():
        selected.append("первый")
    if check2_memory.get():
        selected.append("второй")
    if check3_memory.get():
        selected.append("третий")

    if selected:
        msg = f"Вы выбрали: {', '.join(selected)}"
        messagebox.showinfo("Ваш выбор", msg)
    else:
        messagebox.showinfo("Ваш выбор", "Ничего не выбрано")

# Загрузить текст из файла
def text_from_file():
    selectedfile = filedialog.askopenfilename(
        initialdir=".",
        title="Выберите текстовой файл"
    )
    if not selectedfile:
        return

    with open(selectedfile, "r", encoding="utf-8") as file:
        text = file.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, text)

# Окно
root = tk.Tk()
root.title("Мацаев Дмитрий Романович")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(pady=20, padx=20, fill="both", expand=True)

tab1 = ttk.Frame(notebook, padding="10")
tab2 = ttk.Frame(notebook, padding="10")
tab3 = ttk.Frame(notebook, padding="10")

notebook.add(tab1, text='Калькулятор')
notebook.add(tab2, text='Чекбокс')
notebook.add(tab3, text='Текст')

# Вкладка "Калькулятор"
entry_font = ('Arial', 14)
button_font = ('Arial', 12)

num1_entry = tk.Entry(tab1, font=entry_font, width=10)
num1_entry.grid(row=0, column=0, padx=10, pady=10)

operator_memory = tk.StringVar()
operator_combobox = ttk.Combobox(tab1, textvariable=operator_memory, values=['+', '-', '*', '/'], width=5, state="readonly")
operator_combobox.grid(row=0, column=1, padx=10, pady=10)
operator_combobox.set('+')

num2_entry = tk.Entry(tab1, font=entry_font, width=10)
num2_entry.grid(row=0, column=2, padx=10, pady=10)

calculate_button = tk.Button(tab1, text="=", command=calculator, font=button_font)
calculate_button.grid(row=0, column=3, padx=10, pady=10)

result_label = tk.Label(tab1, text="Результат: ", font=entry_font)
result_label.grid(row=1, column=0, columnspan=4, pady=20)

# Вкладка "Чекбокс"
check1_memory = tk.BooleanVar()
check2_memory = tk.BooleanVar()
check3_memory = tk.BooleanVar()

check1 = tk.Checkbutton(tab2, text="Первый", variable=check1_memory, font=('Arial', 12))
check1.pack(pady=10, anchor='w')

check2 = tk.Checkbutton(tab2, text="Второй", variable=check2_memory, font=('Arial', 12))
check2.pack(pady=10, anchor='w')

check3 = tk.Checkbutton(tab2, text="Третий", variable=check3_memory, font=('Arial', 12))
check3.pack(pady=10, anchor='w')

check_button = tk.Button(tab2, text="Показать выбор", command=show_selection, font=('Arial', 12))
check_button.pack(pady=20)

# Вкладка "Текст"
menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Загрузить файл", command=text_from_file)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)

text_widget = tk.Text(tab3, wrap="word", font=('Arial', 12))
text_widget.pack(pady=10, padx=10, fill="both", expand=True) 

root.mainloop()
