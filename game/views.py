from django.shortcuts import render
from django.views import View
from .models import SPR, HeadTails
from userprofiles.models import UserProfile
from django.shortcuts import render , redirect , get_object_or_404 

# from .games import SPR as SPRGame, HeadTails as HeadTailsGame

from .games import SPR_game as SRPGame, HeadTails_game as HeadTailsGame

class SPRView(View):
    template_name = 'spr.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_id = request.user.id
        user = get_object_or_404(UserProfile, pk=user_id)

        user_choice = request.POST.get('user_choice')
        gambling_points = int(request.POST.get('gambling_points'))

        
        if user.points < gambling_points:
            return render(request, 'spr.html', {'gambling_points': gambling_points, 'error': 'Not enough points'})

        spr_game = SRPGame()
        result = spr_game.execute(user_choice)

        user_choice = result['user_choice']
        computer_choice = result['computer_choice']
        winner = result['winner']


     # Validate points
        if winner == 'user':
            new_points = user.points + 1
            user.points = new_points
            user.save()
        else:
            new_points = user.points - 1
            user.points = new_points
            user.save()


        SPR.objects.create(user_choice=user_choice, computer_choice=computer_choice, winner=winner)
        return render(request, 'spr.html', {'gambling_points': gambling_points, 'result': result})


class HeadTailsView(View):
    template_name = 'headtails.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        user_id = request.user.id
        user = get_object_or_404(UserProfile, pk=user_id)

        gambling_points = int(request.POST.get('gambling_points'))

        if user.points < gambling_points:
            return render(request, 'headtails.html', {'gambling_points': gambling_points, 'error': 'Not enough points'})
        
        user_choice = str(request.POST.get('ht_choice'))

        print(request.POST)
        ht_game = HeadTailsGame()
        result = ht_game.execute()

        # Validate points
        if result == user_choice:
            new_points = user.points + 1
            user.points = new_points
            user.save()
        else:
            new_points = user.points - 1
            user.points = new_points
            user.save()


        HeadTails.objects.create(user_choice = user_choice, result=result)

        return render(request, 'headtails.html', {'gambling_points': gambling_points, 'result': result})
