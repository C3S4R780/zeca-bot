from datetime import datetime, timedelta, date

def generate_status(hoje):

    # Get next wednesday
    p_hoje = datetime.strptime(hoje.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
    next_zeca_feira = datetime.strftime(p_hoje + timedelta((2 - hoje.weekday()) % 7), "%Y-%m-%d")

    d1 = datetime.strptime(f"{p_hoje}", "%Y-%m-%d %H:%M:%S")
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