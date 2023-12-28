from bs4 import BeautifulSoup
import scrapy
from pymongo import MongoClient

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://kora.online-kora.tv/']

    # Define MongoDB connection details as class attributes
    mongo_host = 'mongodb://abdassalam12:99785321Az@ac-0dj0lol-shard-00-00.qrw7hwl.mongodb.net:27017,ac-0dj0lol-shard-00-01.qrw7hwl.mongodb.net:27017,ac-0dj0lol-shard-00-02.qrw7hwl.mongodb.net:27017/?replicaSet=atlas-qi125l-shard-0&ssl=true&authSource=admin'
    mongo_port = 27017
    mongo_db = 'cora'
    mongo_collection = 'practis'

    def save_to_mongodb(self, right_team, left_team, match_time,match_info,dawri,team_logo_src,image_url0):
        client = None
        try:
            # Connect to MongoDB
            client = MongoClient(self.mongo_host, self.mongo_port)
            db = client[self.mongo_db]
            collection = db[self.mongo_collection]

            # Prepare the document to insert

            document = {
                'right_team': right_team,
                'left_team': left_team,
                'match_time': match_time,
                'match_info' :match_info,
                'dawri' : dawri,
                "team_logo_src" :team_logo_src,
                "team_logo_src0" :image_url0
            }

            # Insert into MongoDB
            
            collection.insert_one(document)

            self.log(f'Successfully inserted data into MongoDB: {document}')

        except Exception as e:
            self.log(f'Error inserting data into MongoDB: {e}')
        finally:
            if client:
                client.close()

 
    def parse(self, response):
        # Extract data from elements with class "alkooralive"
        alkooralive_elements = response.xpath('//div[@class="match-container commingsoon"]')
        alkooralive_elements0 = response.xpath('//div[@class="match-container soon"]')
        
        client = None
        try:
            # Connect to MongoDB
            client = MongoClient(self.mongo_host, self.mongo_port)
            db = client[self.mongo_db]
            collection = db[self.mongo_collection]
            
            collection.delete_many({})

        except Exception as e:
            self.log(f'Error inserting data into MongoDB: {e}')
        finally:
            if client:
                client.close()
        for alkooralive_element in alkooralive_elements0:

            # Extract data from elements with class "right-team"
            right_team_element = alkooralive_element.xpath('.//div[@class="right-team"]')
            left_team_element = alkooralive_element.xpath('.//div[@class="left-team"]')
            # Extract the img tag within the team-logo div
            team_logo_src = right_team_element.xpath('.//div[@class="team-logo"]//img').get()
            team_logo_src0 = left_team_element.xpath('.//div[@class="team-logo"]//img').get()
            if team_logo_src0:
                # Use BeautifulSoup to parse the img tag
                soup = BeautifulSoup(team_logo_src0, 'html.parser')
                # Extract the value of the data-src attribute
                image_url0 = soup.img.get('data-src')

            if team_logo_src:
                # Use BeautifulSoup to parse the img tag
                soup = BeautifulSoup(team_logo_src, 'html.parser')
                # Extract the value of the data-src attribute
                image_url = soup.img.get('data-src')
                print(image_url)
            
            # Extract data from elements with class "team-name" within each "right-team" element
            right_team_name_data = right_team_element.xpath('.//div[@class="team-name"]/text()').get()

            center_div = alkooralive_element.xpath('.//div[@class="match-center"]')
            match_timing = center_div.xpath(".//div[@class='match-timing']")
            match_time = match_timing.xpath(".//div[@id='match-time']/text()").get()


            left_team_name_data = left_team_element.xpath('.//div[@class="team-name"]/text()').get()
            match_info = alkooralive_element.xpath('.//div[@class="match-info"]/ul/li[2]/span/text()').get()
            dawri = alkooralive_element.xpath('.//div[@class="match-info"]/ul/li[3]/span/text()').get()

            
            yield {
                'right_team': right_team_name_data if right_team_name_data else None,
                'left_team': left_team_name_data if left_team_name_data else None,
                'match_time': match_time if match_time else None,
                'match_info':match_info ,
                'dawri' :dawri,
                "team_logo_src" :image_url,
                "team_logo_src0" :image_url0,
            }
            self.save_to_mongodb(right_team_name_data, left_team_name_data, match_time,match_info,dawri,image_url,image_url0)
        for alkooralive_element in alkooralive_elements:

            # Extract data from elements with class "right-team"
            right_team_element = alkooralive_element.xpath('.//div[@class="right-team"]')
            left_team_element = alkooralive_element.xpath('.//div[@class="left-team"]')
            # Extract the img tag within the team-logo div
            team_logo_src = right_team_element.xpath('.//div[@class="team-logo"]//img').get()
            team_logo_src0 = left_team_element.xpath('.//div[@class="team-logo"]//img').get()
            if team_logo_src0:
                # Use BeautifulSoup to parse the img tag
                soup = BeautifulSoup(team_logo_src0, 'html.parser')
                # Extract the value of the data-src attribute
                image_url0 = soup.img.get('data-src')

            if team_logo_src:
                # Use BeautifulSoup to parse the img tag
                soup = BeautifulSoup(team_logo_src, 'html.parser')
                # Extract the value of the data-src attribute
                image_url = soup.img.get('data-src')
                print(image_url)
            
            # Extract data from elements with class "team-name" within each "right-team" element
            right_team_name_data = right_team_element.xpath('.//div[@class="team-name"]/text()').get()

            center_div = alkooralive_element.xpath('.//div[@class="match-center"]')
            match_timing = center_div.xpath(".//div[@class='match-timing']")
            match_time = match_timing.xpath(".//div[@id='match-time']/text()").get()


            left_team_name_data = left_team_element.xpath('.//div[@class="team-name"]/text()').get()
            match_info = alkooralive_element.xpath('.//div[@class="match-info"]/ul/li[2]/span/text()').get()
            dawri = alkooralive_element.xpath('.//div[@class="match-info"]/ul/li[3]/span/text()').get()

            
            yield {
                'right_team': right_team_name_data if right_team_name_data else None,
                'left_team': left_team_name_data if left_team_name_data else None,
                'match_time': match_time if match_time else None,
                'match_info':match_info ,
                'dawri' :dawri,
                "team_logo_src" :image_url,
                "team_logo_src0" :image_url0,
            }
            self.save_to_mongodb(right_team_name_data, left_team_name_data, match_time,match_info,dawri,image_url,image_url0)
