import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x500")

def login():
    print("HEllo world")
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Arial",24))
label.pack(pady=12, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Password")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Rembr me")
checkbox.pack(pady=12,padx=10)

root.mainloop()