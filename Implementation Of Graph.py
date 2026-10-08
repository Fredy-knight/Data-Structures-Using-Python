class SocialNetwork:
    def __init__(self, users):
        self.users = sorted(list(set(users)))
        n = len(self.users)
        self.u2i = {u: i for i, u in enumerate(self.users)}
        self.i2u = {i: u for i, u in enumerate(self.users)}
        self.matrix = [[0] * n for _ in range(n)]
        self.list = {u: [] for u in self.users}

    def add_edge(self, u1, u2):
        if u1 in self.u2i and u2 in self.u2i:
            i1, i2 = self.u2i[u1], self.u2i[u2]
            self.matrix[i1][i2] = self.matrix[i2][i1] = 1

            if u2 not in self.list[u1]:
                self.list[u1].append(u2)

            if u1 not in self.list[u2]:
                self.list[u2].append(u1)

    def display(self):
        print("\nMATRIX:")
        print(" " * 10 + " ".join(f"{u:>8}" for u in self.users))

        for i, row in enumerate(self.matrix):
            print(f"{self.i2u[i]:>8} | " + " ".join(f"{v:>8}" for v in row))

        print("\nLIST:")
        for u, f in self.list.items():
            print(f"{u} -> {f}")


def main():
    net = SocialNetwork(input("Users: ").strip().split())

    while True:
        inp = input("Connection: ").strip()

        if inp.lower() == "done":
            break

        p = inp.split()

        if len(p) == 2:
            net.add_edge(p[0], p[1])

    net.display()


if __name__ == "__main__":
    main()
