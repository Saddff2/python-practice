from datetime import datetime

def hours_drive(drive_time_start, drive_time_end):
    total_drive_time = 0
    for start_time, end_time in zip(drive_time_start, drive_time_end):
        t1 = datetime.strptime(start_time, "%H%M")
        t2 = datetime.strptime(end_time, '%H%M')
        delta = t2 - t1
        seconds_drive = delta.total_seconds() / 60 / 60
        drive = seconds_drive - 1
        if drive <= 0:
            print('Insufficient drive time for hours')
        else:
            total_drive_time += drive
        print('Total drive time:', total_drive_time)

if __name__ == '__main__':
    while True:
        drive_time_start = []
        drive_time_end = []
        while True:
            drive_time_start_input = input('Enter the start time of drive (HHMM), or press Enter to finish: ')
            if not drive_time_start_input:
                break
            drive_time_end_input = input('Enter the end time of drive (HHMM): ')
            drive_time_start.append(drive_time_start_input)
            drive_time_end.append(drive_time_end_input)
        
            if not drive_time_start or not drive_time_end:
                print("No drive time data provided.")
                break  # выходим из внутреннего цикла, если не введено время
            else:
                hours_drive(drive_time_start, drive_time_end)
