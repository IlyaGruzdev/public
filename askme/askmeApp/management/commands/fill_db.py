from django.core.management.base import BaseCommand
from askmeApp.models import *
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Fill db with faker'

    fake = Faker()

    def create_users(self, count):
        print('Start creating users')
        words = list(set(self.fake.words(nb=10000)))
        random.shuffle(words)
        usernames = []
        i = 0
        while i < count:
            for first_word in words:
                for second_word in words:
                    usernames.append(first_word + second_word)
                    i += 1

        users = [User(username=usernames[i],
                      email=self.fake.email(),
                      password=self.fake.password())
                 for i in range(count)]

        print('Saving users')
        User.objects.bulk_create(users)

        print('Users are done')

    def create_questions(self, count):
        users = User.objects.all()

        print('Start creating questions')
        questions = [Question(title=self.fake.sentence(),
                              text=self.fake.text(),
                              user=random.choice(users))
                     for _ in range(count)]

        print('Saving questions')
        Question.objects.bulk_create(questions)

        print('Questions are done')

    def create_tags(self, count):
        print('Start creating tags')
        words = list(set(self.fake.words(nb=10000)))
        random.shuffle(words)
        names = []
        i = 0
        while i < count:
            for first_word in words:
                for second_word in words:
                    names.append((first_word + second_word)[:20])
                    i += 1

        tags = [Tag(name=names[i]) for i in range(count)]

        print('Saving tags')
        Tag.objects.bulk_create(tags)

        print('Tags are done')

    def put_tags_on_questions(self):
        tags = Tag.objects.all()

        print('Puttins tags on questions')
        for question in Question.objects.all():
            for tag in random.choices(tags, k=3):
                question.tags.add(tag.id)
                question.save()

        print('Tags on questions are done')

    def create_answers(self, count):
        users = User.objects.all()
        questions = Question.objects.all()

        print('Start creating answers')
        answers = [Answer(text=self.fake.text(),
                          question=random.choice(questions),
                          user=random.choice(users))
                   for _ in range(count)]

        print('Saving answers')
        Answer.objects.bulk_create(answers)

        print('Answers are done')

    def create_question_votes(self, count):
        users = User.objects.all()
        questions = Question.objects.all()

        print('Start creating question votes')
        question_votes = [QuestionVote(question=random.choice(questions),
                                       user=random.choice(users),
                                       vote=random.choice([-1, 1]))
                          for _ in range(count)]

        print('Saving question votes')
        QuestionVote.objects.bulk_create(question_votes)

        print('Question votes are done')

    def create_answer_votes(self, count):
        users = User.objects.all()
        answers = Answer.objects.all()

        print('Start creating answer votes')
        answers_votes = [AnswerVote(answer=random.choice(answers),
                                    user=random.choice(users),
                                    vote=random.choice([-1, 1]))
                         for _ in range(count)]

        print('Saving answer votes')
        AnswerVote.objects.bulk_create(answers_votes)

        print('Answer votes are done')

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        ratio = options['ratio']

        users_count = ratio
        questions_count = ratio * 10
        tags_count = ratio
        answers_count = ratio * 100
        question_likes_count = ratio * 50
        answer_likes_count = ratio * 150

        self.create_users(users_count)
        self.create_questions(questions_count)
        self.create_tags(tags_count)
        self.put_tags_on_questions()
        self.create_answers(answers_count)
        self.create_question_votes(question_likes_count)
        self.create_answer_votes(answer_likes_count)
