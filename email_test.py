import smtplib
from email.mime.text import MIMEText

email_config = dict()
email_config['EMAIL_FROM'] = 'poc2a_telemetry_monitor@apple.com'
email_config['SMTP'] = 'relay.apple.com'

"""
def send_email(job, final_path, job_output, job_errors):
    # job is the dict formed from loading the YAML
    success = len(job_errors) == 0
    if job['email']:
        if success:
            prefix = 'SUCCEEDED'
            body = 'Experiment %s %s' % (job['title'], prefix)
            body += '\n\n' + '='*30 + '\n\n' + job_output + '\n\n' + '='*30
            if final_path is not None:
                body += '\n\nResults available at %s' % (final_path)
        else:
            prefix = 'FAILED'
            report = ''
            for error in job_errors:
                for key in sorted(error):
                    report += '%s:\n%s\n' % (key,error[key])
            body = 'Experiment %s failed:\n\n %s\n\nFiles available at %s' % (job['title'], report, final_path)
        msg = MIMEText(body)
        msg['Subject'] = '%s %s' % (prefix,job['title'])
        msg['From'] = email_config['EMAIL_FROM']
        msg['To'] = ', '.join(job['email'])
        sent = False
        timeout = RETRY_TIMEOUT
        while not sent and timeout > 0:
            try:
                s = smtplib.SMTP(email_config['SMTP'])
                s.sendmail(email_config['EMAIL_FROM'], job['email'], msg.as_string())
                s.quit()
                sent = True
            except Exception as e:
                print 'Sending email failed: %s' % (str(e))
                timeout -= RETRY_DELAY
                time.sleep(RETRY_DELAY)
"""




RETRY_TIMEOUT = 30
RETRY_DELAY = 5
def send_msg_to_contacts(message, contacts):
    msg = MIMEText(message)
    msg['Subject'] = 'Test'
    msg['From'] = 'poc2a_telemetry_monitor@apple.com'
    msg['To'] = ', '.join(contacts)
    sent = False
    timeout = RETRY_TIMEOUT
    while not sent and timeout > 0:
        try:
            s = smtplib.SMTP('relay.apple.com')
            s.sendmail('poc2a_telemetry_monitor@apple.com', msg['To'], msg.as_string())
            s.quit()
            sent = True
        except Exception as e:
            print('Sending email failed')
            timeout -= RETRY_DELAY
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    contacts = ['zlovett@apple.com']
    message = "Hello! This is a test! Will it work?"
    send_msg_to_contacts(message, contacts)
