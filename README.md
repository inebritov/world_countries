# The World Countries

API and web page made according to [this](http://cs629329.vk.me/v629329938/32a75/UpHITWBTRaU.jpg) "product requirements document".

Features:

1. Web-service can return following queries in format JSON/XML (use "`format`" GET parameter e.g. "`/api/countries/1/?format=json`"):
    1. World countries list (name, population) -- `/api/countries/`
    2. Specific country details by it's id -- `/api/countries/1`
    3. Top-5 most populated countries -- `/api/countries/?page_size=5&ordering=-population`
2. Web-page illustrating all queries from 1 paragraph -- index page

Also added admin interface (`/admin`) for convenient moderation.
