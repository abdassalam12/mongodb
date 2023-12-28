from pymongo import MongoClient
from django.shortcuts import render,redirect,HttpResponse
from django.core.management import call_command
import threading
from pymongo.errors import PyMongoError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def run_spider(request):
    # Run the Scrapy spider
    call_command('run_spider')  # Replace 'run_spider' with the actual name of your management command

    # You can add additional logic or render a template as needed
    return redirect('info')
def info(request):
    try:
        # Establish a connection to MongoDB
        client = MongoClient('mongodb://abdassalam12:99785321Az@ac-0dj0lol-shard-00-00.qrw7hwl.mongodb.net:27017,ac-0dj0lol-shard-00-01.qrw7hwl.mongodb.net:27017,ac-0dj0lol-shard-00-02.qrw7hwl.mongodb.net:27017/?replicaSet=atlas-qi125l-shard-0&ssl=true&authSource=admin')

        # Access the 'cora' database
        db = client['cora']

        # Access the 'practis' collection within the database
        collection = db['practis']

        # Query the collection and retrieve all data
        result_cursor = collection.find()

        # Process the retrieved data (you can customize this part based on your needs)
        # For example, converting the cursor to a list
        result_list = list(result_cursor)

        # Pass the data to the template
        return render(request, 'info.html', {'result_list': result_list})
    except PyMongoError as e:
        # Handle MongoDB connection errors
        print(f'MongoDB error: {e}')
        return HttpResponse('Error connecting to MongoDB or querying the collection.')