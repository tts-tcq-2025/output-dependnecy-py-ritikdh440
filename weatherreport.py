def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,   # >60
        'humidity': 26,
        'windSpeedKMPH': 52    # >50
    }

def sensorStubHighPrecipLowWind():
    return {
        'temperatureInC': 50,
        'precipitation': 70,   # >60
        'humidity': 40,
        'windSpeedKMPH': 30    # Low wind
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather

# This test will FAIL: it expects 'rain' but gets 'Sunny Day' because of the bug
def testRainy():
    weather = report(sensorStub)
    print("testRainy result:", weather)
    assert("rain" in weather)

# This test will FAIL: it expects rain/storm for high precipitation, but gets 'Sunny Day'
def testHighPrecipitation():
    weather = report(sensorStubHighPrecipLowWind)
    print("testHighPrecipitation result:", weather)
    assert("rain" in weather or "Partly" in weather or "Cloudy" in weather)

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)")
