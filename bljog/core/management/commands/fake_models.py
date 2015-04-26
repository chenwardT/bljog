from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from faker import Faker

from blog.models import Post
from comments.models import Comment

User = get_user_model()


class Command(BaseCommand):
    help = "Populate models with fake data for testing"

    def add_arguments(self, parser):
        parser.add_argument('num_posts', nargs='+', type=int)

    # TODO: Generate Comment objects.
    def handle(self, *args, **options):
        fake = Faker()

        # TODO: Dynamic authors.
        user = User.objects.get(username='chenward')

        inserted_posts = []

        for x in range(options['num_posts'][0]):
            post_args = {'author': user,
                         'title': fake.sentence(),
                         'body': '\n\n'.join(fake.paragraphs())}
            post = Post(**post_args)
            post.save()
            inserted_posts.append(post)

        # TODO: Formatting
        self.stdout.write('Inserted the following objects:')
        for x in inserted_posts:
            self.stdout.write('%s' % x)