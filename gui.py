import tkinter as tk
from tkinter import IntVar, ttk
from tkinter.messagebox import showerror
from blowfish import Blowfish


root = tk.Tk()
root.title('Blowfish')
root.geometry('550x325')
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)

main_frame = ttk.Frame(root)
padding = {'padx': 5, 'pady': 5}

txt_label = ttk.Label(main_frame, text='Исходный текст:')
txt_label.grid(column=0, row=0, sticky='w', **padding)

key_label = ttk.Label(main_frame, text='Ключ шифрования:')
key_label.grid(column=0, row=1, sticky='w', **padding)

txt_input = tk.StringVar()
key_input = tk.StringVar()

txt_entry = tk.Text(main_frame, height=3, width=45)
txt_entry.grid(column=1, row=0, **padding)
txt_entry.focus()
key_entry = tk.Text(main_frame, height=3, width=45)
key_entry.grid(column=1, row=1, **padding)

def retrieve_txt():
    txt = txt_entry.get('1.0','end-1c')
    return txt

def retrieve_key():
    key = key_entry.get('1.0','end-1c')
    return key

def clear_btn_clicked():
    txt_entry.delete('1.0','end')
    output_txt.delete('1.0','end')
    key_entry.delete('1.0','end')

def encrypt_btn_clicked():
    try:
        output_txt.delete('1.0','end')
        txt = retrieve_txt()
        key = retrieve_key()
        cipher_txt = Blowfish(txt, key)
        if chk.get() == 1:
            cipher_txt.decrypt()
            output_txt.insert('1.0', cipher_txt.decrypted_txt)
        else:
            cipher_txt.encrypt()
            output_txt.insert('1.0', cipher_txt.encrypted_txt)

    except ValueError as error:
        showerror(title='Error', message=error)

def copy():
    try:
        root.clipboard_clear()
        root.clipboard_append(output_txt.get('1.0', 'end'))
    except:
        root.clipboard_append('Error')


chk = IntVar()
chk_btn = ttk.Checkbutton(main_frame, text="Расшифровка", variable=chk)
chk_btn.grid(column=0, row=3, sticky='wesn')

encrypt_btn = ttk.Button(main_frame, text='Раздуть рыбу')
encrypt_btn.grid(column=1, row=3, sticky='wesn', **padding)
encrypt_btn.configure(command=encrypt_btn_clicked)

output_label = ttk.Label(main_frame, text='Вывод:')
output_label.grid(column=0, row=4, sticky='w')
output_txt = tk.Text(main_frame, height=5, width=50)
output_txt.grid(column=0, row=5, rowspan=1, columnspan=2, sticky='wesn')

clear_btn = ttk.Button(main_frame, text="Очистить", command=clear_btn_clicked)
clear_btn.grid(column=0, row=8, columnspan=1, sticky='wesn', **padding)

copy_btn = ttk.Button(main_frame, text="Копировать", command=copy)
copy_btn.grid(column=1, row=8, columnspan=1, sticky='wesn', **padding)

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid(padx=10, pady=10)

root.mainloop()