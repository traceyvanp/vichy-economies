# Vichy-economies

This repository webscrapes business data to a dataframe.

<ls>
<li>1.) Set up the Google Chrome driver and other installs.</li>
<li>2.) Run main.py (python main.py) to run code and get CSV.</li>
</ls>

## Install Google Chrome

<ls>
<li>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb</li>
<li>sudo apt update</li>
<li>apt list --upgradable</li>
<li>sudo apt install -y ./google-chrome-stable_current_amd64.deb</li>
<li>rm google-chrome-stable_current_amd64.deb</li>
</ls>

## Install the ChromeDriver version that matches your installed Chrome version

<ls>
<li>wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.137/linux64/chromedriver-linux64.zip</li>
<li>unzip chromedriver-linux64.zip</li>
<li>sudo mv chromedriver-linux64/chromedriver /usr/local/bin/</li>
<li>rm chromedriver-linux64.zip</li>
</ls>

## install selenium
pip install selenium
