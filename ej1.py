import numpy as np
import matplotlib.pyplot as plt
import time
from decimal import Decimal, ROUND_DOWN

num_samples = 1000  # Choose the number of samples you want
uniform_sample = np.random.uniform(low=0, high=1, size=num_samples)

# Create a histogram of the uniform sample
# plt.figure(figsize=(8, 6))
# plt.hist(uniform_sample, bins=20, edgecolor='black', density=True)
# plt.title('Uniform Distribution between 0 and 1')
# plt.xlabel('Value')
# plt.ylabel('Probability Density')
# plt.grid(True)
# plt.show()

exp_lambda = 10/60
exponential_sample = (-np.log(1-uniform_sample)) / exp_lambda

# plt.figure(figsize=(8, 6))
# plt.hist(exponential_sample, bins=20, edgecolor='black', density=True)
# plt.title('Exponential')
# plt.xlabel('Value')
# plt.ylabel('Probability Density')
# plt.grid(True)
# plt.show()


def events_per_minute(time_intervals):
    count = 0
    timer = 0
    event_count = []
    for event in time_intervals:
        timer += event
        if timer < 60:
            count +=1
        else:
            timer -=60
            event_count.append(count)
            while timer > 60:
                timer -=60
                event_count.append(0)
            count = 1
    return np.array(event_count)

maybe_poisson = events_per_minute(exponential_sample)


# plt.figure(figsize=(8, 6))
# plt.hist(maybe_poisson, bins=10, edgecolor='black', density=True)
# plt.title('Poisson')
# plt.xlabel('Value')
# plt.ylabel('Probability Density')
# plt.grid(True)
# plt.show()

def total_times(intervals):
    acumulated = 0
    total_times =[]
    for interval in intervals:
        acumulated += interval
        total_times.append(acumulated)
    return total_times

times_of_arrival = total_times(exponential_sample)

def crop_to_first_decimal(number):
    decimal_number = Decimal(str(number))
    cropped_decimal = decimal_number.quantize(Decimal('0.0'), rounding=ROUND_DOWN)
    return float(cropped_decimal)

def cars_in_queue(time_intervals):
    accumulated = 0
    arrival_times = []
    departure_times = []
    for interval in time_intervals:
        interval = int(10*crop_to_first_decimal(interval))
        accumulated += interval
        arrival_times.append(accumulated)
        if len(departure_times) == 0:
            departure_times.append(arrival_times[0]+100)
        elif accumulated > departure_times[-1] :
            departure_times.append(accumulated+100)
        else:
            departure_times.append(departure_times[-1]+100)
    print(arrival_times[0:20])
    print(departure_times[0:20])
    return arrival_times, departure_times

def generate_queue(arrival_times, departure_times):

    # Combine and sort both arrival and departure times
    all_times = sorted(arrival_times + departure_times)

    # Initialize variables
    current_queue_length = 0
    queue_lengths = []  # To store queue length at different time points

    # Time points at which you want to record the queue length
    time_points = range(min(all_times), max(all_times) + 1)

    # Iterate through time points
    for time_point in time_points:
        # Check arrivals
        while arrival_times and arrival_times[0] <= time_point:
            current_queue_length += 1
            arrival_times.pop(0)
        
        # Check departures
        while departure_times and departure_times[0] <= time_point:
            current_queue_length -= 1
            departure_times.pop(0)
        
        # Record queue length at this time point
        queue_lengths.append(current_queue_length)

    # Create the plot
    plt.plot(time_points, queue_lengths)
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Queue Length Over Time')
    plt.grid(True)
    plt.show()
    


arr, dep = cars_in_queue(exponential_sample)

generate_queue(arr, dep)