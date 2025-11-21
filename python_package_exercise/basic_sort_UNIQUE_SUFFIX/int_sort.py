# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers using various sorting algorithms and
measuring specific metrics in each.
"""

import psutil
import random

def bubble(int_list):
    
    """
	Perform a bubble sort operation and measure its CPU usage using psutil
	
	:param int_list: list[int]
	:returns: A sorted list of ints, from smallest to largest
	"""

    print("Bubble Sort")

    # Create a psutil process to measure stats
    process = psutil.Process()
    # Initialize cpu usage metric gathering
    process.cpu_percent(interval=None)

    # Perform bubble sort operation
    for i in range(len(int_list) - 1):
        val = i + 1
        for j in range(len(int_list) - val):
               if int_list[j] > int_list[j+1]:
                   int_list[j], int_list[j+1] = int_list[j+1], int_list[j]

    # Capture final cpu usage metric for execution
    CPU_Usage = process.cpu_percent(interval=None)
    print("CPU used during operation:", CPU_Usage, "%")

def quick(int_list):
    
    """
	Perform a recursive quick sort operation and measure its runtime using psutil
	
	:param int_list: list[int]
	:returns: A sorted list of ints, from smallest to largest
	"""
    
    print("Quick Sort")

    # Create a psutil process to measure stats
    process = psutil.Process()
    # Start the psutil timer
    start_timer = process.cpu_times()
    start_time = start_timer.user + start_timer.system

    # Perform quick sort operation
    def quickSort(cur_list):
        # No need to sort if 1 item
        if len(cur_list) <= 1:
            return cur_list

        # Splits the list in half each time to sort
        split_val = cur_list[len(cur_list) // 2]

        left  = [x for x in cur_list if x < split_val]
        middle   = [x for x in cur_list if x == split_val]
        right = [x for x in cur_list if x > split_val]

        return quickSort(left) + middle + quickSort(right)
    
    # Call the quick sort operation
    quickSort(int_list)

    # End the psutil timer and calculate time elapsed
    end_timer = process.cpu_times()
    end_time = end_timer.user + end_timer.system
    total_time = end_time - start_time
    print("Time taken to complete:", total_time)


def insertion(int_list):
    
    """
	Perform an insertion sort operation and measure its CPU usage using psutil
	
	:param int_list: list[int]
	:returns: A sorted list of ints, from smallest to largest
	"""

    print("Insertion Sort")

    # Create a psutil process to measure stats
    process = psutil.Process()

    # Get the memory usage at the start of the operation
    memory_start = process.memory_info().rss

    # Perform insertion sort operation
    for i in range(1, len(int_list)):
        val = int_list[i]
        j = i - 1
        while j >= 0 and int_list[j] > val:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = val
    
    # Get memory usage at the end of the operation
    memory_end = process.memory_info().rss
    # Calculate change in memory usage
    memory_total = memory_end - memory_start
    print("Total memory usage during operation:", memory_total, "bytes")


int_list = [random.randint(1, 10000) for _ in range(10000)]
bubble(int_list)
quick(int_list)
insertion(int_list)
