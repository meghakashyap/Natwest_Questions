candles_size = int(input("Enter the size of the candles: "))
def birthdayCakeCandles():
    count = 0

    candles_height = [int(x) for x in input("Enter the height of the candle: ").split(" ",candles_size)]
    
    max_height = max(candles_height)

    for i in candles_height:
        if i == max_height:
            count += 1
    return count

print(birthdayCakeCandles())

# candles max count