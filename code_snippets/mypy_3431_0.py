if message is None:
    message = Message.objects.select_related().get(id=message_id)

rendered_content = render_markdown(message, content, realm=message.get_realm())
