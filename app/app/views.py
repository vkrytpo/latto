from .part2 import part2Tattslotto ,part2OzLatto ,part2PowerBall
from django.shortcuts import render

def index(request):
    '''default as home view of app accepting get and post request.'''
    if request.POST:
        game = request.POST.get('name')
        input_arr = request.POST.get('input_arr')
        
        if game =="1":
            first = part2Tattslotto("TatsLatto" ,"Saturday" ,1 ,45)
            first.setNumberOfRandoms(8)
            first.set_input(input_arr)
            first.createRandomNumbers()
            first.checkWinningNumbers()
            first.winners()
            msg=first.msg

        elif game=="2":
            second = part2OzLatto("OZ Latto" ,"Tuesday" ,1 ,45)
            second.setNumberOfRandoms(9)
            second.set_input(input_arr)
            second.createRandomNumbers()
            second.checkWinningNumbers()
            second.winners()
            msg=second.msg
        elif game=="3":
            third = part2PowerBall("Power ball" ,"Tuesday" ,1 ,45)
            third.set_input(input_arr)
            third.setNumberOfRandoms(7)
            third.createRandomNumbers()
            third.checkWinningNumbers()
            msg= third.msg
        ctx={'msg':msg}
        return render(request, 'index.html' ,ctx)
    else:
        return render(request, 'index.html')