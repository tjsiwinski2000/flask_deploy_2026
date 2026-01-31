"# flask_deploy_2026" 
**0127-2026**
[from gemini how to display results from zip code search]
2. How to display the results? (UI Components)
Based on your current site's aesthetic, here are three ways to code the display:

Method 1: Bootstrap Cards (Recommended)
Since you are already using a grid layout (the three columns at the bottom), Cards are the best way to show coffee shops. They look great on mobile and desktop.

What to include in each card:

Title: Shop Name

Body: Address and distance from the postal code.

Footer: A "View on Maps" button.

HTML
<div class="row">
    {% for shop in coffee_shops %}
    <div class="col-md-4 mb-4">
        <div class="card h-100 shadow-sm">
            <img src="{{ shop.image_url }}" class="card-img-top" alt="Shop Image">
            <div class="card-body">
                <h5 class="card-title">{{ shop.name }}</h5>
                <p class="card-text text-muted">{{ shop.address }}</p>
                <span class="badge bg-success">Open Now</span>
            </div>
            <div class="card-footer bg-transparent border-top-0">
                <a href="#" class="btn btn-outline-primary btn-sm">View Details</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
**0126-2026**
from flask import Flask, render_template, request
#request for flask must be imported from flask
zip = request.form.get('zip')
#request.form.get['zip'] is incorrect; method needs ( ) 
**0123-2026**
copied working flask app to a temp directory
zipped working flask app
uploaded to my pythonanywhere account 
unzipped via bash console
cp -r * to /mysite directory 
->alternatively configure tjsiwinski2000_pythonanywhere_com_wsgi.py point to new directory




**GIT NOTES**
Create repo on github.com

from your local computer cmd-line
- notes below avoid ~~master~~ versus main drama that can take you for a ride.<br>
- **main** is default since 2020<br>
echo "# flask_deploy_2026" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/tjsiwinski2000/flask_deploy_2026.git  
git push -u origin main  
