# Wanted-is-all-you-need
 - 이력서 양식 변환 서비스

![BDIA_Benner](https://github.com/ETTE154/Wanted-is-all-you-need/assets/109407983/6a711052-85b9-487c-8529-c27d6057bbc4)


***
# 소개

## 목적
  이력서를 작성하다 보면 여러 구인 구직 플랫폼에서 요구하는 이력서의 양식이 서로 상이 하여 같은 내용의 이력서를 여러 번 작성해야 하는 번거로움이 있다. 때문에 본 프로젝트는 **타 플랫폼** 에서 작성된 이력서를 불러와서 **Wanted**의 이력서로 변환 하는 것을 목표로 한다.
 
---
## 구현 방법
### 프론트엔드
- web기반 서비스를 목표로 하며 `streamlit` 을 통해 구현 한다.
- `reportlab` 을 활용한 PDF 형태로 다운로드를 받을 수 있는 서비스를 제공
### 백엔드
- 🦜️🔗`langchain` 프레임워크를 활용하여 아키텍쳐를 구성하고, llm의 경우 **gpt-3.5-turbo** 모델을 사용합니다.
- **Wanted**의 이력서 카테고리에 맞게 타 플랫폼의 이력서 데이터를 분류하는 프롬프트 엔지니어링을 작성합니다.
- `reportlab` 을 기반으로 PDF 형태의 이력서를 자동 생성 합니다.
### 아키텍처
![image](https://github.com/ETTE154/Wanted-is-all-you-need/assets/109407983/8a9a850a-0726-4643-995d-3c38bbdf1832)

1. 타 플랫폼의 PDF 형태의 이력서를 입력으로 받습니다.
2. 이력서에서 원시 텍스트 데이터를 추출하고, 각 카테고리별로 데이터를 분류하여 저장합니다.
3. 분류된 데이터를 llm을 이용하여 이력서 내용을 작성합니다.
4. 작성된 데이터를 `reportlab`을 이용해 PDF 형태의 이력서로 변환합니다.

### 프롬프트 엔지니어링
- [Prompt_Engineering.md](https://github.com/ETTE154/Wanted-is-all-you-need/blob/main/Prompt_Engineering.md) 에서 자세한 내용을 확인할 수 있습니다.

## 실행방법

### 필수 조건

- ubuntu 22.04.3
- Python 3.10.12 or higher
- Streamlit
- LangChain
- OpenAI API key

### 실행 단계

1. 깃허브의 레포지토리를 복제 합니다.
2. 필요한 Python 패키지를 `pip install -r requirements.txt` 명령어를 통해 설치합니다.
3. OpenAI API 키에 대한 환경 변수를 설정합니다.(env.template -> .env)
4. `streamlit run run.py` 명령어를 사용하여 Streamlit 앱을 실행합니다.

### Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wanted.streamlit.app/)
