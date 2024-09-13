def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Statistics class to make some maths operations'''
    operations_functions = {
        'mean': calculate_mean,
        'median': calculate_median,
        'quartile': calculate_quartile,
        'std': calculate_std,
        'var': calculate_variance
    }
    numbers = []

    for num in args:
        if not isinstance(num, int):
            print('Program only accepts integer and key/value arguments')
            return
        numbers.append(num)

    for key, value in kwargs.items():
        if value in operations_functions:
            if len(numbers) == 0:
                print('ERROR')
            else:
                function = operations_functions[value]
                print(function(numbers))


def calculate_mean(nums: list):
    '''return mean in a list of numbers'''
    mean = sum(nums) / len(nums)
    return mean


def calculate_median(nums: list):
    '''return median in a list of numbers'''
    nums.sort()
    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        mid = n // 2
        return (nums[mid] + nums[mid - 1]) / 2


def calculate_quartile(nums: list):
    '''return q1 and q2 from a list of numbers'''
    nums.sort()
    n = len(nums)
    q1 = int(n * 0.25)
    q3 = int(n * 0.75)
    return [float(nums[q1]), float(nums[q3])]


def calculate_std(nums: list):
    '''return standard deviation from a list of numbers'''
    return calculate_variance(nums) ** 0.5


def calculate_variance(nums: list):
    '''return variance from a list of numbers'''
    mean = calculate_mean(nums)
    var_list = [(num - mean) ** 2 for num in nums]
    return calculate_mean(var_list)
