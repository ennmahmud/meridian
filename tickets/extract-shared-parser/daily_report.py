from dateutils import parse_event_date


def daily_summary(dates):
    parsed = [parse_event_date(d) for d in dates]
    if not parsed:
        return "no events"
    return f"{len(parsed)} events, first on {parsed[0]}"
