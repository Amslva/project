from django.shortcuts import render


def analyze(request):
    #test
    context = {
        'title': 'Аналитика IT-рынка',
        'languages_labels': ['Python', 'JavaScript', 'Java', 'C#', 'PHP'],
        'languages_data': [25, 22, 18, 12, 8],

        'backend_labels': ['Django', 'Spring', 'ASP.NET', 'Express.js', 'Flask'],
        'backend_data': [22, 18, 15, 14, 10],

        'frontend_labels': ['React', 'Vue.js', 'Angular', 'Svelte'],
        'frontend_data': [45, 25, 15, 5],

        'tech_labels': ['SQL', 'Docker', 'Git', 'AWS', 'Linux'],
        'tech_data': [85, 78, 75, 65, 50],

        'geo_labels': ['Москва', 'СПб', 'Новосибирск', 'Удаленно', 'Другие'],
        'geo_data': [40, 25, 8, 11, 16],

        'employment_labels': ['Удаленно', 'Офис', 'Гибрид'],
        'employment_data': [35, 30, 35],

        'salary_labels': ['Junior', 'Middle', 'Senior'],
        'salary_min': [60, 120, 200],
        'salary_avg': [80, 150, 250],
        'salary_max': [100, 180, 300],

        'vacancies_labels': ['Backend', 'Frontend', 'DevOps', 'Data'],
        'vacancies_data': [175, 155, 95, 85],
    }
    return render(request, 'analytics/analyze.html', context)