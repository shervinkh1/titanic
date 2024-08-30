# طریقه اجرای پروژه بر روی دستگاه خود

## راه اندازی پیش نیاز های اولیه

1: پروژه را بر روی دستگاه خود کلون کنید 

```
git clone https://github.com/shervinkh1/titanic.git
```

2: محیط مجازی را بر روی دستگاه خود بسازید برای ایزوله کردن پروژه (از قبل برای شما نصب باشد virtualenv دقت کنید که پکیج)  ``virtualenv venv``

3: فعال کردن محیط مجازی 

- اگر سیستم عامل شما ویندوز است : ``source venv/bin/activate``
- اگر سیستم عامل شما لینوکس یا مک است : ``. venv/bin/activate``

## نصب پکیج ها

4. نصب کردن پکیج هایی که برای اجرای پروژه به آنها نیاز دارید 

```
pip install -r requirements.txt
```

## پیکربندی پایگاه داده

### تنظیمات پایگاه داده را در titanic_app/settings.py به‌روزرسانی کنید. برای مثال، برای PostgreSQL:

```
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
```

## پایگاه داده

5: ساخت مایگریشن داده بر اساس دیتا ها و مایگریشن های اولیه

```
python manage.py makemigrations
```

6: ساخت پایگاه داده 

```
python manage.py migrate
```

## استفاده و اجرای پروژه

7: پس از ساخت پایگاه داده میتوانید پروژه را بر اساس دستور های زیر اجرا کنید 

- روی هاست دستگاه 

```
python manage.py runserver
```

- روی هاست دستگاه و همچنین روی آدرس آی پی دستگاه  ``python manage.py runserver 0.0.0.0:8000``


