class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        # Step 1: users ko set me convert karo
        langs = [set(l) for l in languages]

        # Step 2: find users jinko teach karna ho sakta hai
        to_teach = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if langs[u].intersection(langs[v]) == set():
                to_teach.add(u)
                to_teach.add(v)

        if not to_teach:
            return 0  # sab already communicate karte hain

        # Step 3: har language try karo
        res = float('inf')
        for l in range(1, n+1):
            # count how many in to_teach already know l
            know = sum(1 for user in to_teach if l in langs[user])
            need = len(to_teach) - know
            res = min(res, need)

        return res
