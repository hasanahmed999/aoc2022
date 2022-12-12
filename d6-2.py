with open('inputs/d6-1.txt') as file:
    signal = file.readlines()[0].strip()

    # Sliding win
    for i in range(len(signal) - 14 + 1 ):
        marker = signal[i:i+14]
        if len(set(marker)) == 14:
            print(i+14)
            break