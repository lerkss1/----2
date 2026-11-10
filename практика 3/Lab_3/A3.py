prev_reading = int(input())
curr_reading = int(input ())

if curr_reading > prev_reading:
 volume = curr_reading -prev_reading 
else:
 volume = (10000 - prev_reading) + curr_reading

if volume <= 300:
 cost = 21.00
elif volume <= 600:
 cost = 21.00 + (volume - 300) * 0.06
elif volume <= 800:
 cost = 21.00 + (300 * 0.06) +(volume - 600) * 0.04 
else:
 cost = 21.00 + (300 * 0.06) + (200* 0.04) + (volume - 800) * 0.025

if volume > 0:
 avg_price = cost / volume
else:
 avg_price = 0
 print ("Предыдущее Использовано Текущее  m^3")
print(f" {prev_reading: <13}{curr_reading: <10} {volume:<15} {cost:<11.2f} {avg_price:.2f}")