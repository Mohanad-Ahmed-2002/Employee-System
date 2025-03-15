import tkinter as tk
from login import LoginWindow,BasicAuth,EmailAuth
from EMS import AppWindow

if __name__ == "__main__":
    # أولاً، عرض نافذة تسجيل الدخول
    login_root = tk.Tk()  # إنشاء نافذة تسجيل الدخول بشكل صحيح
    auth_startegy = BasicAuth()
    login_app = LoginWindow(login_root,auth_startegy)  # استخدام اسم الفئة الصحيح
    login_root.mainloop()
    
    if login_app.success:
        main_root = tk.Tk()  # إنشاء النافذة الرئيسية للتطبيق بشكل صحيح
        app = AppWindow(main_root)  # إنشاء مثيل من AppWindow
        main_root.mainloop()
    else:
        print("Login was not successful. Exiting the program.")