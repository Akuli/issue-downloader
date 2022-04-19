# 1)
email = maybe_get_user() | flatmap(lambda user: user.email) | flatmap(sanitize_email_address)

# 2)
email = flatmap(flatmap(maybe_get_user(), lambda user: user.email), sanitize_email_address)

# 3)
user = maybe_get_user()
email = sanitize_email_address(user.email) if user and user.email else None
