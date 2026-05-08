class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # ---------- Prime factorization ----------
        def prime_factors(x):
            factors = set()

            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1

            if x > 1:
                factors.add(x)

            return factors

        # ---------- Check prime ----------
        def is_prime(x):
            if x < 2:
                return False

            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False

            return True

        # prime -> indices divisible by prime
        prime_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            for p in prime_factors(val):
                prime_to_indices[p].append(i)

        # ---------- BFS ----------
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        steps = 0

        while q:

            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # adjacent moves
                for nxt in [i - 1, i + 1]:
                    if 0 <= nxt < n and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

                # teleportation
                val = nums[i]

                if is_prime(val):

                    for nxt in prime_to_indices[val]:

                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    # IMPORTANT optimization
                    prime_to_indices[val].clear()

            steps += 1

        return -1