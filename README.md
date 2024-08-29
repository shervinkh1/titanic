ایجاد محیط مجازی

برای مدیریت وابستگی‌های پروژه، یک محیط مجازی ایجاد کنید:

bash
Copy code
python -m venv venv
محیط مجازی را فعال کنید:

در ویندوز:

bash
Copy code
venv\Scripts\activate
در macOS/Linux:

bash
Copy code
source venv/bin/activate
نصب وابستگی‌ها

با استفاده از pip وابستگی‌های مورد نیاز را نصب کنید:

bash
Copy code
pip install -r requirements.txt
اگر requirements.txt وجود ندارد، به صورت دستی وابستگی‌ها را نصب کنید:

bash
Copy code
pip install django psycopg2-binary openpyxl
پیکربندی پایگاه داده

تنظیمات پایگاه داده را در titanic_app/settings.py به‌روزرسانی کنید. برای مثال، برای PostgreSQL:

python
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

bash
Copy code
python manage.py migrate
ایجاد کاربر مدیر

برای دسترسی به پنل مدیریت Django، یک کاربر مدیر ایجاد کنید:

bash
Copy code
python manage.py createsuperuser
اجرای سرور توسعه

سرور توسعه Django را راه‌اندازی کنید:

bash
Copy code
python manage.py runserver
مرورگر خود را باز کنید و به http://127.0.0.1:8000/ بروید تا به اپلیکیشن دسترسی پیدا کنید.

استفاده
آپلود فایل Excel

به صفحه آپلود Excel بروید و فایل Excel شامل داده‌های تایتانیک را آپلود کنید. فایل باید در فرمت .xlsx باشد.

مدیریت داده‌های تایتانیک

به صفحه مدیریت داده‌های تایتانیک بروید تا رکوردهای تایتانیک را مشاهده و ویرایش کنید. می‌توانید رکوردهای جدید اضافه کنید، رکوردهای موجود را ویرایش کنید یا حذف کنید.

مشاهده داده‌های تایتانیک

به صفحه مشاهده داده‌های تایتانیک بروید تا داده‌ها را به صورت جدولی مشاهده کنید. از فیلدهای جستجو برای فیلتر کردن داده‌ها بر اساس ستون‌های مختلف استفاده کنید.
