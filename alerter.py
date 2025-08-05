alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Always returns 200 (OK) in production/stub
    return 200

def alert_in_celcius(farenheit, network_alert=network_alert_stub):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 0  # BUG: should increment, but doesn't

# Test stub that simulates a failure
def failing_stub(celcius):
    print(f"Fake alert failed at {celcius} C")
    return 500  # Simulate alert failure

# Test to expose bug
def test_alert_failure_count():
    global alert_failure_count
    alert_failure_count = 0  # Reset before test
    
    # Call with failing stub twice
    alert_in_celcius(400.5, failing_stub)
    alert_in_celcius(303.6, failing_stub)
    
    # Expect count to be 2, but it'll still be 0 → Test will fail
    assert alert_failure_count == 2, f"Expected 2 failures, got {alert_failure_count}"

if __name__ == "__main__":
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)
    print(f'{alert_failure_count} alerts failed.')

    # Run the test — this will fail
    test_alert_failure_count()
    
    print("All is well (maybe!)")
