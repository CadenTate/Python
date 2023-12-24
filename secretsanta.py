import random
import smtplib, ssl

chat = ["marley","reagan","Judah","lila","caden"]
selection = ["marley","reagan","Judah","lila","caden"]
emails = ["marleygrace0909@icloud.com","rjackson7886@stu.neisd.net","judahdins@gmail.com","lilabearchristian@gmail.com","cadentate0511@gmail.com"]

# Email configuration
# sender_email = 'cadentate0511@gmail.com'

# Connect to the SMTP server (in this case, using Gmail)
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587

# Start TLS for security
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()

# Login to the email account
# server.login(sender_email, 'kvod cmyz gqke wwdk')

for person in chat:
    getter = random.choice(selection)
    while getter == person:
        getter = random.choice(selection)

    selection.pop(selection.index(getter))

    # Attach the body to the email
    # receiver_email = emails[chat.index(person)]

    # Send the email
    # server.sendmail(sender_email, receiver_email, f"{person} got {getter}")
    print(f"{person} got {getter}")

# Quit the server
# server.quit()