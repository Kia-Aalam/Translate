import tkinter as tk
from deep_translator import GoogleTranslator

def translate() : # Translate
    input_text = text_entry.get().strip()
    if input_text.isascii() :
      translated = GoogleTranslator(source = 'en' , target = 'fa').translate(input_text)
    else :
        translated = GoogleTranslator(source = 'fa' , target = 'en').translate(input_text)
    lbl_show.config(text = translated)
      

def close() : # Close Button
    window.destroy()

window = tk.Tk()
window.title("Translate")
window.geometry("300x200")
window.resizable(0 , 0)

window.iconbitmap("icon.ico")

string_var = tk.StringVar()
text_entry = tk.Entry(window , width = 20 , justify = "center" , textvariable = string_var)
text_entry.pack()

lbl_show = tk.Label(window , height = 5 , text = " ")
lbl_show.pack()

btn_translate = tk.Button(window , text = "Translate" , font = ("Arial" , 12) , relief = "raised" , command = translate)
btn_translate.pack()

btn_close = tk.Button(window , text = "Close" , font = ("Arial" , 12) , relief = "raised" , command = close)
btn_close.pack()

window.mainloop()