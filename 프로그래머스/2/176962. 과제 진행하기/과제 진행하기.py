import heapq as hq

def solution(plans):
    heap = []
    stack = []
    answer = []
    
    # initialization
    for hw in plans:
        hour, minute = map(int, hw[1].split(':'))
        hq.heappush(heap, [hour*60+minute, hw[0], int(hw[2])])
    
    # heap[i] = (start, name, playtime)
    stack.append(hq.heappop(heap))
    while heap:
        if stack[-1][0] + stack[-1][2] > heap[0][0]:
            stack[-1][2] += stack[-1][0] - heap[0][0]
            stack.append(hq.heappop(heap))
        elif stack[-1][0] + stack[-1][2] == heap[0][0]:
            answer.append(stack[-1][1])
            stack[-1] = hq.heappop(heap)
        else: # stack[-1][0] + stack[-1][2] < heap[0][0]
            rest = heap[0][0] - (stack[-1][0] + stack[-1][2])
            answer.append(stack.pop()[1])
            while stack:
                if stack[-1][2] > rest:
                    stack[-1][2] -= rest
                    break
                elif stack[-1][2] == rest:
                    answer.append(stack.pop()[1])
                else: # stack[-1][2] < rest
                    rest -= stack[-1][2]
                    answer.append(stack.pop()[1])
            stack.append(hq.heappop(heap))
    while stack:
        answer.append(stack.pop()[1])
    
    return answer