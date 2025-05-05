class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            if email1 not in parent:
                parent[email1] = email1

            if email2 not in parent:
                parent[email2] = email2

            root1 = find(email1)
            root2 = find(email2)

            if root1 != root2:
                parent[root2] = root1

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email, email)
                email_to_name[email] = name

        roots = defaultdict(list)
        for email in email_to_name:
            root = find(email)
            roots[root].append(email)

        result = []
        for root, emails in roots.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result