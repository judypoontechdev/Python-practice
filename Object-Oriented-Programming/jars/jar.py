class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if not self.size + n <= self.capacity:
            raise ValueError('Cookies added have exceeded the current capacity!')
        self.size += n

    def withdraw(self, n):
        if not n <= self.size:
            raise ValueError("You've got too many cookies!")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            int(capacity)
        except ValueError:
            raise ValueError('Pls input integers!')
        else:
            if not capacity >= 0:
                raise ValueError

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size

def main():
    jar = get_jar()
    print(jar)

def get_jar():
    capacity = int(input('capacity: '))
    return Jar(capacity)

if __name__ == '__main__':
    main()
