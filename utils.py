from datetime import datetime, timedelta, date

def generate_status(hoje):

    # Get next wednesday
    next_zeca_feira = date.today() + timedelta((2 - hoje.weekday()) % 7)

    d1 = datetime.strptime(
        f"{hoje.year}-{hoje.month}-{hoje.day} {hoje.hour}:{hoje.minute}",
        "%Y-%m-%d %H:%M")
    d2 = datetime.strptime(f"{next_zeca_feira} 08:00", "%Y-%m-%d %H:%M")

    # Time difference between today and next wednesday
    zeca_delta = d2 - d1
    zeca_hours = int(zeca_delta.total_seconds() / 3600) # 3600 seconds = 1 hour

    if zeca_delta.days > 0:
        s_suffix = "s" if zeca_delta.days > 1 else ""
        m_suffix = "m" if zeca_delta.days > 1 else ""

        status = f"Falta{m_suffix} {zeca_delta.days} dia{s_suffix}"

    elif zeca_hours > 0:
        s_suffix = "s" if zeca_hours > 1 else ""
        m_suffix = "m" if zeca_hours > 1 else ""

        status = f"Falta{m_suffix} {zeca_hours} hora{s_suffix}"

    else:
        status = "Feliz zeca-feira!"

    return status