import driver

if __name__ == '__main__':
    print('Program start')

    # Run Driver
    driver = driver.get_driver()
    print('Get driver')
    
    print("------------------")
    # Open GitHub
    driver.get("https://github.com/")

    print(driver.title)

    # Close browser
    driver.quit()
    print("------------------")
    
    print('Program end')
