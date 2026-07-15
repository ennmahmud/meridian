def parse_event_date(raw):
    """Parse "YYYY-MM-DD" or "YYYY/MM/DD" into an (int, int, int) tuple."""
    sep = "/" if "/" in raw else "-"
    year, month, day = raw.split(sep)
    return (int(year), int(month), int(day))
