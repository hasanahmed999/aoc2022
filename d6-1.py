with open('inputs/d6-1.txt') as file:
    signal = file.readlines()[0].strip()

    # Sliding win
    for i in range(len(signal) - 4 + 1 ):
        marker = signal[i:i+4]
        if len(set(marker)) == 4:
            print(i+4)
            break