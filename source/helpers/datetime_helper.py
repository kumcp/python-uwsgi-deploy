import pytz
from datetime import datetime

from source.constant.constant import DEFAULT_TIMEZONE


def to_utc_string(datetime_string, datetime_format="%Y-%m-%d %H:%M:%S", timezone=DEFAULT_TIMEZONE):
    """Convert datetime string from specific timezone to UTC timezone

    Arguments:
        datetime_string {string} -- Datetime string
        datetime_format {string} -- Format of datetime you want to return
        timezone {string} -- Timezone you want to convert to UTC, default is Asia/Tokyo

    Returns:
        datetime -- datetime value in datetime module
    """

    date_object = datetime.strptime(datetime_string, datetime_format)
    local = pytz.timezone(timezone)
    local_dt = local.localize(date_object, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)

    return utc_dt.strftime(datetime_format)


def start_time_of_date(date_string):
    """Convert datetime string to start time of date

    Arguments:
        date_string {string} -- Date string you want to get start time of

    Returns:
        datetime string -- start time of date
    """

    return date_string + " 00:00:00"


def end_time_of_date(date_string):
    """Convert datetime string to end time of date

    Arguments:
        date_string {string} -- Date string you want to get start time of

    Returns:
        datetime string -- end time of date
    """

    return date_string + " 23:59:59"


def convert_by_timezone(datetime, from_timezone, to_timezone):
    """Convert datetime from {from_timezone} to {to_timezone}

    Arguments:
        datetime {datetime} -- Date object you want to convert
        from_timezone {string}
        to_timezone {strign}

    Returns:
        datetime object -- converted datetime
    """

    from_timezone_object = pytz.timezone(from_timezone)
    from_datetime = from_timezone_object.localize(datetime, is_dst=None)
    to_datetime = from_datetime.astimezone(pytz.timezone(to_timezone))

    return to_datetime
