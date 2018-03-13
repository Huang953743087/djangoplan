from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator

class OrgView(View):
    def get(self, request):
        # 获取所有城市
        all_citys = CityDict.objects.all()
        # 获取所有机构
        all_orgs = CourseOrg.objects.all()
        # 统计机构数量
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 从all——org中每页取5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        render(request, 'org-list.html', {
            'all_citys': all_citys,
            'all_orgs': orgs,
            'org_nums': org_nums,
        })
