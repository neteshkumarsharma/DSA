class Solution:
    def rankTeams(self, votes: List[str]) -> str:#
        n = len(votes[0])  
        counts = {team: [0] * n for team in votes[0]}
        
        for vote in votes:
            for i, team in enumerate(vote):
                counts[team][i] += 1
        
        teams = sorted(counts, key=lambda t: ([-x for x in counts[t]], t))
        return ''.join(teams)
