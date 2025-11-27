import tkinter as tk
from tkinter import messagebox
import requests
import json

def getdata():
    repo_name = repo_entry.get().strip()
    if not repo_name:
        messagebox.showwarning("Ошибка", "Введите полное имя репозитория (пр. Automattic/wp-calypso)")
        return

    parts = repo_name.split('/')
    owner = parts[0]
    repo = parts[1]

    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    repo_response = requests.get(repo_url)
    repo_data = repo_response.json()

    owner_login = repo_data['owner']['login']
    user_url = f"https://api.github.com/users/{owner_login}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    filter_info = {
        'company': user_data.get('company'),
        'created_at': user_data.get('created_at'),
        'email': user_data.get('email'),
        'id': user_data.get('id'),
        'name': user_data.get('name'),
        'url': user_data.get('url')
    }

    output_file = f"{owner_login}_user_info.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filter_info, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Успешно", f"Данные успешно сохранены в файл: {output_file}")

# Окно
root = tk.Tk()
root.title("GitHub user info")
root.geometry("400x150")

info_label = tk.Label(root, text="Введите полное имя репозитория (пр. Automattic/wp-calypso):", font=('Arial', 10))
info_label.pack(pady=10)

repo_entry = tk.Entry(root, width=50, font=('Arial', 12))
repo_entry.pack(pady=5)

getdata_button = tk.Button(root, text="Получить информацию", command=getdata, font=('Arial', 12))
getdata_button.pack(pady=10)

root.mainloop()