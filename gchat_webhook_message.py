from json import dumps
from httplib2 import Http
import tkinter as tk
import os

def send_message():
    url = gchat_url.get()
    bot_message = {
        'text' : message_text.get(),
        'thread' : {
            "name": gchat_thread.get()
        }
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    message_response.delete('1.0', tk.END)
    message_response.insert(tk.END, response)

bg_color = '#233f57'
fg_color = '#ffffff'

window = tk.Tk()
window.title("Send message to GChat WebHook")
window.config(background=bg_color)
window.geometry("600x535")
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

gchat_url_label = tk.Label(window, text="URL:", background=bg_color, foreground=fg_color, font="Helvetica 10 bold")
gchat_url_label.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

gchat_url = tk.Entry(window)
gchat_url.grid(row=0, column=1, sticky="nsew", padx=10, pady=10, columnspan=2)
gchat_url.insert(tk.END, os.getenv('GCHAT_WH_URL', ""))

gchat_thread_label = tk.Label(window, text="Thread:", background=bg_color, foreground=fg_color, font="Helvetica 10 bold")
gchat_thread_label.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

gchat_thread = tk.Entry(window)
gchat_thread.grid(row=1, column=1, sticky="nsew", padx=10, pady=10, columnspan=2)

message_label = tk.Label(window, text="Message:", background=bg_color, foreground=fg_color, font="Helvetica 10 bold")
message_label.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

message_text = tk.Entry(window)
message_text.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

message_send = tk.Button(window, text="Send", command=send_message)
message_send.grid(row=2, column=2, sticky="nsew", padx=10)

message_response = tk.Text(window)
message_response.grid(row=3, column=0, sticky="nsew", padx=10, pady=10, columnspan=3)

if __name__ == '__main__':
    window.mainloop()
