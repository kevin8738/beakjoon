from collections import deque
import math

mush = deque()
score = 0
for _ in range(10):
    mush.append(int(input()))
    
for i in range(10):
    now = mush.popleft()
    score += now
    if score >= 100:
        break
    
if abs(100-score) > abs(100-(score-now)):
    print(score-now)
else:
    print(score)