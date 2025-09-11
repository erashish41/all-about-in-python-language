# Decorator
print(">>>>>>>>>1>>>>>>>>>>>")
# basic decorator
def decorator(func):
    def wrapper():
        print("Transaction Initialized")
        func()
        print("Transaction Finished")
    return wrapper

@decorator
def hello():
    print("Transaction Internal started")
hello()
    
print(">>>>>>>>>2>>>>>>>>>>>")
#  too add
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Transaction Initialized")
        result = func(*args, **kwargs)
        print("Transaction Finished")
        return result
    return wrapper

@decorator
def add(a,b):
    return a + b
print(add(2,5))

@decorator
def hello():
    print("Transaction Internal started")
hello()

print(">>>>>>>>>3>>>>>>>>>>>")
# for interview
def decorator_func(func):
    def wrapper_func():
        print("wrapper func worked")
        return func()
    return wrapper_func

@decorator_func
def display():
    print("display work")
display()

print(">>>>>>>>>4>>>>>>>>>>>")


# decorator with Cron Job (automated jobs)
import time
from datetime import datetime

def log_datetime_decorator(func):
    def wrapper_func():
        print(f"Function: {func.__name__}")
        print(f"Run on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        print("------------------")
        func()
    return wrapper_func

@log_datetime_decorator
def daily_cron_job():
    time.sleep(9)
    print("daily cron job has finished")
    
@log_datetime_decorator
def weekly_cron_job():
    time.sleep(61.5)
    print("weekly cron job has finished")
    
@log_datetime_decorator
def monthly_cron_job():
    time.sleep(2.1)
    print("monthly cron job has finished")

daily_cron_job()
weekly_cron_job()
monthly_cron_job()
