
- Global news intelligence platform
- The project is a real time intelligence system that 
	- collects
	- classifies
	- visualizes 
		- news form multiple countries

- The goal is to break away from mindless scrolling and create a live  dashboard that helps users understand the differences in how different countries report on the same global events

The countries we start out with will be:
- Germany
- USA
- Italy 
- Myanmar
- Kazakhstan

Our data will be injected with two main methods:
- free APIs with dlt
- Web-scraping + RSS feeds with beautiful soup


We expect our schema, after processing to look like:
|source|
|country_target|
|title|
|summary|
|url|
|published_at|
|extracted_at|


The potential volume of our data: Over a 6-week project period approximately 126,000–294,000 records. Each

record is approximately 2–5 KB of text, resulting in a projected warehouse size of ~300 MB–1.5 GB of raw text data, 

with additional storage for embedding vectors.