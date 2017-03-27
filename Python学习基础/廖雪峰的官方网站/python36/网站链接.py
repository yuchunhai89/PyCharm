__author__ = 'yuchunhai'
import webbrowser
import selenium
from selenium import webdriver
webProfileDir = r"C:\Users\yuchunhai\AppData\Roaming\Mozilla\Firefox\Profiles\hd1cgcrn.default"
driver = webdriver.Firefox(webProfileDir)
driver.get("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
