from multiprocessing import Process
import time


def factorize(*number):
    result = []
    for num in number:
        item_result = []
        for i in range(1, num + 1):
            if num % i == 0:
                item_result.append(i)
        print(item_result)
        result.append(item_result)

    return tuple(item for item in result)


if __name__ == '__main__':

    args = (128, 255, 99999, 10651060)
    processes = []

    start = time.time()
    for arg in args:
        pr = Process(target=factorize, args=(arg,))
        pr.start()
        processes.append(pr)
    [el.join() for el in processes]

    end = time.time()
    print("Execution time: ", end - start)
