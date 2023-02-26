# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 10⁶ 
#  
# 
#  Related Topics 数组 数学 枚举 数论 👍 1023 👎 0
from math import sqrt


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        check = [True] * n
        primes = []
        for i in range(2, n):
            if check[i]:
                primes.append(i)
            j = 0
            while j < len(primes) and i * primes[j] < n:
                check[i * primes[j]] = False
                if i % primes[j] == 0:
                    break
                j += 1

        return len(primes)


# leetcode submit region end(Prohibit modification and deletion)
Solution().countPrimes(10)
