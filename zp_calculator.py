from datetime import datetime


def hours_work(start_time, end_time):
    for x in start_time:
        t1 = datetime.strptime(x, "%H:%M")
    for y in end_time:
        t2 = datetime.strptime(y, '%H:%M')
    delta = t2-t1
    seconds = delta.total_seconds()
    total_work = seconds/60/60
    if total_work <= 0:
        total_work += 24
    print('Total work time',total_work)


    

def hours_drive(drive_time_start, drive_time_end):
    for x in drive_time_start:
        t1 = datetime.strptime(x, "%H:%M")
    for y in drive_time_end:
        t2 = datetime.strptime(y, '%H:%M')
    delta = t2-t1
    seconds_drive = delta.total_seconds()/60/60
    drive = seconds_drive - 2
    if drive <= 0:
        print('Insufficient drive time for hours')
    else:
        print('Total drive time', drive)



start_time = ['19:30']
end_time = ['20:30']

drive_time_start = []
drive_time_end = []




if __name__ == '__main__':
    while True:
        drive_time_start = []
        drive_time_end = []
        
        start_times = []
        end_times = []
        while True:
            start_time_input = input("Введите время начала работы (ЧЧ:ММ), или 'q' для завершения: ")
            if start_time_input.lower() == 'q':
                break
            start_times.append(start_time_input)

            end_time_input = input("Введите время окончания работы (ЧЧ:ММ): ")
            end_times.append(end_time_input)

            drive_start_input = input("Введите время начала поездки (ЧЧ:ММ): ")
            drive_time_start.append(drive_start_input)

            drive_end_input = input("Введите время окончания поездки (ЧЧ:ММ): ")
            drive_time_end.append(drive_end_input)

        if len(start_times) == 0 or len(end_times) == 0:
            print("Не предоставлено данных о времени работы. Завершение.")
            break
