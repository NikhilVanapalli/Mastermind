from django.shortcuts import render,redirect
from .nm import Mastermind
import tkinter as mastermind
import random
import collections
# Create your views here.
def home(request):
    return render(request,'main/home.html')

def trial(request):
    root = mastermind.Tk()
    game = Mastermind(root)
    root.mainloop()
    return redirect('/main/home')
