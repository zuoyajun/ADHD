#!bin/bash
time=$(date "+%Y-%m-%d")
rm -rf /usr/local/tomcat/webapps/report/chrome$time
mv /root/.jenkins/workspace/ADHD-selenium-web-Chrome/report/chrome /usr/local/tomcat/webapps/report/chrome$time