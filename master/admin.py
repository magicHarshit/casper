# def getnotification(request):
#     result  = {}
#     """
#     @return : count of notification which are available to the requested user
#     @rtype:  HttpResponse object
#     """
#     result['type'] = "-ERR"
#     result['code'] = "401"
#     try:
#         notificationcount = Notifications.objects.filter(id=request.session.get('id')).count()
#     except ObjectDoesNotExist:
#         result = json.dumps(result)
#         return HttpResponse(result)
#     result['type'] = '+OK'
#     result['code'] = '200'
#     result['notificationcount'] = notificationcount
#     result = json.dumps(result)
#     return HttpResponse(result)
#
#
#
# <script type="text/javascript">
# 				$("#button").click(function() {   //button is the id of tha button
#
#
#
# $.ajax({
# url : "get-notifications",                         //get-notifications is url of server side code
# success : function(result) {
# var result = JSON.parse(result);                   //result  is the response \
#                                                     if u are sending dictionary or list you have to
#                                                      apply logic on result using loop,condiions
#
# $("#notification-div").append(result);               // this will append result into notification-div
#                                                        you can use other method than append()  as per ur
#                                                        requirement
# }});
#
#                 });
# </script>