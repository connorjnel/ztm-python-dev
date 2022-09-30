import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


# Email structure and content
html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Jovan"
email["to"] = "test@test.com"
email["subject"] = "Rabbit, rabbit 🐰"

email.set_content(html.substitute(
    {"name": "Hobbit", "animal": "Rabbit"}), "html")

# SMTP Connection
try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("test@test.com", 'dfsgkjdnfg')
        smtp.send_message(email)
        print("All good boss!")
except:
    print("There was a problem")
