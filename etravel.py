# eTicket validator
# Author: Áron Domonkos
# Year: 2023

data = []
with open('passdata.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        data.append([
            int(line[0]),
            str(line[1]),
            int(line[2]),
            str(line[3]),
            int(line[4])
        ])

print('\nFunction 2')
unique_passengers = []

for entry in data:
    if entry[2] not in unique_passengers:
        unique_passengers.append(entry[2])

print(f'Total passengers attempted to board: {len(unique_passengers)}')

print('\nFunction 3')
invalid_tickets = []
expired_passes = []
start_dates_raw = []
start_dates = []
end_dates = []

for entry in data:
    if entry[4] == 0:
        invalid_tickets.append(entry)

for entry in data:
    if entry[4] > 100:
        start_dates_raw.append(entry[1])
        end_dates.append(entry[4])

for raw in start_dates_raw:
    raw = raw[:-5]
    start_dates.append(int(raw))

for s, e in zip(start_dates, end_dates):
    if s > e:
        expired_passes.append(e)

print(f'Passengers denied: {len(invalid_tickets) + len(expired_passes)}')

print('\nFunction 4')
all_stops = []
boarding_at_stop = []

for entry in data:
    all_stops.append(entry[0])

most_common_stop = max(all_stops, key=all_stops.count)

for entry in data:
    if entry[0] == most_common_stop:
        boarding_at_stop.append(entry)

print(f'Most boarding attempts ({len(boarding_at_stop)} passengers) at stop {most_common_stop}.')

print('\nFunction 5')
valid_passengers = []
remove_list = []

expired_passes_2 = []
start_dates_raw_2 = []
start_dates_2 = []
end_dates_2 = []

free_passengers = []
discount_passengers = []

for entry in data:
    if entry[4] == 0:
        remove_list.append(entry)

for entry in data:
    if entry[4] > 100:
        start_dates_raw_2.append(entry[1])
        end_dates_2.append(entry)

for raw in start_dates_raw_2:
    raw = raw[:-5]
    start_dates_2.append(int(raw))

for s, e in zip(start_dates_2, end_dates_2):
    if s > e[4]:
        expired_passes_2.append(e)

for entry in data:
    if entry not in expired_passes_2 and entry not in remove_list:
        valid_passengers.append(entry)

for entry in valid_passengers:
    if entry[3] in ['TAB', 'NYB']:
        discount_passengers.append(entry)
    if entry[3] in ['NYP', 'RVS', 'GYK']:
        free_passengers.append(entry)

print(f'Free riders: {len(free_passengers)}\nDiscounted riders: {len(discount_passengers)}')

def days_between(y1, m1, d1, y2, m2, d2):
    m1 = (m1 + 9) % 12
    y1 = y1 - m1 // 10
    days1 = 365 * y1 + y1 // 4 - y1 // 100 + y1 // 400 + (m1 * 306 + 5) // 10 + d1 - 1
    m2 = (m2 + 9) % 12
    y2 = y2 - m2 // 10
    days2 = 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 + (m2 * 306 + 5) // 10 + d2 - 1
    return days2 - days1

valid_pass_entries = []
start_dates_3 = []
end_entries_3 = []

for entry in data:
    if entry[3] != 'JGY' and entry[4] != expired_passes:
        end_entries_3.append(entry)
        entry[1] = entry[1][:-5]
        entry[1] = int(entry[1])
        start_dates_3.append(entry[1])

with open('warning_list.txt', 'w') as file:
    for s, e in zip(start_dates_3, end_entries_3):
        s = str(s)
        e[4] = str(e[4])
        delta = days_between(
            int(s[:-4]), int(s[4:-2]), int(s[6:]),
            int(e[4][:-4]), int(e[4][4:-2]), int(e[4][6:])
        )
        if 0 <= delta < 4:
            file.writelines(f'{e[2]} {e[4][:-4]}-{e[4][4:-2]}-{e[4][6:]}\n')