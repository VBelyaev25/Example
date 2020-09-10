import imaplib
import time

class GetCodeIntoEmail():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def getEmail(self):
        time.sleep(20)
        mail = imaplib.IMAP4_SSL('imap.rambler.ru')
        mail.login(self.email, self.password)
        mail.list()
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        import email
        email_message = email.message_from_string(raw_email_string)
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
        import re
        code_idx = re.search(r'Ваш код', body).start()
        code = body[code_idx + 8: code_idx + 14]
        return code