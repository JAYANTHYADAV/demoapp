import json
import time
from django.http import HttpResponse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect, render, Http404

def index(request):
    if request.method == "GET":
        context = {}
        return render(request, 'test1.html', context)

# def fibonacci(n):     
#     first = 0
#     second = 1
#     if n < 0: 
#         return "Incorrect Input" 
#     elif n == 0: 
#         return first 
#     elif n == 1: 
#         return second 
#     else: 
#         for i in range(2,n+1): 
#             temp = first + second 
#             first = second 
#             second = temp 
#         return second

# @csrf_exempt
# def fiboData(request):
#     try:
#         data = json.loads(request.body)
#         start = time.time()
#         fibo_data = fibonacci(int(data["number"]))
#         print(fibo_data)
#         elapsed_time = (time.time() - start) 
#         # return render_to_response('test1.html',
#         #     {
#         #         'status':'success',
#         #         'fibo_data':fibo_data,
#         #         'time_consumed':elapsed_time
#         #     }

#         # )
#         return HttpResponse(json.dumps({'status':'success','fibo_data':fibo_data,'time_consumed':elapsed_time}))
#     except Exception as e:
#         print ("Exception in fiboData : " + str(e))
#         return HttpResponse(json.dumps({'status':'error'}))
