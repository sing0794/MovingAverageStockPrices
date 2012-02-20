#MovingAverages.py

from dumbo import main
import re

def mapper0( key, value ):
    rec = value.split(',')
    timestring = rec[2]
    yield rec[1], (timestring, rec[8])

def reducer0( key, values ):
    slidingWindow = []
    slidingWindowSize = 30
    slidingWindowCounter = 0
    valuesCounter = 0
    for value in sorted(list(values)):
        pricedate = value[0]
        if len( slidingWindow ) < slidingWindowSize:
            slidingWindow.append(float(value[1]))
        if len( slidingWindow ) == slidingWindowSize:
            slidingWindow[slidingWindowCounter] = float(value[1])
            averageprice = sum(slidingWindow) / slidingWindowSize
            yield key, (pricedate, averageprice)
        valuesCounter += 1
        slidingWindowCounter = valuesCounter%slidingWindowSize

def runner( job ):
    job.additer( mapper0, reducer0 )

def starter( prog ):
    return

if __name__ == "__main__":
    main( runner, starter )
