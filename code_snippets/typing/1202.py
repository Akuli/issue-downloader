Email: TypeAlias = str

def send_email(email: Email) -> int:
    # Send an email
    ...

# passes
send_email("test@example.com")

# passes
send_email("badddd")

# passes even if unknown_var is only identified as `str`
send_email(unknown_var)

# This is a bad regex pattern, but you get the idea :)
Email: TypeAlias = str['[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+']

def send_email(email: Email) -> int:
    # Send an email
    ...

# passes
send_email("test@example.com")

# fails
send_email("badddd")

# passes even if unknown_var is only identified as `str`
send_email(unknown_var)
