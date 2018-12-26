def transform_date(date):
    """Encodes date and timke into url format.

    :param date: Date and time.
    :type date: str

    :return: encoded date.
    :rtype: str
    """
    index = date.find(' ')
    date = (date[:index] + 'T' + date[index + 1:] +
            ":00.12345+00:00").replace(':', '%3A').replace('+', '%2B')
    return date


def transform_boolean(value):
    """Transfroms boolean to `1` or `0`.

    :param value: Boolean value.
    :type value: boolean

    :return: number representation of boolean `1` or `0`.
    :rtype: str
    """
    if value:
        return '1'
    else:
        return '0'


def transform_tone(tone):
    """Transforms keyword `negative`, `neutral` or `positive` into `-1`, `0` or `1`.

    :param tone: string representation of tone.
    :type tone: str

    :return: number representation of tone.
    :rtype: str
    """
    if 'negative':
        return '-1'
    elif 'neutral':
        return '0'
    else:
        return '1'
