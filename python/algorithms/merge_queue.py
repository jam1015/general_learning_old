import random
from collections import deque
slack_q = deque([])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves
ra_1_len = 80
ra_2_len = 80
var1 = random.sample(range(1, 100), ra_1_len)
var1.sort()
var2 = random.sample(range(1, 100), ra_2_len)
var2.sort()

ra_1_len = len(var1)
ra_2_len = len(var2)
full_len = ra_1_len + ra_2_len



to_sort = var1 + var2


assignment_ind = 0
probe = ra_1_len
assignment_ind = 0


def print_probes(ra_in, assign,  probe2):
    for i, val in enumerate(ra_in):
        if i == assign:
            print("+", end="")
        if i == probe2:
            print("@", end="")
        print(str(val) + ", ", end="")
    print("")


print_probes(to_sort,  assignment_ind, probe)

while assignment_ind < ra_1_len or slack_q:
    print("~~~~~~~~~~~~~~~~~")
    print_probes(to_sort, assignment_ind,  probe)
    print(slack_q)
    if not slack_q:
        if probe >= full_len:
            pass
        else:
            if to_sort[assignment_ind] <= to_sort[probe]:
                pass
            else:
                slack_q.append(to_sort[assignment_ind])
                to_sort[assignment_ind] = to_sort[probe]
                probe += 1
    else:
        if assignment_ind < ra_1_len: # only append if we need to
            slack_q.append(to_sort[assignment_ind])
        if probe < full_len:
            if slack_q[0] <= to_sort[probe]: #assigning from queue 
                to_sort[assignment_ind] = slack_q.popleft()
            else: # assigning from probe position
                to_sort[assignment_ind] = to_sort[probe]
                probe += 1
        else:
            to_sort[assignment_ind] = slack_q.popleft()
    assignment_ind += 1
    print_probes(to_sort,  assignment_ind, probe)

print(to_sort)
