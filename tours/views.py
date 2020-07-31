from .data import title, description, departures, tours, subtitle
from django.views.generic import TemplateView
import random


def shuffle_dict(d_dict):
    keys = list(map(tuple, d_dict.items()))
    random.shuffle(keys)
    s_dict = dict(keys)
    return s_dict


def cut_dict(d_dict, count):
    for i in range(0, 16 - count):
        d_dict.popitem()
    c_dict = d_dict
    return c_dict


def search_tours(departure, d_data):
    s_data = {}
    for id, tour in d_data.items():
        if tour['departure'] == departure:
            s_data[id] = tour
    return s_data


def search_min_max(d_data, key_name):
    items_list = []
    for id, tour in d_data.items():
        items_list.append(tour[key_name])
    res = {'min': min(items_list), 'max': max(items_list)}
    return res


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['template_data'] = {
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'departures': departures.items(),
            'tours': cut_dict(shuffle_dict(tours), 6).items(),
        }
        return context


class DepartureView(TemplateView):
    template_name = 'departure.html'

    def get_context_data(self, departure, **kwargs):
        context = super(DepartureView, self).get_context_data(departure='msk', **kwargs)
        context['template_data'] = {
            'title': title,
            'departures': departures.items(),
            'tours': search_tours(departure, tours).items(),
            'num_tours': len(search_tours(departure, tours)),
            'price': search_min_max(search_tours(departure, tours), 'price'),
            'nights': search_min_max(search_tours(departure, tours), 'nights'),
            'departure': departures.get(departure),
            'dep_active': departure
        }
        return context


class TourView(TemplateView):
    template_name = 'tour.html'

    def get_context_data(self, id, **kwargs):
        context = super(TourView, self).get_context_data(id=1, **kwargs)
        context['template_data'] = {
            'title': title,
            'departures': departures.items(),
            'departure': departures.get(tours[id].get('departure')),
            'dep_active': tours[id].get('departure'),
            'tour': tours[id],
        }
        return context
