from collections import deque

class SocialNetwork:
    def __init__(self, users):
        self.users = sorted(list(set(users)))
        self.list = {u: [] for u in self.users}

    def add_edge(self, u1, u2):
        if u1 in self.list and u2 in self.list:
            if u2 not in self.list[u1]:
                self.list[u1].append(u2)

            if u1 not in self.list[u2]:
                self.list[u2].append(u1)

    def traverse(self, start):
        if start not in self.list:
            return [], []

        b_vis = {start}
        b_q = deque([start])
        b_order = []

        while b_q:
            curr = b_q.popleft()
            b_order.append(curr)

            for nxt in self.list[curr]:
                if nxt not in b_vis:
                    b_vis.add(nxt)
                    b_q.append(nxt)

        d_vis = {start}
        d_st = [start]
        d_order = []

        while d_st:
            curr = d_st.pop()
            d_order.append(curr)

            for nxt in sorted(self.list[curr], reverse=True):
                if nxt not in d_vis:
                    d_vis.add(nxt)
                    d_st.append(nxt)

        return b_order, d_order


def main():
    net = SocialNetwork(input("Users: ").strip().split())

    while True:
        inp = input("Connection: ").strip()

        if inp.lower() == "done":
            break

        p = inp.split()

        if len(p) == 2:
            net.add_edge(p[0], p[1])

    start = input("Start traversal from: ").strip()

    bfs, dfs = net.traverse(start)

    print("BFS:", bfs)
    print("DFS:", dfs)
    print("Reachable:", [u for u in bfs if u != start])


if __name__ == "__main__":
    main()
