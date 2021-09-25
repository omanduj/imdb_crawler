Crawler imdb move database
To use create virtual env
run virtual env and install scrapy
with scrapy downloaded go to folder with spiders folder
and type scrapy crawl "name_of_spider", in this case imdb

How to use:
1. Run poetry add
2. Cd into correct file and run "poetry run python flask_file.py" in the terminal

useful notes:
scrapy shell "website"
responce.css("div.XX::text").get()
virtualvenv
source venv/bin/activate

To execute endpoints:

For Posts:
    curl -X POST -H "Content-Type: application/json" -d '{"genre": "Short", "personal": "3"}' http://127.0.0.1:5000/movies/random/movie -> To obtain random movie
    curl -X POST -H "Content-Type: application/json" -d '{"my_rating": 10, "movie": "Sex, Fame and Murder: The Luka Magnotta Story"}' http://127.0.0.1:5000/movies/update/personal_rating -> To update personal rating for X movie
    curl -X POST -H "Content-Type: application/json" -d '{"genre": "Short"}' http://127.0.0.1:5000/movies/genre/runtime/average -> To find avg runtime for X genre
    curl -X POST -H "Content-Type: application/json" -d '{"genre": "Short"}' http://127.0.0.1:5000/movies/genre/average -> to find avg stars for X genre
    curl -X POST -H "Content-Type: application/json" -d '{"genre": "Crime"}' http://127.0.0.1:5000/movies/genre -> to find movies of X genre

For Gets:
    http://127.0.0.1:5000/movies -> Shows all info on all movies

Material Dashboard React Tweet
