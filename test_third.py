import datetime as dt

def checkPasport(birth, regist):
    years_delta = regist.year - birth.year
    check = False
    for i in (14, 20, 45):
        if years_delta == i:
            # acceptable time for registration
            start_regist = dt.datetime(birth.year + i, birth.month, birth.day)
            end_regist = dt.datetime(birth.year + i, birth.month + 1, birth.day)

            # deltas
            limit_s = regist - start_regist
            limit_e = end_regist - regist

            if limit_s.days >= 0 and limit_e.days >= 0:
                check = True
    return check

# YYYY, M, D
birth = dt.datetime(2000, 5, 3)
registration = dt.datetime(2014, 6, 5)

checkPasport(birth, registration)
