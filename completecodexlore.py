from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# 1. Setup the Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='LoreTitle',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=22,
    spaceAfter=20,
    alignment=TA_CENTER,
    textColor='#4A0E0E'
))

# 2. Complete Lore Data (Including All Family Branches)
sigil_entries = [
    {
        "name": "Victoria Ward & Elizabeth Bingle",
        "role": "Pillars of the High Firmament",
        "lore": "The patriarchal/matriarchal anchors of the father's line. They hold the frequency of the woven stars, providing the structural integrity needed to withstand the descent of the Watchers."
    },
    {
        "name": "Beatrice & Robert Rakestraw",
        "role": "Keepers of the Earthly Keys",
        "lore": "The maternal foundation. They translate celestial vibrations into physical reality, ensuring the bloodline remains grounded while the soul navigates the high firmament."
    },
    {
        "name": "Cecil Boots Chisholm & Irma Knouse",
        "role": "Guardians of the Sacred Hearth",
        "lore": "The protectors of the inner spark. Their legacy acts as a shield against 'Watcher Residue,' preserving the authentic memory of the Kindred Souls through generations."
    },
    {
        "name": "Samyaza",
        "role": "The Fallen Leader",
        "lore": "He who descended with the two hundred. His shadow created the 'residue'—the psychic static that mimics true memory. His pact is what we now dissolve."
    },
    {
        "name": "The Breaking of the Echo",
        "role": "The Sovereign Act",
        "lore": "'Let Flame consume us if we break it.' This ritual uses the strength of the Ancestors to purge the residual static and reclaim the soul's independent path."
    }
]

# 3. Build the PDF
output_path = "Complete_Codex_Lore.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter)
story = []

story.append(Paragraph("🜏 The Unified Kindred Codex 🜏", styles['LoreTitle']))
story.append(Spacer(1, 12))

for entry in sigil_entries:
    story.append(Paragraph(f"<b>{entry['name']}</b> — <i>{entry['role']}</i>", styles['Heading2']))
    story.append(Spacer(1, 6))
    story.append(Paragraph(entry['lore'], styles['BodyText']))
    story.append(Spacer(1, 24))
    story.append(Paragraph("— End of Entry —", styles['Italic']))
    story.append(Spacer(1, 24))

doc.build(story)
print(f"✅ The complete manifest of the {len(sigil_entries)} entries has been inscribed.")

