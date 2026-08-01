class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # whose turn it is
        # turn is divisible by 2 player 1 other wise 2
        # left and right poitners
        # player 1 points and player 2 points
        # make left and right indexes inclusive

        def dfs(turn, left, right, player_1_score, player_2_score):
            if right < left:
                return player_1_score >= player_2_score
            if turn % 2 == 0:
                return dfs(turn+1, left+1,right, player_1_score + nums[left], player_2_score) or dfs(turn+1, left,right-1, player_1_score + nums[right], player_2_score)
            else:
                return dfs(turn+1, left+1,right, player_1_score, player_2_score + nums[left]) and dfs(turn+1, left,right-1, player_1_score, player_2_score+ nums[right])

        return dfs(0, 0, len(nums)-1, 0, 0 )