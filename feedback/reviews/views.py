from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .models import Review
from .forms import ReviewForm

# Create your views here.

class ReviewView(FormView): #jako jedyny(chyba) view nie wie co zrobić z pozyskanymi danymi i trzeba mu wskazać
    form_class = ReviewForm
    template_name = "reviews/review.html" # te dwie linijki zastępują get i post
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

#class ReviewView(CreateView): #nie trzeba uzywac ModelForm wtedy, co takiego jak FormView
    #model = Review
   # form_class = ReviewForm
    #template_name = "reviews/review.html" 
   # success_url = "/thank-you"

   # def form_valid(self, form):
        #form.save()
       #S return super().form_valid(form)




#class ReviewView(View):
   # def get(self,request):
      #form = ReviewForm()
      #return render(request, "reviews/review.html", {
        #"form": form
       # })

      
   # def post(self,request):
        #form = ReviewForm(request.POST)

       # if form.is_valid():
           # form.save()
           # return HttpResponseRedirect("/thank-you")

       # return render(request, "reviews/review.html", {
          #  "form": form
       # })

class ThankYouView(TemplateView):
   template_name = "reviews/thank_you.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["message"] = 'This works!'
      return context
   
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model=Review
    context_object_name="reviews" #nadanie swojej nazwy dla wygody, bo jeśli tego nie będzie to trzeba iterowac po object_list

    # jeśli chcesz uzyskać konkretne danye pod warunkami
    # #def get_queryset(self):
      #  base_query =  super().get_queryset()
       # data = base_query.filter(rating__gt=4)
       # return data

#class ReviewsListView(TemplateView):
   #template_name = "reviews/review_list.html"

  # def get_context_data(self, **kwargs):
      #context = super().get_context_data(**kwargs)
      #reviews = Review.objects.all()
      #context["reviews"] = reviews
      #return context

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review #django automatyczznie przekazuje nazwę modelu do htmla małymi literami, dlatego nic nie trzeba zmieniać

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get["favourite_review"]
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context

class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)






   
#class SingleReviewView(TemplateView):
    #template_name = "reviews/single_review.html"

    #def get_context_data(self, **kwargs):
       # context = super().get_context_data(**kwargs)
        #review_id = kwargs["id"]
        #selected_review = Review.objects.get(pk=review_id)
       # context["review"] = selected_review
        #return context
