class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target: int) -> int:
        i = 0
        for x in hours:
            if target >= x:
                return i+1
        print(i)


Solution.numberOfEmployeesWhoMetTarget(self=0, hours = [1,2,3,4,5,6], target=2)