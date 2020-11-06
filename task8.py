def digit_to_time(digit):
    hours = int(digit / 60)
    minutes = int(digit % 60)
    h_plural = "" if (hours == 1) else "s"
    m_plural = "" if (minutes == 1) else "s"
    return(f"{hours} hour{h_plural}, {minutes} minute{m_plural}")

