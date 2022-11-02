# QRkot_spreadseets

### Описание
Сервис сбора пожертвований на различные целевые проекты для поддержки котиков. Добавлена возможность формирования отчёта в гугл-таблице

**Проекты**  
У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.

**Пожертвования**  
Пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

**Пользователи**  
- Целевые проекты создаются администраторами сайта.
- Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
- Любой пользователь может видеть список всех проектов.

Примеры запросов к API, варианты ответов и ошибок приведены в документации проекта, доступной по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Технологии
- Python 3.9.13
- FastAPI 0.78.0

### Шаблон наполнения файла `QRkot_spreadsheets/.env`
```
APP_TITLE=Приложение QRKot
APP_DESCRIPTION=Сервис сбора пожертвований для поддержки котиков.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secret
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
TYPE=service_account
PROJECT_ID=your_projectid
PRIVATE_KEY_ID=your_private_key
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----your_private_key-----END PRIVATE KEY-----
CLIENT_EMAIL=client@your_projectid.iam.gserviceaccount.com
CLIENT_ID=123456789012345678901
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/client%40your_projectid=.iam.gserviceaccount.com
EMAIL=your@gmail.com
```

### Запуск проекта
- Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://github.com/niktere12321/QRkot_spreadsheets.git
```
```
cd QRkot_spreadsheets
```
- Установите и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Запустите проект командой:
```
uvicorn app.main:app --reload
```

### Автор
Терехов Никита Алексеевич
