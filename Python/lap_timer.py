# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 225.
# Programming Exercise.
# Q 3. Lap Times.

track_round = int(input("Enter the number of rounds: "))   # number of times run around racetrack.
time = 0                                                   # timer at initial state.
time_array = []

for timer in range(track_round):
    lap_time = float(input("Enter Lap Time: t = "))        
    time_array.append(lap_time)
    time += lap_time

average_time = time/track_round
fastest_time = max(time_array)
slowest_time = min(time_array)
print("Fastest Lap Time: ", fastest_time)
print("Slowest Lap Time: ", slowest_time)
print("Average Lap Time: ", average_time)
