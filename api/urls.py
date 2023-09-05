from django.urls import path
from app.views import getTodos,getTodo,updateTodo,createTodo,deleteTodo,partialTodoUpdate
urlpatterns = [
    path('api/todo',getTodos),
    path('api/todo/create',createTodo),
    path('api/todo/<int:id>',getTodo),
    path('api/todo/update/<int:id>',updateTodo),
    path('api/todo/delete/<int:id>',deleteTodo),
    path('api/todo/partial-update/<int:id>',partialTodoUpdate),
    
]
