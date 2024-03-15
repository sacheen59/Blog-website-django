from datetime import date
from django.shortcuts import render

dummy_posts = [
    {
        "slug": "hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Sachin",
        "date": date(2024,3,3),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero unde quisquam deleniti illo velit similique doloribus saepe deserunt et obcaecati!",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Sachin",
        "date": date(2023,10,11),
        "title": "Programming",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero unde quisquam deleniti illo velit similique doloribus saepe deserunt et obcaecati!",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Sachin",
        "date": date(2024,2,1),
        "title": "Nature at the best",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero unde quisquam deleniti illo velit similique doloribus saepe deserunt et obcaecati!",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem dolorem blanditiis dolorum numquam quasi quos, ducimus ab quo enim magni iusto eius deleniti. Aliquid vel molestiae nisi consectetur odio saepe rerum blanditiis, praesentium, necessitatibus minima, et vitae eius architecto eum?
        """
    },
]

# helper function
def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_post = sorted(dummy_posts,key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_post
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": dummy_posts
    })

def post_detail(request,slug):
    identified_post = next(post for post in dummy_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        'post': identified_post
    })

