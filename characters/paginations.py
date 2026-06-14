import math

from rest_framework import pagination
from rest_framework.response import Response


class CharactersListPagination(pagination.PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        page_count = math.ceil(self.page.paginator.count / self.page.paginator.per_page)

        return Response(
            {
                "count": self.page.paginator.count,
                "page_count": page_count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )
