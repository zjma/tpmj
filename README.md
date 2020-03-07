## Dev Guide

### Get Started

#### Prerequisites

NOTE: use git bash if you are on Windows, or built-in terminal on unix-like system.

`python -V` to check python version. It should be 3.7.0 or higher.

`pip -V` to check pip version. It should be 20.0.2 or higher.

`pip install virtualenv` to install virtualenv.

`pip install pytest` to install pytest.

`node -v` to check nodejs version. It should be 12.14.0 or higher.

`npm -v` to check npm version. It should be 6.13.4 or higher.

#### API server

Go to backend folder.
```
cd backend
```

Create a virtualenv.
```
venvname=`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1`
virtualenv --no-site-packages /tmp/$venvname
. /tmp/$venvname/Scripts/activate
```

Install dependencies.
```
pip install -r requirements.txt
```

Run unittests.
```
pytest
```

Start API server locally.
```
python app/main.py
```
The default server URL should be `http://localhost:8080`.
This URL is needed to later start web client.

#### Web client

Go to webcli folder.
```
cd webcli
```

Install dependencies.
```
npm install
```

Run unittests.
```
npm test
```

Start web server locally.
```
npm run serve <api-server-url>
```
