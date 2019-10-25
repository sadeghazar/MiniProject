# MiniProject
User Management API

# How to use this project
 

## Run it

in order to run project:

    cd ~/
    git clone https://github.com/sadeghazar/MiniProject.git
    cd ~/MiniProject
    sudo docker-compose up

## Login

before first request it should automatically create 'users' table in database
 default admin user is:
 **username = admin
 password = 123**

    curl --location --request POST "http://127.0.0.1:5000/login" \
    --header "Content-Type: multipart/form-data; boundary=--------------------------987843810823516316019456" \
    --form "username=admin" \
    --form "password=123"

sample response:

    {
    "message": "Logged in as admin",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5OTY3NjAsIm5iZiI6MTU3MTk5Njc2MCwianRpIjoiMzY3MjQ2ZjItNDcwNy00MzA3LTgxZTQtNDY5ZjJkODk2OWRiIiwiZXhwIjoxNTcxOTk3NjYwLCJpZGVudGl0eSI6ImFkbWluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.GdciMkzYNvfG6oOlonsxF2G5BwJqfb2lx1o1cH57mT4",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5OTY3NjAsIm5iZiI6MTU3MTk5Njc2MCwianRpIjoiNzU0OWI4ZDctNjUyZS00ZTRmLThmZjYtMDhkNDI1ZTYyNmE2IiwiZXhwIjoxNTc0NTg4NzYwLCJpZGVudGl0eSI6ImFkbWluIiwidHlwZSI6InJlZnJlc2gifQ.674zzyx5f9CJPYogiexVXcAowAFh9uvqJuzaGtTzX4U"
    }

Copy access_token value and put it in every request header
for example:

    curl --location --request GET "http://127.0.0.1:5000/user/48" \
    --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5NTY4MzYsIm5iZiI6MTU3MTk1NjgzNiwianRpIjoiMWQyMDVjZTktNjM1ZS00ZjcxLTg4YjUtMTBlNDQ5MGI4Mjk5IiwiZXhwIjoxNTcxOTU3NzM2LCJpZGVudGl0eSI6IlNhZGVnaDEyMzQiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.hLVZTJalwEiIlE9OHCaw2v2W99Wng08rsePx8_Kmg1c"

## Endpoints
### Get user by id

    curl --location --request GET "http://127.0.0.1:5000/user/48" \
    --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5NTY4MzYsIm5iZiI6MTU3MTk1NjgzNiwianRpIjoiMWQyMDVjZTktNjM1ZS00ZjcxLTg4YjUtMTBlNDQ5MGI4Mjk5IiwiZXhwIjoxNTcxOTU3NzM2LCJpZGVudGl0eSI6IlNhZGVnaDEyMzQiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.hLVZTJalwEiIlE9OHCaw2v2W99Wng08rsePx8_Kmg1c"

### Create New User

    curl --location --request POST "http://127.0.0.1:5000/user" \
    --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5ODk5NTcsIm5iZiI6MTU3MTk4OTk1NywianRpIjoiOGYyNmYzMmEtM2FmNi00YTQwLTljOWUtMmE2MzBmMjk5OTIwIiwiZXhwIjoxNTcxOTkwODU3LCJpZGVudGl0eSI6ImFkbWluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.MmxJijfmXgwj5OOtNF_02rlR-ivxl2-PBfPdsTlCsck" \
    --header "Content-Type: multipart/form-data; boundary=--------------------------382353173572796149724746" \
    --form "username=msadegh" \
    --form "password=1234" \
    --form "first_name=sadegh" \
    --form "last_name=azarkaman" \
    --form "phone_number=093834342"

### Modify user

    curl --location --request PUT "http://127.0.0.1:5000/user/46" \
    --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5ODk5NTcsIm5iZiI6MTU3MTk4OTk1NywianRpIjoiOGYyNmYzMmEtM2FmNi00YTQwLTljOWUtMmE2MzBmMjk5OTIwIiwiZXhwIjoxNTcxOTkwODU3LCJpZGVudGl0eSI6ImFkbWluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.MmxJijfmXgwj5OOtNF_02rlR-ivxl2-PBfPdsTlCsck" \
    --header "Content-Type: multipart/form-data; boundary=--------------------------381364090129897866552550" \
    --form "first_name=sa" \
    --form "last_name=d" \
    --form "phone_number=d" \
    --form "birth_date=2019-10-24T15:43:24" \
    --form "username=asd" \
    --form "password=234"


### Delete user

    curl --location --request DELETE "http://127.0.0.1:5000/user/46" \
    --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE5ODk5NTcsIm5iZiI6MTU3MTk4OTk1NywianRpIjoiOGYyNmYzMmEtM2FmNi00YTQwLTljOWUtMmE2MzBmMjk5OTIwIiwiZXhwIjoxNTcxOTkwODU3LCJpZGVudGl0eSI6ImFkbWluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.MmxJijfmXgwj5OOtNF_02rlR-ivxl2-PBfPdsTlCsck"


## Run tests
in order to run tests use this command:

     sudo docker-compose run app sh -c "pytest -v"

## Run pgAdmin
After running docker-compose you can go to 
[http://localhost:5050](http://localhost:5050)
default credentials is:
**username = pgadmin4@pgadmin.org
password = admin**
After log in to panel add server and use '**db'** in hostname/address
**username=userpg
password=pass123**

