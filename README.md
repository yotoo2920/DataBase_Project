
## Installing a new developing environment:

> Be sure to have all prerequisites.

1. Clone git repository
`$ git clone https://github.com/yotoo2920/DataBase_Project.git`

2. Change into the directory
`$ cd DataBase_Project`

3. Create virtual enviroment
`$ python3 -m venv myvenv`

4. Activate virtual environtment
`$ source myvenv/bin/activate`

5. Install requirements
`(myvenv) $ pip install -r requirements.txt`

6. Create database path
`(myvenv) $ mkdir data`

7. Setup database
`(myvenv) $ python manage.py migrate`

8. Load initial data
`(myvenv) $ python manage.py loaddata initial-data.json`

9. Start the web server!
`(myvenv) $ python manage.py runserver`

### Prerequisites

- Supported Operating Systems:
  - Ubuntu Linux 16.04
  
- Needed Packages:
  - python3-venv
