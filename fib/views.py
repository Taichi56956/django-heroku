from django.http import JsonResponse

def fibonacci_view(request, n):
    if int(n) < 0:
        return JsonResponse({'status':400, 'message': 'bad request'}, status=400)
    elif int(n) == 0:
        return JsonResponse({'result': 0})
    elif int(n) == 1:
        return JsonResponse({'result': 1})

    a = 0
    b = 1
    for _ in range(int(n) - 1):
        a, b = b, a + b
    return JsonResponse({'result': b})