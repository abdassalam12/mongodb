import os
from django.core.management.base import BaseCommand
from subprocess import run

class Command(BaseCommand):
    help = 'Run the Scrapy spider'
    def run(self, *args, **options):
        # Start the Scrapy spider in a separate thread
        spider_thread = threading.Thread(target=self.run_spider)
        spider_thread.daemon = True
        spider_thread.start()

        # Call the original runserver command
        super().run(*args, **options)
    def handle(self, *args, **options):
        # Change to the Scrapy project directory
        os.chdir('C:\\django\\first_project\\spark\\scrapy\\firstScrapy\\firstScrapy')

        # Run the Scrapy crawl command
        run(['scrapy', 'crawl', 'spider'])
