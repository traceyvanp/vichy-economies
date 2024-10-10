# Tellus (former Axereal)

This repository webscrapes the current and forecasted prices on sourced raw materials and exports to a dataframe.

<ls>
1.) Set up the Google Chrome driver and other installs.
2.) Run main.py (python main.py) to run code and get CSV
</ls>

## Install Google Chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt update
apt list --upgradable
sudo apt install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

## Install the ChromeDriver version that matches your installed Chrome version

wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.137/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
rm chromedriver-linux64.zip

## install selenium
pip install selenium
