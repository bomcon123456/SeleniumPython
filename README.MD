# Selenium Course
# Summary 04/11/2019
## Section 13:
1. Learn how to install Selenium package for python
2. Selenium 3.x Update: Firefox must install driver manually
## Section 14:
1. Running test on Firefox, Chrome, Safari:
    - Add the driver using the constructor
    - Set the environment variable
    - use `.get(url)` to open a new window of the browser which access the url
    - [Firefox Driver](https://github.com/mozilla/geckodriver/releases) 
    - [Chrome Driver](https://chromedriver.chromium.org/downloads) 
    - [Safari Server Standalone](https://www.seleniumhq.org/download/): Must enable option Enable Automate Testing in the Develop section
2. Set Drivers in System Path
## Section 15:
1. Find element/elements by multiple locators:
    - id
    - name
    - class
    - tag
    - xpath
    - css selector
    - (partial) link text
2. Should use static, unique attribute or may cause NoSuchElementException or Fuzzy (because many elements have it)
3. Trivia: send_keys(): set value for the selected element, exceptions if element doesn't have value field.
4. find_by_class: only take one class name
5. If dynamic id, best option to deal: CSS -> Xpath -> Link Text -> Class

## Section 16:
1. Syntax: `tag[attribute=value]`
2. If attribute == 'id' or 'class', we can use this `#value`, `.value`
3. Multiple Class:
Using syntax: the value must be absolute: eg if we want to find `<input class="inputs aaa"\>` by (1)
-> `input[attribute='inputs aaa]`
Or: `.inputs.aaa`
4. Wildcards
    - ^: starting text
    - $: ending text
    - *: text contained
    - Syntax `tag[attribute<special>='value'`
    - eg: `input[class^='inputs']` will find all inputs having class which has value starting with 'inputs'
5. Finding Children

## Section 17:
If an element doesnt have an id, we should build a xpath to access it.

`/`: look for the element immediately insde the parent element

`//`: look for any child, nested-child element inside parent element

Syntax: `.//tag[@attribute='value']`  
1. Absolute vs Relative XPath:
    - Absolute starts from the root. e.g: `html/body/header/.../a`
        - Should not use because what if something changed and the path is ded
    - Relative: reduce the cost
2. Build Xpath by text
    - Absolute value: `//div[@class='hompage-hero]//a[text()='Enroll now]`
    - Contains:
        - Syntax: `tag[contains(attribute, 'value)]`
        - Eg: 
            - `//div[@class='hompage-hero]//a[contains(text(),'Enr')]`
            - `//div[@class='hompage-hero]//a[contains(@class, 'navbar-link') and contains(@href='sign_in')]`
    - Starts-with:
        - Syntax: `tag[starts-with(attribute, 'value')]`
        - Eg:
            - `//div[@id='navbar']//a[starts-with(@class, 'navbar-link')]`
3. Find Parent, Siblings Node
    - Parent:
        - Syntax: `xpath-to-elem//parent::<tag>`
        - Eg: `a[@href='/sign_in']//parent::li`
    - Preceding Siblings:
        - Syntax: `xpath-to-elem//preceding-sibling::<tag>`
        - Eg: `a[@href='/sign_in']//parent::li//preceding-sibling::li[1]`
    - Following Siblings:
        - Syntax: `xpath-to-elem//following-sibling::<tag>`
        - Eg: `a[@href='/sign_in']//parent::li//following-sibling::li[2]`
        
## Section 18:
1. Browser Interaction in `BrowserInteractions.py`
2. Element interaction (click, clear, send_keys)
3. implicitly_wait(x): wait x seconds if fail then try again
4. Deal with disabled, hidden element

## Section 19:
1. Get text from element: access the `text` field to get it
2. Get value of attribute: `get_attribute('attribute')`
3. Create a Wrapper Class

## Section 20:
1. Explicit Wait
    - Custom, wait until some condition is achieved
    - Some available expected conditions ...
    - Syntax:
    ```
        wait = WebDriverWait(driver, timeout, poll_frequency, ignore_exceptions=....)
        element = wait.until(EC....())
   ```
2. Implicit Wait
    - If elements are not immediately available -> tell Web Driver to poll the DOM for a certain # of time
    - Default = 0
    - Before throwing exception (because of not finding the element), it will wait for that # time
3. Create a ExplicitWait class

## Section 21:
1. Calendar Selector: remember to see the format of the calendar (maybe ul/li, table,..)
2. Autocomplete select by Xpath
3. Take screenshots `driver.save_screenshot(save_dir)`, may throw `NotADirectoryException`
4. Execute JS script `driver.execute_script(...)` 
    - Find size with `window.inner(Height|Width)`
    - Scroll down with `window.scrollBy(horizontal, vertical)` base on window size
    - Scroll element into view `element.scrollIntoView(true)`

## Section 22:
1. Switch window:
    - Each window win have a handle
    - Get current handle: `driver.current_window_handle`
    - Get all handles: `driver.window_handles`
    - Switch handle: `drive.switch_to.window(handle)`
    - Remember to switch back even if you close the pop-up one
2. IFrame:
    - Notice if part of a page is IFrame or not, if it does, you must switch frame first
    - Get the id of the Iframe then: `driver.switch_to.frame(id/name/index)`
    - Switch to normal: `driver.switch_to.default_content()`
3. Javascript popup:
    - Alert()/ Confirm() -> `driver.switch_to.alert`
        - This object will provide some function like `accept(), dismiss()`,..