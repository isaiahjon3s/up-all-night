import requests
from bs4 import BeautifulSoup
import random

def get_random_college():
    """
    Scrapes college names from a Wikipedia page and returns a random one.
    """
    try:
        # Use Wikipedia's list of colleges as a reliable source
        url = "https://en.wikipedia.org/wiki/List_of_colleges_and_universities_in_the_United_States"
        
        # Set a user agent to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links that are likely to be college names
        # Look for links in the main content area
        college_links = []
        
        # Find all links that contain "University" or "College" in their text
        for link in soup.find_all('a', href=True):
            link_text = link.get_text().strip()
            if link_text and ('University' in link_text or 'College' in link_text):
                # Filter out obviously non-college links
                if (not link_text.startswith('Category:') and 
                    not link_text.startswith('List of') and
                    not link_text.startswith('Template:') and
                    len(link_text) > 10 and  # Avoid very short names
                    len(link_text) < 100):   # Avoid very long descriptions
                    college_links.append(link_text)
        
        # Remove duplicates while preserving order
        unique_colleges = list(dict.fromkeys(college_links))
        
        if unique_colleges:
            return random.choice(unique_colleges)
        else:
            # Fallback list in case scraping fails
            fallback_colleges = [
                "Harvard University",
                "Stanford University", 
                "Massachusetts Institute of Technology",
                "University of California, Berkeley",
                "Yale University",
                "Princeton University",
                "University of Chicago",
                "Columbia University",
                "University of Pennsylvania",
                "California Institute of Technology"
            ]
            return random.choice(fallback_colleges)
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        # Return a fallback college
        fallback_colleges = [
            "Harvard University",
            "Stanford University", 
            "Massachusetts Institute of Technology",
            "University of California, Berkeley",
            "Yale University"
        ]
        return random.choice(fallback_colleges)
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Harvard University"  # Ultimate fallback

def main():
    college = get_random_college()
    print(f"🎓 Your random college is: {college}")
    return college

if __name__ == "__main__":
    main()