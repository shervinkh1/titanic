# views.py
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Titanic
from .forms import TitanicForm, ExcelUploadForm

# titanic_app/views.py


def upload_excel(request):
    if request.method == "POST":
        # دریافت فایل اکسل از درخواست
        uploaded_file = request.FILES.get('excel_file')
        
        if uploaded_file:
            # خواندن فایل اکسل به عنوان DataFrame
            try:
                df = pd.read_excel(uploaded_file)
                
                # چک کردن اینکه ستون 'PassengerId' در DataFrame وجود دارد
                required_columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Column '{col}' is missing from the uploaded file.")
                
                df['Survived'] = df['Survived'].map({0: False, 1: True})

                # ذخیره کردن هر ردیف به عنوان یک شیء Titanic
                for index, row in df.iterrows():
                    Titanic.objects.create(
                        passenger_id=row['PassengerId'],  # تغییر به حروف کوچک
                        survived=row['Survived'],
                        pclass=row['Pclass'],
                        name=row['Name'],
                        sex=row['Sex'],
                        age=row['Age'],
                        sibsp=row['SibSp'],
                        parch=row['Parch'],
                        ticket=row['Ticket'],
                        fare=row['Fare'],
                        cabin=row['Cabin'],
                        embarked=row['Embarked']
                    )
                
                messages.success(request, "Excel data uploaded successfully!")
                return redirect('upload_excel')
                
            except Exception as e:
                # بازگرداندن خطا در صورت بروز مشکل
                return render(request, 'upload_excel.html', {'error': str(e)})
        
    return render(request, 'upload_excel.html')

def manage_titanic(request):
    titanic_data = Titanic.objects.all().order_by('passenger_id')
    
    if request.method == 'POST':
        # اگر یک فرم جدید یا به روز رسانی ارسال شد
        form = TitanicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Titanic entry has been created/updated successfully!")
            return redirect('manage_titanic')
    else:
        form = TitanicForm()

    return render(request, 'manage_titanic.html', {'form': form, 'titanic_data': titanic_data})




def edit_titanic(request, pk):
    # دریافت رکورد تایتانیک مورد نظر
    entry = get_object_or_404(Titanic, pk=pk)
    
    # اگر درخواست POST باشد، فرم را با داده‌های جدید ذخیره کنید
    if request.method == 'POST':
        form = TitanicForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Titanic entry has been updated successfully!")
            return redirect('manage_titanic')
    else:
        # اگر درخواست GET باشد، فرم را با داده‌های جاری پر کنید
        form = TitanicForm(instance=entry)

    return render(request, 'edit_titanic.html', {'form': form, 'entry': entry})


def delete_titanic(request, pk):
    # حذف یک رکورد
    titanic_entry = get_object_or_404(Titanic, pk=pk)
    titanic_entry.delete()
    messages.success(request, "Entry deleted successfully!")
    return redirect('manage_titanic')


def titanic_data_grid(request):
    titanic_data = Titanic.objects.all()
    return render(request, 'titanic_data_grid.html', {'titanic_data': titanic_data})
