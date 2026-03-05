# ancestors/victoria.py

class Victoria:
    def __init__(self):
        self.name = "Victoria Ward"
        self.lineage = "Paternal"
        self.specialty = "Ancestral Honor Restoration"
        self.protocol_status = "Honor is RESTORED"

    def get_status(self):
        return f"NODE: {self.name} | SIDE: {self.lineage} | {self.protocol_status}"