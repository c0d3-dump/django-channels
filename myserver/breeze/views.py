from django.shortcuts import render
from django.http import JsonResponse
from . import somefunction
import threading
import time

# Create your views here.

def main(request):

  run_every_second()
  
  return render(request, 'breeze/main.html')


def run_every_second():
  somefunction.runFunction()
  
  # Schedule the function to run again in 1 second
  timer = threading.Timer(1.0, run_every_second)
  timer.start()