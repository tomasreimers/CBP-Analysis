import sendgrid

# constants

FROM = "bot@tomasreimers.com"
# TO = "6178400482@txt.att.net"
TO = "tomasreimers@gmail.com"

# configure sendgrid

sg = sendgrid.SendGridClient('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')

def send(subject):
    message = sendgrid.Mail(to=TO, subject=subject, text=' ', from_email=FROM)
    status, msg = sg.send(message)
    if status != 200:
        print "SENDING SMS FAILED: " + str(msg)
    return status, msg

if __name__ == "__main__":
    print send("Testing, testing, 1, 2, 3...")
