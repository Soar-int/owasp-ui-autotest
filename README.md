# owasp-ui-autotest
This project automates interactions with the Juice Shop application using Selenium WebDriver. It uses Python to manage browser sessions and conduct automated testing.

## Prerequisites

1. Python 3.8 or higher
2. Google Chrome (latest version)
3. Required Python libraries:
    ```
    selenium
    webdriver-manager
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Soar-int/owasp-ui-autotest.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

## Usage

1. Run the automation script:
    ```bash
    pytest
    ```

## Components

### `config.py`
Holds application and user configuration settings.

### `driver_manager.py`
Manages the browser setup and initializes WebDriver sessions.