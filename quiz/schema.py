import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields ='__all__'

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = '__all__'

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields ='__all__'

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields ='__all__'

class Query(graphene.ObjectType):
    all_question = graphene.Field(QuestionType, id=graphene.Int())
    all_answer = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_question(root, info, id):
        return Question.objects.get(pk=id)
    
    def resolve_all_answer(root, info, id):
        return Answer.objects.filter(question=id)

schema = graphene.Schema(query=Query)
