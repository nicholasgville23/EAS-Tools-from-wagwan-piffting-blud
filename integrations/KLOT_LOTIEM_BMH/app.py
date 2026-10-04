import json, tkinter as tk
from tkinter import ttk
from pathlib import Path
CFG=json.loads((Path(__file__).parent/'config.json').read_text(encoding='utf-8'))
root=tk.Tk(); root.title('KLOT | LOTIEM — EAS/BMH Laboratory Console'); root.geometry('900x500')
ttk.Label(root,text='KLOT | LOTIEM — EAS/BMH Laboratory Console',font=('Segoe UI',20,'bold')).pack(pady=20)
ttk.Label(root,text='SIMULATION ONLY — no EAS/SAME/RF/public transmission',foreground='dark orange').pack()
ttk.Label(root,text=f"Text Workstation: {CFG['text_workstation']['ip_address']}:{CFG['text_workstation']['port']}  |  WXK89: {CFG['bmh_station']['status']}").pack(pady=10)
frame=ttk.Frame(root); frame.pack(fill='both',expand=True,padx=30,pady=20)
for label in ['KLOT LOTIEM TEXT WORKSTATION','BMH Network','AWIPS Active Alerts - Unified','KLOT Polygon Tool','WarnGen / WatchGen']:
    ttk.Button(frame,text=label,command=lambda x=label: tk.messagebox.showinfo(x,'Open the full prototype package supplied with this integration.')).pack(fill='x',pady=4)
root.mainloop()
