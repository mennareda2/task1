import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
import os
from playsound import playsound

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Text to Speech - Omar Abouelkheir")
root.geometry("500x300")

# الدوال الخاصة بالأزرار
def play_text():
    text = text_entry.get()  # الحصول على النص من الحقل
    if text:  # إذا كان هناك نص مدخل
        tts = gTTS(text=text, lang='ar')  # تحويل النص إلى كلام
        tts.save("output.mp3")  # حفظ الملف الصوتي
        playsound("output.mp3")  # تشغيل الملف الصوتي
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال النص!")  # تحذير في حال عدم وجود نص

def set_text():
    text_entry.delete(0, tk.END)  # مسح النص الموجود في الحقل

def save_text():
    text = text_entry.get()  # الحصول على النص
    if text:  # إذا كان النص موجودًا
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:  # إذا تم اختيار مكان الحفظ
            with open(file_path, "w", encoding="utf-8") as file:  # كتابة النص في الملف
                file.write(text)
            messagebox.showinfo("نجاح", "تم حفظ النص بنجاح!")  # رسالة نجاح
    else:
        messagebox.showwarning("تحذير", "لا يوجد نص لحفظه!")  # تحذير عند عدم وجود نص

def exit_app():
    root.destroy()  # إغلاق التطبيق

# تصميم الواجهة
tk.Label(root, text="أدخل النص:", font=("Arial", 14)).pack(pady=10)

# حقل إدخال النص
text_entry = tk.Entry(root, font=("Arial", 14), width=30)
text_entry.pack(pady=5)

# إطار يحتوي على الأزرار
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

# زر التشغيل (Play)
play_btn = tk.Button(btn_frame, text="تشغيل", bg="green", fg="white", font=("Arial", 12), command=play_text)
play_btn.grid(row=0, column=0, padx=10)

# زر المسح (Set)
set_btn = tk.Button(btn_frame, text="مسح", bg="blue", fg="white", font=("Arial", 12), command=set_text)
set_btn.grid(row=0, column=1, padx=10)

# زر الحفظ (Save)
save_btn = tk.Button(btn_frame, text="حفظ", bg="yellow", fg="black", font=("Arial", 12), command=save_text)
save_btn.grid(row=0, column=2, padx=10)

# زر الخروج (Exit)
exit_btn = tk.Button(btn_frame, text="خروج", bg="red", fg="white", font=("Arial", 12), command=exit_app)
exit_btn.grid(row=0, column=3, padx=10)

# تشغيل التطبيق
root.mainloop()