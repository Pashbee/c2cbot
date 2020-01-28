from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2018, 1, 1)
end_date = date(2019, 1, 1)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%d%m%Y"))