def maximum_possible_date_anywhere_on_earth(instant: Optional[datetime] = None) -> date:
    """
    The largest possible date that any human on earth could legitimately
    claim to be "today". Basically whatever day the UTC+14 people are on.
    """
    if instant is None:
        instant = now()

    return max(
        timezone.normalize(instant.astimezone(timezone)).date()
        for timezone in map(pytz.timezone, pytz.all_timezones)
    )
