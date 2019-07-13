from django.utils.deprecation import MiddlewareMixin
import re
from django.http import HttpResponse


# class MD1(MiddlewareMixin):
#     # process_request按照注册顺序  顺序执行
#     def process_request(self, request):
#         print('MD1里的process_request')
#         print(request)
#
#     # def process_view(self, request, callback):
#     #     pass
#     #
#     # process_response是按照注册顺序倒序执行
#     def process_response(self, request, response):
#         print('MD1里的process_response')
#         return response
#
#     # process_views按照注册顺序 顺序执行
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         # view_func即将使用的视图函数
#         # view_args即将传递给试图的参数列表
#         # view_kwargs即将传递给视图的关键字参数字典
#         print('*' * 80)
#         print('MD1中的process_view')
#         print(view_func, view_func.__name__)
#
#     # process_exception按照注册顺序 倒序执行
#     def process_exception(self, request, exception):
#         print(exception)
#         print('MD1中的process_exception')
#
#     # process_templates_response按照注册顺序 倒序执行
#     def process_template_response(self, request, response):
#         print('MD1中的process_template_response')
#         return response


# class MD2(MiddlewareMixin):
#     def process_request(self, request):
#         print('MD2里的process_request')
#         print(request)
#
#     def process_response(self, request, response):
#         print('MD2里的process_response')
#         return response
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         # view_func即将使用的视图函数
#         # view_args即将传递给试图的参数列表
#         # view_kwargs即将传递给视图的关键字参数字典
#         print('#' * 80)
#         print('MD2中的process_view')
#         print(view_func, view_func.__name__)
#
#     def process_exception(self, request, exception):
#         print(exception)
#         print('MD2中的process_exception')
#
#     def process_template_response(self, request, response):
#         print('MD2中的process_template_response')
#         return response


class VisitedLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_addr = request.META['REMOTE_ADDR']
        # 判断当前访问的路由是否包含/demo/show 如果不包含，退出中间件函数
        if not re.match('/demo/show', request.path_info):
            return
        # 如果包含/demo/show  统计当前IP访问的次数，
        times = self.visit_times.get(ip_addr, 0)
        # 将访问次数加一，
        self.visit_times[ip_addr] = times + 1
        # 如果次数小于5，可以继续访问，退出中间件函数，
        if times < 5:
            return
        # 如果次数大于5，返回一个HttpResponse对象
        return HttpResponse('您已经访问' + str(times) + '次，您被拉黑了')
