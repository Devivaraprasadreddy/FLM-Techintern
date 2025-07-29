# Input list of email subjects
emails = ["New Lead from Form", "Daily Report", "Zoom Invite", "Cybersecurity Lead"]

# Iterate and filter subjects containing lead
for subject in emails:
    if "lead" in subject.lower():
        print(subject)

