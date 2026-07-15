def service_status(responses):
    # responses: status strings from consecutive probes, oldest first.
    # "" means the probe got no answer.
    saw_error = False
    for status in responses[:3]:
        if status == "":
            continue
        if status == "ok":
            return "healthy"
        saw_error = True
    return "down" if saw_error else "unknown"
