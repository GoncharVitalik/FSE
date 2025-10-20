last_measurement = int(input())
current_measurement = int(input())
used = current_measurement - last_measurement
if used <= 300:
    pay = 21
elif used <= 600:
    pay = 21 + (used - 300) * 0.06
elif used <= 800:
    pay = 21 + 300 * 0.06 + (used - 600) * 0.04
elif used > 800:
    pay = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
else:
    print("input error")
average = pay / used
print(f"Previous: {last_measurement}")
print(f"Current: {current_measurement}")
print(f"Used: {used}")
print(f"For payment: {pay:.2f}")
print(f"Average price m^3: {average:.2f}")


