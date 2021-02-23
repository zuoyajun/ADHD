#!bin/bash
time=$(date "+%Y-%m-%d")
rm -rf /usr/local/tomcat/webapps/report/chrome
mv /root/.jenkins/workspace/ADHD-selenium-web-chrome/report/chrome /usr/local/tomcat/webapps/report/chrome$time