"""
    You're given a list of time intervals during which students at a school need a laptop. These time
    intervals are represented by pairs of integers [start, end], where 0 <= start < end don't represent
    real times; therefore, they may be greater than 24.

    No two students can use a laptop at the same time, but immediately after a student is done using a 
    laptop, another student can use that same laptop. For example, if one student rents a laptop during
    the time interval [0, 2], another student can rent the same laptop during any time interval starting
    with 2.

    Write a function that returns the minimum number of laptops that the school needs to rent such that all
    students will always have access to a laptop when they need one.

    Example:
        times = [
            [0, 2],
            [1, 4],
            [4, 6],
            [0, 4],
            [7, 8],
            [9, 11],
            [3, 10]
        ]

        Output:
            3
"""
# Time O(n log(n))
def laptopRentals(times):
    if times == []:
        return 0

    # Get the latest time we need to have a laptop rented out    
    times = sorted(times, key=lambda x: x[1])
    max_time = times[-1][1]

    # Construct an array where every slot represents a rental time
    all_times = [0]*(max_time+1)

    for this_time in times:
        start_time, end_time = this_time
        
        # Add a 1 to every rental time in this rental's range
        for i in range(start_time, end_time):
            all_times[i] = all_times[i] + 1

    # Get the time slot with the greatest number of laptops checked out
    return max(all_times)