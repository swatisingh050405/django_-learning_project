from django.shortcuts import render 
from django.http import HttpResponse



posts = [
        {
            "title": "Getting Started with Django",
            "author": "Swati Singh",
            "date": "May 2026",
            "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4",
            "content": "Django is a powerful Python framework used for building secure and scalable web applications. It follows the MVT architecture and helps developers create projects quickly."
        },

        {
            "title": "Future of Artificial Intelligence",
            "author": "Rahul Sharma",
            "date": "May 2026",
            "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
            "content": "Artificial Intelligence is transforming industries like healthcare, education, finance and cybersecurity. AI tools are becoming an important part of everyday life."
        },

        {
            "title": "Tips for Student Developers",
            "author": "Ananya Verma",
            "date": "May 2026",
            "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
            "content": "Student developers should focus on consistency, project building and improving problem-solving skills. Learning by creating projects is the best way to grow."
        }
    ]

context = {
        "posts": posts
    }


def home(request):
    return render(request , 'blog/home.html' , context)


def about(request):
    return render(request , 'blog/about.html')


