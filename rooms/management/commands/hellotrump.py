from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command says hello to Trump."

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do you want to say hello")

    def handle(self, *args, **options):
        print(args, options)
        times = options.get("times")
        for t in range(0, int(times)):
            print("Hello, mr.Trump!")
            # self.stdout.write(self.style.SUCCESS("Hello, mr.Trump!"))
            # self.stdout.write(self.style.ERROR("Hello, mr.Trump!"))
            # self.stdout.write(self.style.WARNING("Hello, mr.Trump!"))
