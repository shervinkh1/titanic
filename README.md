## ایجاد محیط مجازی

### برای مدیریت وابستگی‌های پروژه، یک محیط مجازی ایجاد کنید:


>python -m venv venv
### محیط مجازی را فعال کنید:

### در ویندوز:


>venv\Scripts\activate
### در macOS/Linux:


>source venv/bin/activate
## نصب وابستگی‌ها

### با استفاده از pip وابستگی‌های مورد نیاز را نصب کنید:


>pip install -r requirements.txt
### اگر requirements.txt وجود ندارد، به صورت دستی وابستگی‌ها را نصب کنید:


>  pip install django psycopg2-binary openpyxl
## پیکربندی پایگاه داده

### تنظیمات پایگاه داده را در titanic_app/settings.py به‌روزرسانی کنید. برای مثال، برای PostgreSQL:

>python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
اجرای مایگریشن‌ها

برای راه‌اندازی ساختار پایگاه داده، مایگریشن‌ها را اجرا کنید:


>python manage.py migrate
ایجاد کاربر مدیر

برای دسترسی به پنل مدیریت Django، یک کاربر مدیر ایجاد کنید:


>python manage.py createsuperuser
اجرای سرور توسعه

سرور توسعه Django را راه‌اندازی کنید:

>python manage.py runserver
مرورگر خود را باز کنید و به http://127.0.0.1:8000/ بروید تا به اپلیکیشن دسترسی پیدا کنید.

