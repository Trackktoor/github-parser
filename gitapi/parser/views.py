from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from parser.parser import get_data


class UserReps(APIView):
    def get(self, github_username):
        url = ''.join(f"https://github.com/{github_username}?tab=repositories")
        data = get_data(url)
        print(github_username)
        return Response(data)