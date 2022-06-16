import subprocess, os
from time import sleep
from tkinter import filedialog, messagebox
import tkinter as tk
pyPath = ''
ico = ''
window = tk.Tk()
window.geometry('600x400')
window.title('Py To Exe converter by IlProgrammatore.py and Gianluca Veronese')
Trascina = tk.Label(window,text='Trascina qui il tuo file python')
Trascina.grid(row=0,column=0,sticky='WN',padx=20,pady=20)
#Piccola cosa estetica e per comodita

def Get_Py():
    global pyPath
    while True:
        pyPath = filedialog.askopenfilename( 
            defaultextension=".txt",
            filetypes=[("Script Python", "*.py"),])
        if pyPath!='':
            Trascina = tk.Label(window,text=f'Trascina qui il tuo file python\n{pyPath}')
            Trascina.grid(row=0,column=0,sticky='WN',padx=20,pady=20)
            break
Py = tk.Button(text='Scegli il file.py',command=Get_Py)
Py.grid(row=1,column=0,sticky='WN',padx=50,pady=20)

def Get_Ico():
    global ico
    while True:
        ico =filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Icona", "*.ico"),])
        if ico!='':
            ICO = tk.Label(window,text=f'Trascina qui il tuo file ico\n{ico}')
            ICO.grid(row=0,column=0,sticky='WN',padx=200,pady=20)
            break
ICO = tk.Label(window,text=f'Trascina qui il tuo file ico')
ICO.grid(row=0,column=0,sticky='WN',padx=200,pady=20)
ICO_B = tk.Button(text='Scegli il file.ico',command=Get_Ico)
ICO_B.grid(row=1,column=0,sticky='WN',padx=220,pady=20)
def Convert():
    global pyPath, ico
    if pyPath!='' and ico!='':
        while True:
            risposta = subprocess.run(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile', shell=False, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            dati= risposta.stdout + risposta.stderr
            if 'deined' not in dati.decode():
                box_title = "Exe creato con successo"
                box_message = "Troverai il tuo file nella cartella dist!"
                messagebox.showinfo(box_title, box_message) # É input perchè altrimenti non si leggeva l'output
                break
            else:
                print('Prolemi di permesso probabilmente antivirus')
Py = tk.Button(text='Converti',command=Convert)
Py.grid(row=2,column=0,sticky='WN',padx=150,pady=20)
# os dava prolemi di permesso
sleep(0.2)
# shutil.rmtree("build") è inutile
window.mainloop()
