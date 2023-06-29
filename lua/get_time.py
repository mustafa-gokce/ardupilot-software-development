import datetime


def gps_to_unix(gps_week, gps_week_ms, utc_offset=3):
    """
    Convert GPS week and seconds to UNIX time.
    :param gps_week: Number of weeks since EPOCH
    :param gps_week_ms: Number of milliseconds since the start of the current week
    :param utc_offset: Local time zone offset
    :return:
    """
    epoch = datetime.datetime(year=1980, month=1, day=6)
    elapsed = datetime.timedelta(weeks=gps_week, hours=utc_offset, seconds=-18, milliseconds=gps_week_ms)
    return epoch + elapsed


if __name__ == "__main__":
    print(gps_to_unix(gps_week=2268, gps_week_ms=403033600))
