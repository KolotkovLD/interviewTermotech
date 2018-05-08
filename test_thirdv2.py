import datetime as dt
from dateutil.relativedelta import relativedelta

def checkPasport(birth, regist, age):
    delta = regist - birth
    years_delta = regist.year - birth.year
    check_bool = False
    i = age
    if years_delta >= i:
        start_regist = dt.datetime(birth.year + i, birth.month, birth.day)
        limit_s = regist - start_regist
        if limit_s.days >= 0:
            check_bool = True
    return check_bool

def getAge(birth):
    """
    age last pasport must be
    """
    now = dt.datetime.now()
    birth14 = dt.datetime(birth.year + 14, birth.month, birth.day)
    birth20 = dt.datetime(birth.year + 20, birth.month, birth.day)
    birth45 = dt.datetime(birth.year + 45, birth.month, birth.day)
    
    if now >= birth45:
        age = 45
    elif now >= birth20:
        age = 20
    elif now >= birth14:
        age = 14
    return age

# YYYY, M, D
birth = dt.datetime(2000, 5, 3)
registration = dt.datetime(2015, 6, 3)

age = getAge(birth)

checkPasport(birth, registration, age)
