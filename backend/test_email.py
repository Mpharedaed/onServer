import smtplib

def send_test_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # TLS port for Gmail
    smtp_username = 'mohamed200334reda@gmail.com'  # Your Gmail address
    smtp_password = 'jhaa thqb zvtx fokj'  # Your generated app password
    from_email = 'mohamed200334reda@gmail.com'
    to_email = 'mohamedredaed@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email.'

    message = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, message)
        server.quit()
        print('Test email sent successfully')
    except Exception as e:
        print(f'Failed to send test email: {e}')

if __name__ == '__main__':
    send_test_email()
