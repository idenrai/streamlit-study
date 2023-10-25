# streamlit-study

## 환경설정

### 파이썬 설치 및 가상환경 만들기

```terminal
brew update && brew upgrade pyenv
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
streamlit run ./streamlit/Home.py
```

### 페이지 설명

- LearnAPI
  - 기본적인 사용법 습득
- Selectbox
  - selectbox를 이용한 Dataframe 필터링
- Filter
  - Dataframe with filter (multiselect, radio, slider, button)
- Plot
  - Plotly Chart
- Map
  - 지도 표시

## Package

패키지를 추가할 경우, 이하 커맨드를 실행할 것

```terminal
pip freeze > requirements.txt
```
