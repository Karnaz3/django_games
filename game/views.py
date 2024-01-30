from django.shortcuts import render
from django.views import View
from .models import SPR, HeadTails
from .games import SPR as SPRGame, HeadTails as HeadTailsGame

class SPRView(View):
    template_name = 'spr.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_choice = request.POST.get('user_choice')
        gambling_points = int(request.POST.get('gambling_points'))

        spr_game = SPRGame()
        result = spr_game.execute(user_choice)

        SPR.objects.create(
            user_choice=user_choice,
            computer_choice=result['computer_choice'],
            winner=result['winner']
        )

        return render(request, 'spr.html', {'gambling_points': gambling_points, 'result': result})

class HeadTailsView(View):
    template_name = 'headtails.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        gambling_points = int(request.POST.get('gambling_points'))

        ht_game = HeadTailsGame()
        result = ht_game.execute()

        HeadTails.objects.create(result=result)

        return render(request, 'headtails.html', {'gambling_points': gambling_points, 'result': result})
