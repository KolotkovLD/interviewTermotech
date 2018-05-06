import datetime as dt
from dateutil.relativedelta import relativedelta

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = dt.datetime.now()
    return from_date - relativedelta(years=years)

def checkPasport(birth, regist):
    delta = regist - birth
    years_delta = regist.year - birth.year
    check_bool = False
    for i in (14, 20, 45):
        if years_delta == i:
            start_regist = dt.datetime(birth.year + i, birth.month, birth.day)
            end_regist = dt.datetime(birth.year + i, birth.month + 1, birth.day)
            print("start_regist = ", start_regist)
            limit_s = regist - start_regist
            limit_e = end_regist - regist
            print("limit_s = ", limit_s)
            print("limit_e = ", limit_e)
            if limit_s.days >= 0 and limit_e.days >= 0:
                check_bool = True
    return check_bool


birth = dt.datetime(2000, 5, 3)

registration = dt.datetime(2015, 6, 3)

print(checkPasport(birth, registration))
#print(str(yearsago(21, birth)))
