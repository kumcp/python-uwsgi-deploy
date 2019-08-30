
from datetime import datetime, timedelta


def convert_string_to_date(string_date, format_date="%Y/%m/%d"):
    """Convert string to datetime

    Arguments:
        string_date {string} -- String datetime

    Keyword Arguments:
        format_date {str} -- format of string_date value (default: {"%Y/%m/%d"})

    Returns:
        datetime -- datetime value in datetime module
    """

    return datetime.strptime(string_date, format_date)


def get_weekday(string_date, format_day="%A"):
    return convert_string_to_date(string_date).strftime(format_day)


def diff_now(**kwargs):
    """Return the relative date from now

    Returns:
        datetime -- datetime object represent for the specific time
    """
    return datetime.now() + timedelta(**kwargs)


def now(timezone=None):
    """Return current now time.

    Returns:
        datetime -- datetime object represent for the specific time
    """
    return datetime.now()


def strptime(string_date, format_date="%Y/%m/%d", **kwargs):
    """A reference to datetime.strptime, but it has a default format_date
        and the format_date can  be auto detected for some common cases

    Arguments:
        string_date {string} -- string represent for a date

    Keyword Arguments:
        format_date {str} -- format similar parameter to parse into
                            datetime.strptime (default: {"%Y/%m/%d"})

    Returns:
        datetime -- Datetime class base object
    """

    return datetime.strptime(string_date, format_date)


def strptime_list(string_date, format_list=[], **kwargs):
    """A reference to datetime.strptime, and take multiple format.
    Which format match first will be taken as that format.

    Arguments:
        string_date {string} -- string represent for a date

    Keyword Arguments:
        format_list {list} -- format list can be parsed (default: {[]})

    Returns:
        datetime -- Datetime class base object
    """

    for format_string in format_list:
        try:
            return strptime(string_date, format_string, **kwargs)
        except ValueError:
            pass

    raise ValueError("No format match for time data: %s" % (string_data))


def strftime(datetime_obj, format="%Y/%m/%d"):
    """A reference to datetime.strftime, but it has a default format

    Arguments:
        datetime_obj {datetime} -- datetime object

    Keyword Arguments:
        format {str} -- format output (default: {"%Y/%m/%d"})

    Returns:
        str -- Output string
    """
    return datetime_obj.strftime(format)
