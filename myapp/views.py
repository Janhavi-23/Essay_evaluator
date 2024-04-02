from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from openai import OpenAI
from .forms import EssayForm
from django.http import JsonResponse
import os

# Create your views here.

def myapp(request):
    return render(request, "myapp.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def submit_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            essay = form.cleaned_data['essay']

            print(title, essay)
            # Process your essay here
            OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

            client = OpenAI(api_key=OPENAI_API_KEY)

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "For the given essay: A)Count the spelling errors in the essay. B) Does the given title align with the essay contents? (yes/no) C)An essay score out of 10. D)Provide brief feeback to the essay in less then 100 words. \n Your response should consists name of the point (example A)Number of errors : , B)Content related to title: , C) Score: , D)Feedback: ) followed by your response for each point."},
                    {"role": "user", "content": f"Title : {title}"},
                    {"role": "user", "content": f"Essay: {essay}"}
                ]
            )

            response_data = {
                "message": completion.choices[0].message.content,
                'status': 200
            }

            print(response_data)
            return JsonResponse(response_data)
        else:
            return JsonResponse({"errors": "Method Not Allowed"}, status=400)
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)

    
    

