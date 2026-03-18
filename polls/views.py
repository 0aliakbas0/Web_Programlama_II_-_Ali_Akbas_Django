from django.db import models
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    """
    Handles the display of the main index page, listing active questions.
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Retrieves the standard queryset for the index view, with optional search filtering.
        
        Returns:
            QuerySet: The filtered and ordered questions, excluding future ones.
        """
        query = self.request.GET.get("q")
        queryset = Question.objects.filter(pub_date__lte=timezone.now())
        if query:
            queryset = queryset.filter(question_text__icontains=query)
        return queryset.order_by("-pub_date")[:5]

    def get_context_data(self, **kwargs):
        """
        Injects system-wide statistics into the index context.
        """
        context = super().get_context_data(**kwargs)
        all_questions = Question.objects.filter(pub_date__lte=timezone.now())
        
        total_votes = sum(choice.votes for q in all_questions for choice in q.choice_set.all())
        completed_polls = sum(1 for q in all_questions if q.choice_set.aggregate(models.Sum('votes'))['votes__sum'] or 0 > 0)
        
        context['total_votes_all'] = total_votes
        context['completed_polls_count'] = completed_polls
        context['search_query'] = self.request.GET.get("q", "")
        return context


class DetailView(generic.DetailView):
    """
    Handles the display of a specific question's voting form.
    """
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Restrict the queryset to exclude unpublished (future) questions.
        
        Returns:
            QuerySet: Questions published up to the current timestamp.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """
    Handles the visualization of voting results for a specific question.
    """
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        """
        Injects additional context, including percentage calculations for choices.
        
        Args:
            **kwargs: Dictionary of keyword arguments to pass to the view.
            
        Returns:
            dict: The context dictionary containing 'sorted_choices' and 'total_votes'.
        """
        context = super().get_context_data(**kwargs)
        question = context['question']
        choices = question.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        
        sorted_choices = []
        for choice in choices:
            percentage = (choice.votes / total_votes * 100) if total_votes > 0 else 0
            choice.percentage = percentage
            sorted_choices.append(choice)
            
        sorted_choices.sort(key=lambda x: x.votes, reverse=True)
        
        context['sorted_choices'] = sorted_choices
        context['total_votes'] = total_votes
        return context


def vote(request, question_id):
    """
    Processes the voting submission for a given question.
    
    Args:
        request (HttpRequest): The incoming HTTP request payload.
        question_id (int): The primary key of the question being voted on.
        
    Returns:
        HttpResponseRedirect: Redirects into the Results view on successful vote.
        HttpResponse: Renders the detail view with an error message on failure.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form due to missing choice parameter.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Atomic increment to prevent race conditions during high concurrency.
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after processing POST data.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
