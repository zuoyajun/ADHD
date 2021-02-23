#!bin/bash
time=$(date "+%Y-%m-%d")
rm -rf /usr/local/tomcat/webapps/report/firefox$time
mv /root/.jenkins/workspace/ADHD-selenium-web-Chrome/report/firefox /usr/local/tomcat/webapps/report/firefox$time