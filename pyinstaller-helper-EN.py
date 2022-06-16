import subprocess, os
from time import sleep
from tkinter import filedialog, messagebox
import tkinter as tk
pyPath = ''
ico = ''
window = tk.Tk()
window.geometry('600x400')
window.title('Py To Exe converter by IlProgrammatore.py and Gianluca Veronese')
Trascina = tk.Label(window,text='Drop here your python file')
Trascina.grid(row=0,column=0,sticky='WN',padx=20,pady=20)
#Piccola cosa estetica e per comodita

def Get_Py():
    global pyPath
    while True:
        pyPath = filedialog.askopenfilename( 
            defaultextension=".txt",
            filetypes=[("Script Python", "*.py"),])
        if pyPath!='':
            Trascina = tk.Label(window,text=f'Drop here your python file\n{pyPath}')
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
            ICO = tk.Label(window,text=f'Drop here your ico file\n{ico}')
            ICO.grid(row=0,column=0,sticky='WN',padx=200,pady=20)
            break
ICO = tk.Label(window,text=f'Drop here your ico file')
ICO.grid(row=0,column=0,sticky='WN',padx=200,pady=20)
ICO_B = tk.Button(text='Select your file.ico',command=Get_Ico)
ICO_B.grid(row=1,column=0,sticky='WN',padx=220,pady=20)
def Convert():
    global pyPath, ico
    if pyPath!='' and ico!='':
        while True:
            risposta = subprocess.run(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile', shell=False, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            dati= risposta.stdout + risposta.stderr
            if 'deined' not in dati.decode():
                box_title = "Exe created!"
                box_message = "You will find your file in the dist folder!"
                messagebox.showinfo(box_title, box_message)
                break
            else:
                print('Permission error, disable your antivirus!')
Py = tk.Button(text='Convert',command=Convert)
Py.grid(row=2,column=0,sticky='WN',padx=150,pady=20)
sleep(0.2)
# shutil.rmtree("build") is useless and wont work in this case
window.mainloop()
