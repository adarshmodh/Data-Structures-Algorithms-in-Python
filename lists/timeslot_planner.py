"""
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

inputs = slotsA = [[10, 50], [60, 120], [140, 210]]
         slotsB = [[0, 15], [60, 70]]
         dur = 8
outputs = [60, 68]

Time complexity = O(n+m) - 2pointers (O(nxm) - if you do 2 for loops)
Space complexity = O(1)


"""

def meeting_planner(slotsA, slotsB, dur):
  
  a_index = 0
  b_index = 0
  
  while(a_index<len(slotsA) and b_index<len(slotsB)):
    
    start_slot = max(slotsA[a_index][0], slotsB[b_index][0])
    end_slot = min(slotsA[a_index][1], slotsB[b_index][1])
    
    if end_slot-start_slot>=dur:
      return [start_slot,start_slot+dur]
    else: 
      if slotsA[a_index][1]<=slotsB[b_index][1]:
        a_index = a_index + 1
      else:
        b_index = b_index + 1
        
    
  return [] # your code goes here


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA,slotsB,dur))
