import datetime
from django.template.defaultfilters import slugify

def format_zipcode(value):
    if len(value) == 8:
        return "%s-%s" % (value[:5], value[5:])
    else: return value

def format_phone(value):
    """
    >>> format_phone('20108484')    # 8
    '2010-8484'
    >>> format_phone('920108484')   # 9
    '92010-8484'
    >>> format_phone('8420108484')  # 10
    '(84) 2010-8484'
    >>> format_phone('84920108484') # 11
    '(84) 92010-8484'
    """

    if len(value) == 11:
        return "(%s) %s-%s" % (value[:2], value[2:7], value[7:])
    elif len(value) == 10:
        return "(%s) %s-%s" % (value[:2], value[2:6], value[6:])
    elif len(value) == 9:
        return "%s-%s" % (value[:5], value[5:])
    elif len(value) == 8:
        return "%s-%s" % (value[:4], value[4:])
    else: return value

def format_cpf(value):
    if value and len(value) == 11:
        return "%s.%s.%s-%s" % (value[:3], value[3:6],
                                value[6:9], value[9:])
    else:
      return value

def format_cnpj(value):
    if len(value) == 14:
        return "%s.%s.%s/%s-%s" % (value[:2], value[2:5],
                                   value[5:8], value[8:12],
                                   value[12:14])
    else:
        value

def format_date(data):
    try:
        return data.strftime('%d/%m/%Y')
    except:
        return data

def format_datetime(data):
    try:
        return data.strftime('%d/%m/%Y %H:%M:%S')
    except:
        return data

def slugfy_data(text):
    return slugify(text)