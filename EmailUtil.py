class EmailUtil:
    __invalid_email_error = "Email {} is invalid."

    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".edu") or email.endswith(".org"))

    def check_is_valid_email(email):
        if EmailUtil.is_valid_email(email):
            return True

        print(EmailUtil.__invalid_email_error.format(email))

        return False