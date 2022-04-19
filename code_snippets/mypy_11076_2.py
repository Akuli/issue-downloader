def ensure_correct_context(event: EventBase, context: Final[EventContext]):
  remote_auth_chain = get_event_auth(event)
  for auth_event in remote_auth_chain:
    # XXX: Violation shold trigger here!
    # We are introducing a bug because `context` which corresponds to `event`
    # is being re-assigned to the `context` for the `auth_event`
    context = compute_event_context(auth_event)
    persist_event(auth_event, context)

  # logic for context_needs_updating

  if context_needs_updating:
    return compute_event_context(event)

  return context
