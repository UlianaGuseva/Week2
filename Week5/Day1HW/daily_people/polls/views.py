from django.shortcuts import render

# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people_info(request, id): 
    context = people[id-1]
    return render(request, 'index.html', context)

def people_all(request): 
    to_sort_people = people
    sorted_people = []
    ages = []
    for i in to_sort_people:
        ages.append(i['age'])
    ages.sort() 
    for n in ages:
        for c in to_sort_people:
            if c['age'] == n:
                # to_sort_people.remove(c)
                sorted_people.append(c)
    context = {'people': sorted_people}
    # for i in range(1, len(people)+1):
    #     context[i] = people[i-1]['name'] + people[i-1]['age'] + people[i-1]['country']
    #     return context
    return render(request, 'all_people.html', context)