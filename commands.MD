python3 -m venv name_environment #this creates the virtual environment

source name_environment/bin/activate #this activates the virtual environment

echo "# study-buddy" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/callistopan/study-buddy.git
git push -u origin masterRecursively remove all adjacent duplicates 

python manage.py makemigrations
python manage.py migrate  --set database