def is_person_available(personal_schedule, activity_time):
    for scheduled_start, scheduled_end in personal_schedule:
        start = activity_time[0]
        end = activity_time[1]

        if scheduled_start <= start and scheduled_end >= end:
            return False
        elif scheduled_start <= start and scheduled_end > start:
            return False
        elif scheduled_start < end and scheduled_end >= end:
            return False
    
    return True

cases_count = int(input())
for case_index in range(cases_count):
    general_schedule = []
    cameron_schedule = []
    jamie_schedule = []

    activities_count = int(input())
    for activities_index in range(activities_count):
        aux = input()

        if general_schedule != list('IMPOSSIBLE'):
            activity_time = tuple([int(i) for i in aux.split(' ')])

            if is_person_available(cameron_schedule, activity_time):
                general_schedule.append('C')
                cameron_schedule.append(activity_time)

            elif is_person_available(jamie_schedule, activity_time):
                general_schedule.append('J')
                jamie_schedule.append(activity_time)
            
            else:
                general_schedule = list('IMPOSSIBLE')

    print("Case #{}: {}".format(case_index+1, ''.join(general_schedule)))