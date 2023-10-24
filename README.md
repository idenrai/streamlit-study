# streamlit-study

## 환경설정

### 파이썬 설치 및 가상환경 만들기

```terminal
pyenv install 3.11.6
python local 3.11.6
pyenv virtualenv 3.11.6 sl-venv
pyenv activate sl-venv
pip install --upgrade pip
```

### Streamlit 설치

```terminal
pip install streamlit
```

### Package Install

```terminal
pip install -r requirements.txt
```

## 실행

```terminal
streamlit run app.py
```

## Package

패키지를 추가할 경우, 이하 커맨드를 실행할 것

pip freeze > requirements.txt
