import time
from multiprocessing import Pool, process

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            if line != "":
                all_data.append(line)
            else:
                break


def main():

    file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    time_BS = time.time()
    """
    for file in file_list:
        read_info(file)
         """



    with Pool(processes = 4) as pool:
        it = pool.imap(read_info, file_list)
    time_AS = time.time()
    print(time_AS - time_BS)

if __name__ == "__main__":
    main()