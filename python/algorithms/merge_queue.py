import random
from collections import deque
slack_q = deque([])
#queue.append("Terry")           # Terry arrives
#queue.append("Graham")          # Graham arrives
#queue.popleft()                 # The first to arrive now leaves

slack_q.popleft() 
ra_1_len = 20
ra_2_len = 21
var1 = random.sample(range(1, 10000), ra_1_len)
var1.sort()
var2 = random.sample(range(1, 10000), ra_2_len)
var2.sort()
to_sort = var1 + var2


ind_1 = 0
ind_2 = ra_1_len
len_slack_q = 0

while ind_1 < ra_1_len and ind_2 < ra_2_len and len_slack_q > 0:

    if len_slack_q == 0:
        if to_sort[ind_1] <= to_sort[ind_2]:
            pass
        if to_sort[ind_1] > to_sort[ind_2]:
            pass

        else:
            if slack_q[len_slack_q] <= to_sort[ind_2]:
                pass
            if slack_q[len_slack_q] > to_sort[ind_2]:
                pass



