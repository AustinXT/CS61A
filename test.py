import heapq
from random import randint


class SocksHeaps:
    """socks heap
    every day wear the cleanest socks.
    and every day the socks weard will be dirtier by a random integer from 1 to 10.
    when all the socks reach the dirty threshold(100), they will be threw away.
    """

    def __init__(self, threshold=100, socks_num=7, name="Xianxian"):
        self.threshold = threshold
        self.socks_num = socks_num
        self.name = name
        self.heaps = [0]*socks_num
        self.sock = 0
        self.day = 0
        print(threshold, socks_num, name)

    def daily(self):
        print(f"The {self.day} begins...")
        print(f"{self.name} get a sock of {self.sock} dirty value.")
        random_num = randint(1, 10)
        self.sock += random_num
        print(
            f"{self.name} wear the sock for a day, and the get {random_num} more dirty value and becom {self.sock}.")
        heapq.heappush(self.heaps, self.sock)

    def run(self):
        heapq.heapify(self.heaps)
        print(self.heaps)
        self.sock = heapq.heappop(self.heaps)
        while self.sock < 100:
            self.daily()
            self.day += 1
            print("Here this the socks heaps")
            print(self.heaps)


if __name__ == "__main__":
    xiansocks = SocksHeaps(20)
    xiansocks.run()
