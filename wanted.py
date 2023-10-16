#%%
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus import Flowable
from reportlab.lib.colors import black

from reportlab.platypus.tables import Table, TableStyle

# 글꼴 등록
pdfmetrics.registerFont(TTFont('SpoqaHanSansNeo-Regular', 'SpoqaHanSansNeo_TTF_original/SpoqaHanSansNeo-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SpoqaHanSansNeo-Bold', 'SpoqaHanSansNeo_TTF_original/SpoqaHanSansNeo-Bold.ttf'))
pdfmetrics.registerFont(TTFont('SpoqaHanSansNeo-Thin', 'SpoqaHanSansNeo_TTF_original/SpoqaHanSansNeo-Thin.ttf'))

def add_experience_section(story, experience_data, styles):
    # Adding the "경력" label only once for the first item
    label_added = False
    for exp in experience_data:
        # Add the "경력" label only for the first item
        if not label_added:
            label = Paragraph("경력", styles["RegularFont"])
            label_added = True
        else:
            label = ""
        
        # Company, Position, and Duration
        data = [[label, 
                 Paragraph(exp["company"], styles["BoldFont_size12"]),
                 Paragraph(exp["duration"], styles["RegularFont"])]]
        data.append([None,
                     Paragraph(exp["position"], styles["RegularFont"]),
                     None])
        
        # Projects
        for proj in exp["projects"]:
            data.append([None,
                         Paragraph("● " + proj["name"] + " " + proj["duration"], styles["RegularFont_size10"]),
                         None])
            for detail in proj["details"]:
                data.append([None, Paragraph("– " + detail, styles["CustomBullet_size10"]), None])
        
        table = Table(data, colWidths=[40, 250, 150], rowHeights=20)
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5)
        ]))
        story.append(table)
        story.append(Spacer(1, 25))

def add_education_section(story, education_data, styles):
    # Adding the "학력" label only once for the first item
    label_added = False
    for edu in education_data:
        # Add the "학력" label only for the first item
        if not label_added:
            label = Paragraph("학력", styles["RegularFont"])
            label_added = True
        else:
            label = ""
        
        # School Name, Major, and Duration
        data = [[label, 
                 Paragraph(edu["school_name"], styles["BoldFont_size12"]),
                 Paragraph(edu["duration"], styles["RegularFont"])]]
        data.append([None,
                     Paragraph(edu["major"], styles["RegularFont"]),
                     None])
        
        table = Table(data, colWidths=[40, 250, 150], rowHeights=20)
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5)
        ]))
        story.append(table)
        story.append(Spacer(1, 25))

def add_skills_section(story, skills, styles, max_width=400):
    # Concatenate skills with ", " separator
    skills_text = ", ".join(skills)
    
    # Split the skills text into lines that don't exceed the max width
    lines = []
    line = []
    current_width = 0
    
    for skill in skills:
        skill_width = pdfmetrics.stringWidth(skill, 'SpoqaHanSansNeo-Regular', 12)
        if current_width + skill_width < max_width:
            line.append(skill)
            current_width += skill_width + pdfmetrics.stringWidth(", ", 'SpoqaHanSansNeo-Regular', 12)
        else:
            lines.append(", ".join(line))
            line = [skill]
            current_width = skill_width

    # Add any remaining skills to the lines list
    if line:
        lines.append(", ".join(line))

    # Define the "스킬" label
    label = Paragraph("스킬", styles["RegularFont"])
    
    # Create data list for the table
    data = [[label, Paragraph(lines[0], styles["RegularFont"])]]

    # Add the remaining lines to the data list
    for skill_line in lines[1:]:
        data.append([None, Paragraph(skill_line, styles["RegularFont"])])
    
    # Create the table using the data list
    table = Table(data, colWidths=[40, max_width])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5)
    ]))
    story.append(table)
    story.append(Spacer(1, 25))

def add_awards_and_others_section(story, awards_data, styles):
    # Create an empty data list to store the table rows
    data = []
    label_added = False
    
    for award in awards_data:
        # Add the "수상 및 기타" label only for the first item
        if not label_added:
            label = Paragraph("수상 및 기타", styles["RegularFont"])
            label_added = True
        else:
            label = ""

        # Award/Completion, Details, and Date
        data.append([label, 
                     Paragraph(award["type"], styles["BoldFont_size12"]),
                     Paragraph(award["date"], styles["RegularFont"])])
        if award["details"]:
            data.append([None,
                         Paragraph(award["details"], styles["RegularFont_size10"]),
                         None])
    
    # Create the table using the data list
    table = Table(data, colWidths=[100, 250, 100])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5)
    ]))
    story.append(table)
    story.append(Spacer(1, 25))

def add_language_section(story, language_data, styles):
    # Create an empty data list to store the table rows
    data = []
    label_added = False
    
    for lang in language_data:
        # Add the "외국어" label only for the first item
        if not label_added:
            label = Paragraph("외국어", styles["RegularFont"])
            label_added = True
        else:
            label = ""
        
        # Language, Test, Date, and Score
        data.append([label,
                     Paragraph(lang["language"], styles["BoldFont_size12"]),
                     None])
        data.append([None,
                     Paragraph("● " + lang["test"] + " " + lang["date"], styles["RegularFont_size10"]),
                     None])
        if "score" in lang:
            data.append([None,
                         Paragraph(str(lang["score"]), styles["RegularFont_size10"]),
                         None])
    
    # Create the table using the data list
    table = Table(data, colWidths=[60, 250, 90])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5)
    ]))
    story.append(table)
    story.append(Spacer(1, 25))

def add_links_section(story, links_data, styles):
    # Create an empty data list to store the table rows
    data = []
    
    # Add the "링크" label only for the first item
    label = Paragraph("링크", styles["RegularFont"])

    for link in links_data:
        link_paragraph = Paragraph('<link href="{}">{}</link>'.format(link, link), styles["RegularFont"])
        data.append([label, link_paragraph])
        label = ""
    
    # Create the table using the data list
    table = Table(data, colWidths=[60, 340])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5)
    ]))
    story.append(table)
    story.append(Spacer(1, 25))

class HorizontalLine(Flowable):
    """Custom class to draw a horizontal line in the PDF."""
    
    def __init__(self, width, color=black):
        Flowable.__init__(self)
        self.width = width
        self.color = color

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.line(0, 0, self.width, 0)

def create_wanted_template_v2(filename, applicant_name,email,contact, introduce, 
                              experience_data, education_data, skills, awards_data, 
                              language_data, links_data):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []

    # 새로운 스타일 추가
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="LeftAligned", alignment=0, fontName='SpoqaHanSansNeo-Bold', fontSize=25))
    styles.add(ParagraphStyle(name="RegularFont", fontName='SpoqaHanSansNeo-Regular', fontSize=12))  
    styles.add(ParagraphStyle(name="CustomBullet", fontName='SpoqaHanSansNeo-Regular', fontSize=12, leftIndent=20, firstLineIndent=-20, spaceAfter=5))
    styles.add(ParagraphStyle(name="RegularFont_size10", fontName='SpoqaHanSansNeo-Regular', fontSize=10))
    styles.add(ParagraphStyle(name="CustomBullet_size10", fontName='SpoqaHanSansNeo-Regular', fontSize=10, leftIndent=20, firstLineIndent=-20, spaceAfter=5))
    styles.add(ParagraphStyle(name="BoldFont_size12", fontName='SpoqaHanSansNeo-Bold', fontSize=12))
    styles.add(ParagraphStyle(name="BoldFont_size10", fontName='SpoqaHanSansNeo-Bold', fontSize=10))
    
    # 제목(이름)
    title_text = "<b>{}</b>".format(applicant_name)  # 인자로 받은 이름을 여기에 반영
    title = Paragraph(title_text, styles["LeftAligned"])
    story.append(title)
    story.append(Spacer(1, 50))

    # 이메일story.append(Spacer(1, 50))
    email = "<b>{}</b>".format(email)  # 인자로 받은 이름을 여기에 반영
    email_label = Paragraph("<b>이메일:</b>"+email, styles["RegularFont"])
    story.append(email_label)
    
    # 연락처
    contact = "<b>{}</b>".format(contact)  # 인자로 받은 이름을 여기에 반영
    contact_label = Paragraph("<b>연락처:</b>"+contact, styles["RegularFont"])
    story.append(contact_label)
    story.append(Spacer(1, 15))
    
    # 한줄 소개
    for line in introduce.split('\n'):
        if line.startswith('•'):
            p = Paragraph(line, styles["CustomBullet"])
        else:
            p = Paragraph(line, styles["RegularFont"])
        story.append(p)
    story.append(Spacer(1, 25))
        
    story.append(HorizontalLine(450))  # Add the horizontal line
    story.append(Spacer(1, 25))
    
    # 경력
    add_experience_section(story, experience_data, styles)

    story.append(HorizontalLine(450))  # Add the horizontal line
    story.append(Spacer(1, 25))
    
    # 학력
    add_education_section(story, education_data, styles)

    story.append(HorizontalLine(450))  # Add the horizontal line
    story.append(Spacer(1, 25))

    # 스킬
    add_skills_section(story, skills, styles)

    story.append(HorizontalLine(450))  # Add the horizontal line
    story.append(Spacer(1, 25))

    # Awards and Others
    add_awards_and_others_section(story, awards_data, styles)
    story.append(HorizontalLine(450))
    story.append(Spacer(1, 25))
    
    # Language
    add_language_section(story, language_data, styles)
    story.append(HorizontalLine(450))
    story.append(Spacer(1, 25))
    
    # Links
    add_links_section(story, links_data, styles)
    
    doc.build(story)


# # Sample Introduction Data
# introduce = '''Next.js, TypeScript, React 기반의 5년차 프론트엔드 개발자 김티드입니다.
# 새로운 기술을 활용해 비즈니스 문제를 해결하는 것에 관심이 많습니다.

# • 웹/앱 서비스의 프론트엔드 설계, 개발, 운영 경험
# • 다수의 UI 구현 경험으로 사용자 인터렉션에 대한 높은 이해도
# • 제한된 리소스 환경에서 기획 단계부터 참여한 프로젝트 다수
# • 프로젝트 리딩 및 다양한 팀과의 협업 경험'''

# # Sample Experience Data
# experience = [
#     {
#         "company": "삼성전자",
#         "position": "소프트웨어 엔지니어",
#         "duration": "2018.01 ~ 2021.01",
#         "projects": [
#             {
#                 "name": "Galaxy S20 UI 개발",
#                 "duration": "2019.05 ~ 2020.05",
#                 "details": ["UI 구현", "사용자 인터랙션 개선"]
#             },
#             {
#                 "name": "Tizen OS 개발",
#                 "duration": "2018.02 ~ 2019.04",
#                 "details": ["OS 최적화", "보안 패치 적용"]
#             }
#         ]
#     },
#     {
#         "company": "LG전자",
#         "position": "데이터 과학자",
#         "duration": "2021.02 ~ 현재",
#         "projects": [
#             {
#                 "name": "데이터 분석 플랫폼 구축",
#                 "duration": "2021.02 ~ 현재",
#                 "details": ["데이터 수집 및 처리", "분석 모델 구현"]
#             }
#         ]
#     }
# ]

# # Sample Education Data
# education = [
#     {
#         "school_name": "서울대학교",
#         "major": "컴퓨터공학과",
#         "duration": "2014.03 ~ 2018.02"
#     },
#     {
#         "school_name": "부산대학교",
#         "major": "전자공학과",
#         "duration": "2010.03 ~ 2014.02"
#     }
# ]

# # Updated Awards and Others Data
# awards_and_others = [
#     {
#         "type": "원티드 주관 해커톤 <해, 커리어> 1위 수상",
#         "details": "아티스트 공연 홍보/펀딩 위한 앱 서비스",
#         "date": "2018.03"
#     },
#     {
#         "type": "ABC 프론트엔드 교육 과정 이수",
#         "details": "",
#         "date": "2017.01"
#     }
# ]

# # Sample Skills Data
# skills_list = ["React.js", "TypeScript", "JavaScript", "SASS", "CSS", "HTML", "Node.js", "JIRA", "Confluence"]

# # Sample Language Data
# language_data_sample = [
#     {
#         "language": "영어",
#         "test": "토익",
#         "date": "2023.09",
#         "score": 750
#     }
# ]

# # Sample Links Data
# links_data_sample = [
#     "https://github.com/wanted",
#     "https://medium.com/wanted"
# ]

# create_wanted_template_v2(filename = "wanted_template_v2.pdf",
#                           applicant_name = "전채욱",
#                           email = " a01025648934@gmail.com",
#                           contact = " 010-2564-8934",
#                           introduce = introduce,
#                           experience_data = experience,
#                           education_data = education,
#                           skills = skills_list,
#                           awards_data = awards_and_others,
#                           language_data = language_data_sample,
#                           links_data=links_data_sample)
