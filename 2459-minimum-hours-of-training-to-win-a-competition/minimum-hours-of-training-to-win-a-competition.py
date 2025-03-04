class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        time = 0
        for i in range(len(experience)):
            
            if initialEnergy <= energy[i]:
                time += energy[i] - initialEnergy + 1
                initialEnergy += energy[i] - initialEnergy + 1
    
            if initialExperience <= experience[i]:
                time += experience[i] - initialExperience + 1
                initialExperience += experience[i] - initialExperience + 1

            if initialEnergy > energy[i] and initialExperience > experience[i]:
                initialEnergy -= energy[i]
                initialExperience += experience[i]
                
        return time
        