import tkinter as tk
from login import LoginWindow, BasicAuth
from EMS import AppWindow
from database import DatabaseManager  # استيراد قاعدة البيانات

if __name__ == "__main__":
    # إنشاء نافذة تسجيل الدخول
    login_root = tk.Tk()
    auth_strategy = BasicAuth()
    login_app = LoginWindow(login_root, auth_strategy)
    
    # تشغيل نافذة تسجيل الدخول
    login_root.mainloop()
    
    # التحقق من نجاح تسجيل الدخول
    if login_app.success:
        print("✅ Login successful! Opening main application...")

        # إنشاء نافذة التطبيق الرئيسي
        main_root = tk.Tk()
        
        # إنشاء كائن قاعدة البيانات وتمريره إلى AppWindow
        db = DatabaseManager()
        app = AppWindow(main_root, db)
        
        main_root.mainloop()
    else:
        print("❌ Login failed. Exiting program.")
