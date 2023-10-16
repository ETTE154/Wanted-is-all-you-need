# Wanted-is-all-you-need

# 이력서 양식 변환 서비스
[[BDIA DEV Contest]]
![BDIA_Benner](https://github.com/ETTE154/Wanted-is-all-you-need/assets/109407983/f47bdcb3-529e-4c56-bad2-07cec8f1c3db)
***
# 소개

## 목적
  이력서를 작성하다 보면 여러 구인 구직 플랫폼에서 요구하는 이력서의 양식이 서로 상이 하여 같은 내용의 이력서를 여러번 작성해야 하는 번거로움이 있다. 때문에 본 프로젝트는 **타 플랫폼** 에서 작성된 이력서를 불러와서 **Wanted**의 이력서로 변환 하는 것을 목표로 한다.
 
---
## 방법
### Front
- web기반 서비스를 목표로 하며 `streamlit` 을 통해 구현 한다.
- `reportlab` 을 활용한 PDF 형태로 다운로드를 받을 수 있는 서비스를 제공
### Back
- 🦜️🔗`langchain` 프레임워크를 활용하여 아키텍쳐를 구성하고, llm의 경우 **GPT** 모델을 사용
- 타 플랫폼의 이력서를 Wanted의 이력서 카테고리에 맞게 데이터를 분류할 프롬프트 엔지니어링 필요
- `reportlab` 기반한 PDF 형테의 이력서 자동화 
### Architecture
1. pdf 형태의 타 플랫폼 이력서를 입력을 받는다.
2. 이력서에서 rawtext 데이터를 추출하고, 각 category별로 데이터를 나누어 저장한다.
3. 카테고리 별로 분류된 데이터를 작성을 위한 llm을 이용해서 이력서의 내용을 작성한다. 
4. 작성된 데이터를 `reportlab` 를 활용하여 PDF형태의 이력서로 작성한다.

### Prompt_Engineering
- [Prompt_Engineering.md](https://github.com/ETTE154/Wanted-is-all-you-need/blob/main/Prompt_Engineering.md) 에서 기술
