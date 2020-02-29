from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import User, Node
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def checkUserStatus(request):
    reqData = json.loads(request.body.decode('UTF-8'))
    userId = reqData['uId']
    user = User.objects.get(userId=userId)
    path = list(user.path.all())
    responseLevel = 0
    responseStatus = True
    for node in path:
        responseStatus = responseStatus and node.status
        responseLevel = max(responseLevel, int(node.qualityLevel))
    
    return JsonResponse({"status":responseStatus, "level" : responseLevel})

def getDefectiveNodes(request):
    allNodes = Node.objects.all()
    defectiveNodes = []
    for node in allNodes:
        if node.status is False:
            temp = {}
            temp['id'] = node.nodeId
            temp['level'] = node.qualityLevel
            defectiveNodes.append(temp)

    return JsonResponse({"defectiveNodes" : defectiveNodes} )

@csrf_exempt
def checkAutoCut(request):
    reqData = json.loads(request.body.decode('UTF-8'))
    userId = reqData['uId']
    user = User.objects.get(userId=userId)
    tapNode = user.tapNode
    if tapNode.status is False and int(tapNode.level)>=3:
        responseStatus = True
    else:
        responseStatus = False
    
    return JsonResponse({"status":responseStatus, "level" : tapNode.qualityLevel})
