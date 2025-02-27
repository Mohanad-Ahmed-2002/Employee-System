import tkinter as tk
from login import LoginWindow
from EMS import AppWindow
import sys
import os

# تحقق إن كان التطبيق يعمل من ملف EXE (مجمع بـ PyInstaller)
if getattr(sys, 'frozen', False):
    # إذا كان مجمعًا كـ EXE، يتم تخزين الموارد في مجلد مؤقت يشير إليه sys._MEIPASS
    os.chdir(sys._MEIPASS)  # نغير الدليل العامل إلى المجلد المؤقت


os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    # أولاً، عرض نافذة تسجيل الدخول
    login_root = tk.Tk()  # إنشاء نافذة تسجيل الدخول بشكل صحيح
    login_app = LoginWindow(login_root)  # استخدام اسم الفئة الصحيح
    login_root.mainloop()
    
    if login_app.success:
        main_root = tk.Tk()  # إنشاء النافذة الرئيسية للتطبيق بشكل صحيح
        app = AppWindow(main_root)  # إنشاء مثيل من AppWindow
        main_root.mainloop()
    else:
        print("Login was not successful. Exiting the program.")
        