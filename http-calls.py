from seleniumwire import webdriver
import time

driver = webdriver.Firefox()
print('\nNew responses:\n')

for request in driver.requests:
    if request.response:
        print(request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
            )

del driver.requests
time.sleep(2)
print('\nNew responses:\n')

driver.get('https://www.google.com')
time.sleep(2)

for request in driver.requests:
    if request.response:
        print(request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
            )

del driver.requests
time.sleep(2)
print('\nNew responses:\n')

driver.get('https://www.keybr.com')
time.sleep(2)

for request in driver.requests:
    if request.response:
        print(request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
            )
