## Prompt_Engineering

### 한줄소개
- `'''`으로 구분되는 여러줄 문자
1. 작성자는 무엇을 할 줄 아는가?(예시 : ~을 할줄아는 {name}입니다.)
2. 작성자는 무엇에 관심 있는가?(예시 : {skill} 에 관심이 많습니다.)
3. 작성자는 어떠한 경력이 있는가?(개조식으로 작성)

ex)
```
introduce = '''Next.js, TypeScript, React 기반의 5년차 프론트엔드 개발자 김티드입니다.

새로운 기술을 활용해 비즈니스 문제를 해결하는 것에 관심이 많습니다.

  

• 웹/앱 서비스의 프론트엔드 설계, 개발, 운영 경험

• 다수의 UI 구현 경험으로 사용자 인터렉션에 대한 높은 이해도

• 제한된 리소스 환경에서 기획 단계부터 참여한 프로젝트 다수

• 프로젝트 리딩 및 다양한 팀과의 협업 경험'''
```
### 경력
1. 작성자가 다녔던 회사는 어디인가?(ex: 삼성전자, LG전자)
	1. 결과값을 list로 저장
2. company[i]에서의 직책은?
3. company[i]에서의 기간(YYYY.MM ~ YYYY.MM)은?
4. company[i]에서의 진행한 프로젝트는(ex : Galaxy S20 UI 개발, Tizen OS 개발)
	1. 결과값을 list로 저장
5. project[j]의 세부내용은?
6. project[j]의 기간(YYYY.MM ~ YYYY.MM)은?


ex)
```
experience = [

{

"company": "삼성전자",

"position": "소프트웨어 엔지니어",

"duration": "2018.01 ~ 2021.01",

"projects": [

{

"name": "Galaxy S20 UI 개발",

"duration": "2019.05 ~ 2020.05",

"details": ["UI 구현", "사용자 인터랙션 개선"]

},

{

"name": "Tizen OS 개발",

"duration": "2018.02 ~ 2019.04",

"details": ["OS 최적화", "보안 패치 적용"]

}

]

},

{

"company": "LG전자",

"position": "데이터 과학자",

"duration": "2021.02 ~ 현재",

"projects": [

{

"name": "데이터 분석 플랫폼 구축",

"duration": "2021.02 ~ 현재",

"details": ["데이터 수집 및 처리", "분석 모델 구현"]

}

]

}

]
```
### 학력
- school_name, major, duration 을 포함하는 튜플구조
1. 작성자가 다녔던 학교명
	1. 리스트로 저장
2. school[i] 에서의 전공
3. school[i] 를 다닌 기간(YYYY.MM ~ YYYY.MM)
ex)
```
education = [

{

"school_name": "서울대학교",

"major": "컴퓨터공학과",

"duration": "2014.03 ~ 2018.02"

},

{

"school_name": "부산대학교",

"major": "전자공학과",

"duration": "2010.03 ~ 2014.02"

}

]
```
### 스킬
- 리스트 구조
1. 사용자의 기술스택을 나열하라(최대10개, 쉼표로 구분)
	1. 리스트로 저장
예시)
skills_list = ["React.js", "TypeScript", "JavaScript", "SASS", "CSS", "HTML", "Node.js", "JIRA", "Confluence"]
ex)
```
skills_list = ["React.js", "TypeScript", "JavaScript", "SASS", "CSS", "HTML", "Node.js", "JIRA", "Confluence"]
```
### 수상 및 기타
- type, details, date 를 포함하는 튜플 구조
수상 및 기타 또한 아래와 같은 질문 구조를 통해 결과를 얻고자 한다.
1. 작성자의 수상한 상 또는 수료한 교육은?(쉼표로 구분)
	1. awards_and_others[i] 의 날짜(YYYY.MM)는?
	2. awards_and_others[i] 의 세부 내용은?
예시)
awards_and_others = [

{

"type": "원티드 주관 해커톤 <해, 커리어> 1위 수상",

"details": "아티스트 공연 홍보/펀딩 위한 앱 서비스",

"date": "2018.03"

},

{

"type": "ABC 프론트엔드 교육 과정 이수",

"details": "",

"date": "2017.01"

}

]
```
awards_and_others = [

{

"type": "원티드 주관 해커톤 <해, 커리어> 1위 수상",

"details": "아티스트 공연 홍보/펀딩 위한 앱 서비스",

"date": "2018.03"

},

{

"type": "ABC 프론트엔드 교육 과정 이수",

"details": "",

"date": "2017.01"

}

]
```
### 외국어
languge, test, date, score 를 포함하는 튜플 구조
1. 작성자가 학습한 외국어는?(쉼표로 구분)
	1. 리스트로 저장
2. language[i] 의 평가를 위해 친 시험은?(단답형)
3. {test}의 성적은?(단답형)
4. {test}의 성적 취득일자는?(YYYY.MM)
결과)
language_data = [

{

"language": "영어",

"test": "토익",

"date": "2023.09",

"score": 750

}

]

```
language_data_sample = [

{

"language": "영어",

"test": "토익",

"date": "2023.09",

"score": 750

}

]
```
### 링크
- 리스트 구조
1. 이력서에서 제공되는 노션 및 깃허브의 링크는?(쉼표로 구분)
	1. 리스트로 저장

```
links_data_sample = [

"https://github.com/wanted",

"https://medium.com/wanted"

]
```
