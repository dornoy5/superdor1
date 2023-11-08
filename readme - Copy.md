pip install

pip uninstall

pip freeze >requirements.txt
pip uninstall -r requirements.txt

######################  git  #####################
גיט חדש
echo "# repository name" >> README.md
git init
git add .
git commit -m "commit name"
git branch -M main
git remote
git push -u origin main

git clone ...

לגיט קיים
git remote add origin / git add .
git commit -M "sec"
git push

git commit -m "all files"
git commit -m "update קובץ ספציפי "

######################  virtual env  #####################
py -m virtualenv env
env\Scripts\activate

######################  clali  #####################
cd+ למעבר לתיקיה -שם התקייה
cd..למעבר לתיקיה קודמת 

dir -איזה קבצים יש בתקייה
mkdir + יצירת תיקייה -שם התיקיה
echo "">+ יצירת קובץ- שם הקובץ

py -m pydoc os>help.txt  עזרה לגבי מודול\פקאג'\קלאסים\פונקציות, או אס מודול במקרה הזה ,
ניתן לשנות לקבלת עזרה לגבי מודול אחר ויצירת קובץ טקסט

py -m pydoc -p 4000

py -m pydoc -w <שם הקובץ ללא סיומת>

######################  flask  #####################
flask run
flask --debug run
py app.py

######################  django  #####################
#Install django and create project#

pip install django
django-admin startproject myproj .    (the dot is part of the command)
django-admin startapp base	(create application)
py manage.py runserver  (run the server)

#Migration -create the tables#

py manage.py makemigrations
py manage.py migrate  
py manage.py createsuperuser (dor123->123)

#Create super user#
py manage.py createsuperuser

#Rest api framework#
pip install djangorestframework

#Install pillow# להעלאת תמונה
pip install pillow

#axios#
<script src="https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"></script>

#serialize#
pip install djangorestframework
