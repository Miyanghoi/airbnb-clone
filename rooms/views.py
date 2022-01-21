# from datetime import datetime
from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

# from django.http import HttpResponse
from . import models


def all_rooms(request):
    #   now = datetime.now()
    #   return HttpResponse(content=f"<h1>{now}</h1>")

    # 아래와 같이 print로 뿌려가면서 확인하는 것 완전 유용함
    # print(dir(request.GET.get()))
    # print(request.GET.get())

    # page = request.GET.get("page", 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # page_count = ceil(models.Room.objects.count() / page_size)

    # all_rooms = models.Room.objects.all()[
    #     offset:limit
    # ]  # 첫번쨰는 제한, 두번째는 오프셋 (Limit, offset)

    # return render(
    #     request,
    #     "rooms/all_rooms.html",
    #     context={
    #         "rooms": all_rooms,
    #         "page": page,
    #         "page_count": page_count,
    #         "page_range": range(1, page_count),
    #     },
    # )

    page = request.GET.get("page", 1)
    # 쿼리셋을 만들면 그 쿼리셋이 바로 DB에 붙어서 데이터를 불러오는 게 아니라
    # 그 쿼리셋을 담은 변수를 불러올 떄 DB에 붙어서 전부 끌어온다.
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    # rooms = paginator.get_page(page)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/all_rooms.html", {"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
