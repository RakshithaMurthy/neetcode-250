class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        # Step 1: initialize
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

        # Step 2: union emails in same account
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                union(first_email, email)

        # Step 3: group by root
        groups = {}
        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        # Step 4: build result
        res = []
        for root in groups:
            name = email_to_name[root]
            res.append([name] + sorted(groups[root]))

        return res