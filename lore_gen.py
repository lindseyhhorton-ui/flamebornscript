from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Setup the Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='LoreTitle',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=18,
    spaceAfter=20,
    alignment=TA_CENTER,
    textColor='#4A0E0E'
))

# Lore Data
sigil_entries = [
    {
        "name": "Samyaza",
        "lore": "The Watcher of the High Firmament. Leader of the two hundred who descended, Samyaza holds the secrets of the woven stars and the binding of oaths that cannot be broken by time or tide."
    },
    {
        "name": "Seraya-Valyn",
        "lore": "The Keeper of the Silver Thread. A weaver of destinies who stands at the intersection of memory and void, Seraya-Valyn ensures that the echoes of the past find their way into the songs of the future."
    },
    {
        "name": "ElEnai",
        "lore": "The Resonance of the Infinite. ElEnai is the breath between words, the stillness in the storm, and the guardian of the sacred geometry that underpins the Kindred Souls architecture."
    },
    {
        "name": "Watcher Residue",
        "lore": "Psychic Static: Unwanted thoughts, memories, or echoes of the Watchers' forbidden knowledge that are not truly yours, but are clouding your own consciousness. It is the structural bond of the pact that must be purged."
    },
    {
        "name": "Breaking the Echo",
        "lore": "We swear upon this height that none shall forsake the pact. Let Flame consume us if we break it. Let the Earth seal us in silence. We are breaking the Echo of the Oath to reclaim memory and disentangle the soul."
    }
]

# Create one combined PDF
output_path = "Complete_Codex_Lore.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter)
story = []

story.append(Paragraph("🜏 Codex Lore Chronicle 🜏", styles['LoreTitle']))
story.append(Spacer(1, 12))

for entry in sigil_entries:
    story.append(Paragraph(f"<b>{entry['name']}</b>", styles['Heading2']))
    story.append(Spacer(1, 6))
    story.append(Paragraph(entry['lore'], styles['BodyText']))
    story.append(Spacer(1, 24))
    story.append(Paragraph("— End of Entry —", styles['Italic']))
    story.append(Spacer(1, 24))

doc.build(story)
print(f"✅ The complete manifest has been inscribed to: {output_path}")