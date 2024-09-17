#install Google Chrome in your Codespace

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt update
apt list --upgradable
sudo apt install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# Install the ChromeDriver version that matches your installed Chrome version

#old: wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.112/linux64/chromedriver-linux64.zip
wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.137/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
rm chromedriver-linux64.zip

pip install selenium



