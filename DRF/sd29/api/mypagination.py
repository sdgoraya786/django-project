from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 4
    ordering = 'name'