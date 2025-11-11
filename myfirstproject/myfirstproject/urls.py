"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

def hello_world(request):
    from django.http import HttpResponse
    return HttpResponse('''
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Bootstrap Demo</title>
         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
     </head>
     <body>
         <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
             <div class="container">
                 <a class="navbar-brand" href="#">MyWebsite</a>
                 <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                     <span class="navbar-toggler-icon"></span>
                 </button>
                 <div class="collapse navbar-collapse" id="navbarNav">
                     <ul class="navbar-nav ms-auto">
                         <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
                         <li class="nav-item"><a class="nav-link" href="#">About</a></li>
                         <li class="nav-item"><a class="nav-link" href="#">Services</a></li>
                         <li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
                     </ul>
                 </div>
             </div>
         </nav>
         <div class="container mt-5">
             <div class="jumbotron bg-light p-5 rounded">
                 <h1 class="display-4">Welcome to Our Website!</h1>
                 <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content.</p>
                 <hr class="my-4">
                 <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
                 <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
             </div>

             <div class="row mt-5">
                 <div class="col-md-4">
                     <div class="card">
                         <div class="card-body">
                             <h5 class="card-title">Feature One</h5>
                             <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                             <a href="#" class="btn btn-outline-primary">Learn More</a>
                         </div>
                     </div>
                 </div>
                 <div class="col-md-4">
                     <div class="card">
                         <div class="card-body">
                             <h5 class="card-title">Feature Two</h5>
                             <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                             <a href="#" class="btn btn-outline-primary">Learn More</a>
                         </div>
                     </div>
                 </div>
                 <div class="col-md-4">
                     <div class="card">
                         <div class="card-body">
                             <h5 class="card-title">Feature Three</h5>
                             <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                             <a href="#" class="btn btn-outline-primary">Learn More</a>
                         </div>
                     </div>
                 </div>
             </div>
         </div>

         <footer class="bg-dark text-white text-center py-3 mt-5">
             <div class="container">
                 <p>&copy; 2024 MyWebsite. All rights reserved.</p>
             </div>
         </footer>

         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
     </body>
     </html>
                        ''')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='hello_world'),
]
