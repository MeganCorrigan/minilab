
class Fibonacci:

    def __init__(self, series):

        if series < 2 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);


    def calc_series(self):
        limit = self._series
        f = 1  # starting factorial number
        x = 1
        while limit >= x:  # counts up to the limit
            self.set_data(f) # adds current number to the list to print at end
            f = self.recursive_factorial(x) # calculates factorial through recursion
            x += 1 # updates to be the next count

    def recursive_factorial(self, num): # calculates the factorial of num by getting num-1 and multiple that by num
        if num > 1:
            return num * self.recursive_factorial(num - 1)
        else:
            return num # base case (if condition fails then break out of recursive loop)

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 20
    '''Constructor of Class object'''
    fibonacci = Fibonacci(n)

    '''Using getters to obtain data from object'''
    print(f"Factorial number for {n} = {fibonacci.number}")
    print(f"Factorial series for {n} = {fibonacci.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Factorial sequence {i + 1} = {fibonacci.get_sequence(i)}")

