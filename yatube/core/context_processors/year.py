from django.utils import timezone


def year(request) -> int:
    '''Добавляет переменную с текущим годом.'''
    return {
        'year': timezone.now().year
    }
