from django.shortcuts import render

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

def sort_iterable(iterable, criteria):
    return sorted(iterable, key=lambda item: item.get(criteria))

def peopleall(request):
    sorted_list = sort_iterable(people, 'age')
    output = ['']
    for p in sorted_list:
        for i,v in p.items():
            output.append(i + ': ' + str(v))
        output.append('')            
    return render(request, 'people.html', {'info':output})

def peopleid(request, pid):
    for dict in people:
        output = []
        if dict['id'] == int(pid):
            for i,v in dict.items():
                output.append(i + ': ' + str(v))
            break
    return render(request, 'peopleid.html', {'info':output})
