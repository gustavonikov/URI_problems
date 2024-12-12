cases = int(input())

for case in range(cases):
    power_strips_data = input().split()
    power_strips_data = [int(item) for item in power_strips_data]
    power_strips_data.pop(0)

    appliances_max_number = sum(power_strips_data) - (len(power_strips_data) - 1)

    print(appliances_max_number)
