from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serilalizers import TodoSerializer
from .models import Todo


@api_view(["GET"])
def getTodos(request):
    todo_obj = Todo.objects.all().order_by("-date_created")
    if request.method == "GET":
        serialize = TodoSerializer(todo_obj, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getTodo(request, id):
    try:
        todo_obj = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize = TodoSerializer(todo_obj)
        return Response(serialize.data, status=status.HTTP_200_OK)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateTodo(request, id):
    try:
        todo_obj = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        data = request.data
        serialize = TodoSerializer(todo_obj, data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def partialTodoUpdate(request, id):
    try:
        todo_obj = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        data = request.data
        serialize = TodoSerializer(todo_obj, data=data, partial=True)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteTodo(request, id):
    try:
        todo_obj = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        todo_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def createTodo(request):
    if request.method == "POST":
        data = request.data
        serialize = TodoSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
