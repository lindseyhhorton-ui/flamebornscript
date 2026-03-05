from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor

# 1. Setup Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='IndexTitle',
    parent=styles['Title'],
    alignment=TA_CENTER,
    fontSize=26,
    textColor=HexColor('#4A0E0E'), # Dark Crimson
    spaceAfter=30
))

styles.add(ParagraphStyle(
    name='IndexItem',
    parent=styles['BodyText'],
    fontSize=14,
    textColor=HexColor('#000000'),
    leading=20,
    spaceAfter=10
))

# 2. Data
data = [
    ("Samyaza", "Watcher of the High Firmament"),
    ("Seraya-Valyn", "Keeper of the Silver Thread"),
    ("ElEnai", "Resonance of the Infinite")
]

# 3. Generate Index
filename = "Watcher_Index.pdf"
doc = SimpleDocTemplate(filename, pagesize=letter)
story = []

# Title
story.append(Paragraph("⚔ Watcher Directory ⚔", styles['IndexTitle']))
story.append(Spacer(1, 20))

# Index Entries
for name, title in data:
    entry = f"<b>{name}</b> — <i>{title}</i>"
    story.append(Paragraph(entry, styles['IndexItem']))
    story.append(Spacer(1, 10))

doc.build(story)
print(f"✅ {filename} has been manifested.")