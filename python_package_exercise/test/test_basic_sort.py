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

import pytest
import numpy as np
import int_sort

def is_sorted(self, int_list):
    """
    Testing oracle.
    """
    for i in range(len(int_list)):
        if int_list[i] <= int_list[i+1]:
            return False
    
    return True

@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    # **Used the below line for a long random list of ints
    # int_list = [random.randint(1, 10000) for _ in range(10000)]
    return [[3,2,1],
	        [1,1,1],
			np.random.randint(low=-10, high=200, size=5)] 
    
def test_bubble(int_lists):
    for _list in int_lists:
        sorted_list, metric = int_sort.
def test_quick(int_lists):
    assert True

def test_insertion(int_lists):
    assert True
