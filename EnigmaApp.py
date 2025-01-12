import tkinter as tk
import pyperclip, os, sys
import Thonigma

app = tk.Tk()
EnigmaMachine = Thonigma.EnigmaMachine(rotor1_pos=0, rotor2_pos=1, rotor3_pos=2)

common_font = ("Arial", 10)
# Apply the common font to all Label, Entry, and Button widgets
app.option_add("*Label.Font", common_font)
app.option_add("*Entry.Font", common_font)
app.option_add("*Button.Font", common_font)

def crypt():
    ent3.delete(0, tk.END)
    ent3.insert(0, EnigmaMachine.run_emulator(sentence=ent1.get(), cmd="crypt"))
def decrypt():
    ent4.delete(0, tk.END)
    ent4.insert(0, EnigmaMachine.run_emulator(sentence=ent2.get(), cmd="decrypt"))

def copy_crypt():
    pyperclip.copy(ent3.get())
def copy_decrypt():
    pyperclip.copy(ent4.get())

def copyInit():
    import pyperclip
    bu3 = tk.Button(app, text="Copy", command=copy_crypt)
    bu3.place(x=85, y=325)
    bu4 = tk.Button(app, text="Copy", command=copy_decrypt)
    bu4.place(x=385, y=325)

def change_theme():
    if bu_theme.cget("text") == "☀":
        app.config(bg="SystemButtonFace")
        bu_theme.config(text="🌙")
    else:
        app.config(bg="black")
        bu_theme.config(text="☀")

def validate_input(input_):
    return input_.isdigit() or input_ == ""

def modify_engine():
    if int(edit_ent1.get()) <= 26 and int(edit_ent2.get()) <= 26 and int(edit_ent3.get()) <= 26:
        EnigmaMachine = Thonigma.EnigmaMachine(rotor1_pos=int(edit_ent1.get()), rotor2_pos=int(edit_ent2.get()), rotor3_pos=int(edit_ent3.get()))
    else:
        print(":(")

def editEngine():
    edit = tk.Tk()
    edit.title("Edit Enigma Machine")
    edit.geometry("500x500")
    vcmd = (edit.register(validate_input), '%P')

    global edit_ent1, edit_ent2, edit_ent3
    edit_lab1 = tk.Label(edit, text="Rotor 1 start pos:")
    edit_lab1.pack()
    edit_ent1 = tk.Entry(edit, validate="key", validatecommand=vcmd)
    edit_ent1.pack()
    edit_lab2 = tk.Label(edit, text="Rotor 2 start pos:")
    edit_lab2.pack()
    edit_ent2 = tk.Entry(edit, validate="key", validatecommand=vcmd)
    edit_ent2.pack()
    edit_lab3 = tk.Label(edit, text="Rotor 3 start pos:")
    edit_lab3.pack()
    edit_ent3 = tk.Entry(edit, validate="key", validatecommand=vcmd)
    edit_ent3.pack()
    edit_bu1 = tk.Button(edit, text="Send", command=modify_engine)
    edit_bu1.pack()

def appli():
    app.title("Enigma Machine")
    app.geometry("500x500")

    lab1 = tk.Label(app, text="Enigma Machine", font=("Arial", 20))
    lab1.pack()
    bu_rotors = tk.Button(app, text="Edit Enigma Machine", command=editEngine)
    bu_rotors.pack()

    lab2 = tk.Label(app, text="Crypt")
    lab2.place(x=85, y=100)
    lab3 = tk.Label(app, text="Decrypt")
    lab3.place(x=375, y=100)

    lab4 = tk.Label(app, text="Entre une phrase")
    lab4.place(x=55, y=150)
    lab5 = tk.Label(app, text="Entre une phrase")
    lab5.place(x=355, y=150)

    global ent1, ent2, ent3, ent4, bu_theme
    ent1 = tk.Entry(app)
    ent1.place(x=40, y=200)
    ent2 = tk.Entry(app)
    ent2.place(x=340, y=200)

    bu1 = tk.Button(app, text="Crypter", command=crypt)
    bu1.place(x=80, y=250)
    bu2 = tk.Button(app, text="Decrypter", command=decrypt)
    bu2.place(x=375, y=250)

    ent3 = tk.Entry(app)
    ent3.insert(0, "Le résultat va être ici !")
    ent3.place(x=40, y=300)
    ent4 = tk.Entry(app)
    ent4.insert(0, "Le résultat va être ici !")
    ent4.place(x=340, y=300)

    question = input("Voulez vous activer le protocole de copie du texte ? Oui/Non: ")
    if question.upper() == "OUI":
        os.system(f"{sys.executable} -m pip install pyperclip")
        copyInit()

    bu_theme = tk.Button(app, text="🌙", command=change_theme)
    bu_theme.place(x=450, y=5)

    lab_version = tk.Label(app, text="App by Thony3ds App version: V1.0.\nEncryption core version: ThonigmaCore V1.0")
    lab_version.place(x=140, y=450)

    app.mainloop()

if __name__ == '__main__':
    appli()