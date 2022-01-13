class deque:
    def __init__(self, s):
        self.items= list(s)

    def append(self, c):  # add a new entry to the right side
        self.items.append(c)

    def appendleft(self, c):  # add a new entry to the left side
        self.items.insert(0,c)

    def pop(self):  # return and remove the rightmost item
        return self.items.pop()

    def popleft(self):  # return and remove the leftmost item
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def right(self):
        return self.items[-1]

    def left(self):
        return self.items[0]


def check_palindrome(string):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

s = input()
print(check_palindrome(s))