if message is None:
    message = Message.objects.select_related().get(id=message_id)

assert message is not None # ADDED, but outside the if, now.
rendered_content = render_markdown(message, content, realm=message.get_realm())
