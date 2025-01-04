import re


class RouteExtractor:


    # Define patterns for common dynamic segments, you can add here any supported estimations.
    patterns = [
        (r"/\d+", "/:id"),                  # Replace numeric IDs with :id
        (r"/[a-f0-9\-]{36}", "/:uuid"),     # Replace UUIDs with :uuid
        (r"/\d{4}-\d{2}-\d{2}", "/:date")   # Replace Date (yyyy-mm-dd) with :date
    ]


    @staticmethod
    def extract_route(url: str) -> str:

        route = url
        for pattern, placeholder in RouteExtractor.patterns:
            if re.search(pattern, url):                         # first, check if there is a pattern matching
                route = re.sub(pattern, placeholder, url)     # if so, create a new string and break
                break

        return route
