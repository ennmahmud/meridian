from dateutils import parse_event_date


def weekly_summary(dates):
    parsed = [parse_event_date(d) for d in dates]
    return f"{len(parsed)} events this week"
