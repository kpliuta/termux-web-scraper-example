# Termux Web Scraper Example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository provides example projects demonstrating the usage of the [termux-web-scraper](https://github.com/kpliuta/termux-web-scraper) framework, which enables running Selenium-based web scraping tasks on Android devices using Termux.

## Prerequisites

Before you can use the Termux Web Scraper, you need to have the following installed on your Android device:

*   **Termux:** You can download Termux from the [F-Droid](https://f-droid.org/en/packages/com.termux/) or [Google Play](https://play.google.com/store/apps/details?id=com.termux) store.
*   **Git:** You can install Git in Termux by running `pkg install git`.

You also need to:

*   **Disable Battery Optimization:** Disable battery optimization for Termux to prevent it from being killed by the Android system.
*   **Acquire a Wakelock:** Acquire a wakelock in Termux to prevent the device from sleeping while your scraper is running.
*   **Address Phantom Process Killing (Android 12+):** On Android 12 and newer, you may need to disable phantom process killing to prevent Termux from being killed. You can do this by running the following command in an ADB shell:
    ```bash
    ./adb shell "settings put global settings_enable_monitor_phantom_procs false"
    ```

## Project Structure

```
.
├── simple
│   ├── run.sh
│   └── ...
├── loop_error_ignore
│   ├── run.sh
│   └── ...
├── ...
```

This repository contains next example projects:

*   **`simple`:** A basic example that demonstrates how to perform a search on DuckDuckGo.
*   **`loop_error_ignore`:** An example that shows how to run the scraper in a loop and gracefully handle errors.

## Getting Started

1.  Get started by launching Termux on your Android device and cloning the repository:
    ```bash
    git clone https://github.com/kpliuta/termux-web-scraper-example.git
    ```

2.  Then, navigate to a project like `simple` and run the script:
    ```bash
    cd termux-web-scraper-example/simple
    ./run.sh
    ```
## Example Projects

### Simple

The `simple` example demonstrates a basic web scraping scenario. It navigates to [DuckDuckGo](https://duckduckgo.com/), searches for "Python Selenium Example", and saves a screenshot of the results.

### Loop with Error Ignoring

The `loop_error_ignore` example showcases how to run the scraper in a continuous loop while ignoring any errors that may occur during the process. This is useful for long-running scraping tasks that need to be resilient to network issues or unexpected page changes. The script attempts to navigate to a non-existent URL, and the `--loop-error-ignore` flag ensures that the loop continues to run even when the navigation fails.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
