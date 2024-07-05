# Standard Library
from io import BytesIO

# External
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


## Objective 3.
def get_pdf_file(
    analysis_data: dict[str, int],
    issues_summary: tuple[list[str], str],
    filename: str = "analysis_report.pdf",
):
    main_issues, detailed_analysis = issues_summary
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    story.append(Paragraph("Psychological Emotion Analysis Report", styles["Title"]))
    story.append(Spacer(1, 12))
    plt.figure(figsize=(8, 6))
    plt.pie(analysis_data.values(), labels=analysis_data.keys(), autopct="%1.1f%%", startangle=90)
    plt.title("Emotion Distribution")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png", bbox_inches="tight")
    img_buffer.seek(0)
    story.append(Paragraph("Emotion Distribution", styles["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(Image(img_buffer, width=400, height=300))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Analysis Data", styles["Heading2"]))
    story.append(Spacer(1, 12))
    for emotion, count in analysis_data.items():
        story.append(Paragraph(f"{emotion}: {count}", styles["BodyText"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Main Issues", styles["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(
        ListFlowable(
            [ListItem(Paragraph(issue, styles["BodyText"])) for issue in main_issues],
            bulletType="bullet",
        )
    )
    story.append(Spacer(1, 12))
    story.append(Paragraph("Detailed Analysis", styles["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(detailed_analysis, styles["BodyText"]))
    doc.build(story)
