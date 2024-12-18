from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a 32-character hexadecimal string

# Predefined users
users = {
    "Cse": "stanley@123",
    "Ece": "stanley@123",
    "It": "stanley@123",
    "Aids": "stanley@123",
    "EEE": "stanley@123",
    "Cme": "stanley@123"
}

def send_email_to_principal(name, department, date, last_date, event_type, event_details, venue, contacts):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "160622733076@stanley.edu.in"
    smtp_password = "pravam@123"  # Replace with your email password

    # Email content
    html_content = f"""
    <html>
    <body>
        <p>Name: {name}</p>
        <p>Department: {department}</p>
        <p>Date: {date}</p>
        <p>Last Date to Enroll: {last_date}</p>
        <p>Event Type: {event_type}</p>
        <p>Event Details: {event_details}</p>
        <p>Venue: {venue}</p>
        <p>Contacts: {contacts}</p>
        <br>
        <form action="http://127.0.0.1:5000/approved" method="post">
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="department" value="{department}">
            <input type="hidden" name="date" value="{date}">
            <input type="hidden" name="last_date" value="{last_date}">
            <input type="hidden" name="event_type" value="{event_type}">
            <input type="hidden" name="event_details" value="{event_details}">
            <input type="hidden" name="venue" value="{venue}">
            <input type="hidden" name="contacts" value="{contacts}">
            <button type="submit">Approved</button>
        </form>
        <form action="http://127.0.0.1:5000/disapproved" method="post">
            <input type="hidden" name="name" value="{name}">
            <button type="submit">Disapproved</button>
        </form>
        <form action="http://127.0.0.1:5000/onhold" method="post">
            <input type="hidden" name="name" value="{name}">
            <button type="submit">On Hold</button>
        </form>
    </body>
    </html>
    """

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = "pravalikaboddupally3@gmail.com"
    msg['Subject'] = "Event Enrollment: " + name
    msg.attach(MIMEText(html_content, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        date = request.form['date']
        last_date = request.form['lastDate']
        event_type = request.form['eventtype']
        event_details = request.form['eventDetails']
        venue = request.form['venue']
        contacts = request.form['contacts']

        # Send email
        send_email_to_principal(name, department, date, last_date, event_type, event_details, venue, contacts)
        
        flash('Event details sent to the principal!', 'success')
        return redirect(url_for('success'))
    return render_template('success.html')

@app.route('/approved', methods=['POST'])
def approved():
    name = request.form['name']
    department = request.form['department']
    date = request.form['date']
    last_date = request.form['last_date']
    event_type = request.form['event_type']
    event_details = request.form['event_details']
    venue = request.form['venue']
    contacts = request.form['contacts']

    # Update the HTML file based on event type
    if event_type.lower() == "hackathon":
        update_html_file("hackathons.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Hackathons!</p>"
    elif event_type.lower() == "coding competition":
        update_html_file("coding_competitions.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Coding Competitions!</p>"
    elif event_type.lower() == "cultural festival":
        update_html_file("cultural_festival.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Cultural Festival!</p>"
    elif event_type.lower() == "cultural workshop":
        update_html_file("cultural_workshops.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Cultural Workshops!</p>"
    elif event_type.lower() == "debate" or event_type.lower() == "quiz":
        update_html_file("debates_quiz.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Debates & Quiz!</p>"
    elif event_type.lower() == "seminar":
        update_html_file("seminars.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Seminars!</p>"
    elif event_type.lower() == "project exhibition":
        update_html_file("project_exhibitions.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Project Exhibitions!</p>"
    elif event_type.lower() == "sports tournament":
        update_html_file("sports_tournaments.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Sports Tournaments!</p>"
    elif event_type.lower() == "social impact activity":
        update_html_file("social_impact_activities.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Social Impact Activities!</p>"
    elif event_type.lower() == "tech talk":
        update_html_file("tech_talks.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Tech Talks!</p>"
    elif event_type.lower() == "technical workshop":
        update_html_file("technical_workshops.html", name, department, date, last_date, event_details, venue, contacts)
        return f"<p>Event by {name} approved and added to Technical Workshops!</p>"
    else:
        return "<p>Event type not recognized!</p>"

def update_html_file(file_path, name, department, date, last_date, event_details, venue, contacts):
    new_event_html = f"""
    <div class="hackathon">
        <h2>{name}</h2>
        <p>Description: {event_details}</p>
        <p>Date: {date}</p>
        <p>Last Date to Enroll: {last_date}</p>
        <p>Venue: {venue}</p>
        <p>Contacts: {contacts}</p>
        <button class="register-btn" onclick="openForm()">Register</button>
    </div>
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Insert the new event HTML before the closing </div> tag
    updated_content = content.replace("</div>", f"{new_event_html}</div>", 1)

    with open(file_path, 'w') as file:
        file.write(updated_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
