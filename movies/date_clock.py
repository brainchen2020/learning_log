from datetime import datetime , timedelta

def DateClocker(start, end , fmt ='%Y%m%d',index=0 ):
    date_index = {}
    start = datetime.strptime(start, fmt)
    end = datetime.strptime(end, fmt)
    days = (end - start).days
    list_dates = [(start + timedelta(i)).strftime(fmt) for i in range(days+1)]
    for date in list_dates:
        temp = {date: index}
        temp = temp.copy()
        if date_index == None:
            date_index = {date: index}

        date_index = dict(date_index)
        date_index.update(temp)
        print(temp)
        index += 1

    return  date_index

# date_index= DateClocker("2018-4-17","2018-5-17", fmt="%Y-%m-%d",index=16 )# from 17 beggined..
# index_daily = date_index[str(datetime.today().strftime("%Y-%m-%d"))]
# print(index_daily)



