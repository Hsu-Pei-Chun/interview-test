def count_no14_up_to(N: int) -> int:
    """
    回傳從 0 到 N 之間，不含 '14' 的整數個數
    """

    digits = list(map(int, str(N)))  # 轉成位數
    n_len = len(digits)
    
    # dp(pos, prev, is_tight) 記憶化表
    # -1 代表還沒計算
    # dp 會回傳：從第 pos 位處理到末位，
    #           不會產生 '14' 的 valid 數量
    # prev = 前一位的 digit (若沒有上一位，給 -1 做為 "無意義" 狀態)
    from functools import lru_cache

    @lru_cache(None)
    def dfs(pos: int, prev: int, is_tight: bool) -> int:
        # pos 走到頭，表示一個完整數字產生，且還沒遇到 '14'
        if pos == n_len:
            return 1

        limit = digits[pos] if is_tight else 9
        total_count = 0

        for dig in range(limit + 1):
            # 假如上一位是 1，這一位 dig 是 4，代表出現 '14' → 這路徑直接跳過
            if prev == 1 and dig == 4:
                continue

            # 下一位是否還 tight，需看本位是否用到 limit
            next_tight = is_tight and (dig == limit)

            total_count += dfs(pos + 1, dig, next_tight)

        return total_count

    return dfs(0, -1, True)

def count_with14_in_1_to(N: int) -> int:
    """
    回傳從 1 到 N 之間，包含 '14' 的數字個數
    """
    if N <= 0:
        return 0
    # 從 0..N 之間不含 '14' 的個數
    no14_count = count_no14_up_to(N)
    # 從 1..N 含 '14' 的個數 = N + 1 - 不含 '14'（因為包含 0）
    return (N + 1) - no14_count

# ----------------------------------
# 以下示範計算題目需求
# ----------------------------------

# 1) 從 1 ~ 10,000 含 '14' 有多少?
ans1 = count_with14_in_1_to(10_000)
print("1 ~ 10,000 含 '14' 的個數 =", ans1)

# 2) 從 1 ~ 10,000,000 含 '14' 有多少?
ans2 = count_with14_in_1_to(10_000_000)
print("1 ~ 10,000,000 含 '14' 的個數 =", ans2)

# 3) 從 1 ~ 10,000,000,000 含 '14' 有多少?
ans3 = count_with14_in_1_to(10_000_000_000)
print("1 ~ 10,000,000,000 含 '14' 的個數 =", ans3)
