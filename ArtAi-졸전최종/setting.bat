@echo off
call conda create -n artAi python=3.9.12
call conda activate artAi
call pip install pyperclip googletrans==4.0.0-rc1 pyqt5 selenium webdriver_manager packaging