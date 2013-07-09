function onhover_courses(){
    $('#id_course_drp').addClass('open');
}

function onclick_change(element){
    $(element).parent().attr('class','active');

}

function onblur_courses(){
    $('#id_course_drp').attr('class','dropdown')
}

function show_programs(pref)
{
    $('#id_qual_list').hide();
    $('#id_qual_'+pref).slideDown();
}



function hide_programs(pref)
{

    $('#id_qual_'+pref).hide();
    $('#id_qual_list').slideDown();
}

function scroll_left(key)
{
    key = parseInt(key);
    if (key == 4)
        n_key = 1;
    else
        n_key = parseInt(key)+1;
    $('#scroll_'+key).hide()
    $('#scroll_'+n_key).show()
}

function scroll_right(key)
{
    key = parseInt(key);
    if (key == 1)
        n_key = 4;
    else
        n_key = parseInt(key)-1;
    $('#scroll_'+key).hide()
    $('#scroll_'+n_key).show()
}
 
function changeclass(divid,len)
{
    
    looplen = parseInt(len)
    if ($('#'+divid).attr('class') == 'minus pull-right')
    {
        for (i=1;i<=looplen;i++)
        {
            $('#span_'+i).removeClass('plus pull-right').addClass('minus pull-right');
        }
        $('#'+divid).removeClass('minus pull-right').addClass('plus pull-right');
    }
    else
    {
        for (i=1;i<=looplen;i++)
        {
            $('#span_'+i).removeClass('minus pull-right').addClass('plus pull-right');
        }
        $('#'+divid).removeClass('plus pull-right').addClass('minus pull-right');
    }
}

function getcbval()
{
    if ($('#id_checkbox').val()== '0')
        $('#id_checkbox').val('1');
    else
        $('#id_checkbox').val('0');
}


function ShowPayDiv()
{
    $('#id_order').hide();
    $('#id_payment').show();
}

function ShowOrderDiv()
{
    $('#id_order').show();
    $('#id_payment').hide();
}
function ValidateChqDetail()
{
    var status = true;
    chq_no = $('#id_cheque_no').val();
    bank = $('#id_bank').val()
    if (chq_no == '')
    {
        $('#id_error_cheque_no').show();
        $('#li_cheque_no').addClass('error');
        status = false;
    }
    if (bank == '')
    {
        $('#id_error_bank').show();
        $('#li_bank').addClass('error');
        status = false;
    }
    return status;
}


function SubmitNL(contact_type)
{
    var div_id = 'id_newsletter_div';
    var name = $('#id_name');
    var email = $('#id_email');
    var type = $('#id_type');
    var data = {'name':name.val(),'email':email.val(),'type':type.val()};
    var all_fields = ['name','email','type'];
    jQuery.ajax({
        url: '/feedback/'+contact_type+'/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            ShowNLrrorThickBox(res,div_id,all_fields);
        }
    });
}


function ShowNLrrorThickBox(res, div_id, all_fields){
    var check = res.split('-');
    if( check[0] == 'error')
    {
        var fields = check[1].split('|');
        for (var i=0; i<fields.length;i++)
        {
            var error = fields[i].split(':');
            $('#id_'+error[0]).attr('class','error');
            all_fields = removeByValue(all_fields,error[0]);
        }
        for (var j=0;j<all_fields.length;j++){
            $('#id_'+all_fields[j]).attr('class','text');
        }
    }
    else if(check[0] == 'success')
    {   
        
        var html_cont = '<div class="div_cointainer_login"><div class="close"><a href="javascript:void(0);" onclick="tb_remove();"></a></div><div class="register"><strong>Thank you</strong>'+check[1]+'</div><div class="clear"></div></div>';
        $('#'+div_id).html(html_cont);
        tb_show('','#TB_inline?height=505&width=505&inlineId='+div_id,'');
        setTimeout("tb_remove()", 3000);

    }
}

function SubmitNoResult(contact_type)
{
    var div_id = 'id_thankyou_div';
    var name = $('#id_name');
    var email = $('#id_email');
    var type = $('#id_type');
    var message = $('#id_message');
    var data = {'name':name.val(),'email':email.val(),'type':type.val(),'message':message.val()};
    var all_fields = ['name','email','type','message'];
    jQuery.ajax({
        url: '/feedback/'+contact_type+'/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            ShowNOResulterrorThickBox(res,div_id,all_fields);
        }
    });
}


function ShowNOResulterrorThickBox(res, div_id, all_fields){
    var check = res.split('-');
    if( check[0] == 'error')
    {
        var fields = check[1].split('|');
        for (var i=0; i<fields.length;i++)
        {
            var error = fields[i].split(':');
            $('#id_'+error[0]).parent().attr('class','error');
            $('fieldset #id_'+error[0]).parent().append('<div id="'+'id_error_'+error[0]+'"  class='+"crossing"+'></div>');
            $('fieldset #id_'+error[0]).attr('onfocus','remove_error_class_from_li("'+error[0]+'");');
            all_fields = removeByValue(all_fields,error[0]);
        }
        for (var j=0;j<all_fields.length;j++){
            $('#id_'+all_fields[j]).attr('class','text');
        }
    }
    else if(check[0] == 'success')
    {

        var html_cont = '<div class="div_cointainer_login"><div class="close"><a href="javascript:void(0);" onclick="tb_remove();"></a></div><div class="register"><strong>Thank you</strong>'+check[1]+'</div><div class="clear"></div></div>';
        $('#'+div_id).html(html_cont);
        tb_show('','#TB_inline?height=505&width=505&inlineId='+div_id,'');
        setTimeout("tb_remove();window.location=self.location;", 3000);

    }
}

function SubmitContact(contact_type)
{
    var div_id = 'id_contact_div';
    var name = $('fieldset #id_name');
    var email = $('fieldset #id_email');
    var type = $('fieldset #id_type');
    var contact_number = $('fieldset #id_contact_number');
    var message = $('fieldset #id_message');
    var data = {'name':name.val(),'email':email.val(),'contact_number':contact_number.val(),'message':message.val(),'type':type.val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()};
    var all_fields = ['name','email','contact_number','message','type'];
    jQuery.ajax({
        url: '/feedback/'+contact_type+'/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            ShowContacterrorThickBox(res,div_id,all_fields);
        }
    });
}


function ShowContacterrorThickBox(res, div_id, all_fields){
    var check = res.split('-');
    if( check[0] == 'error')
    {
        var fields = check[1].split('|');
        for (var i=0; i<fields.length;i++)
        {
            var error = fields[i].split(':');
            $('fieldset #id_em_'+error[0]).attr('class','error');
            $('fieldset #id_'+error[0]).attr('onfocus','remove_error_class_from_li("'+error[0]+'");');
            if($('fieldset #id_em_'+error[0]).children('em').length == 0){
                $('fieldset #id_em_'+error[0]).append('<em>This field is required</em>');
            }
            $('fieldset #id_error_'+error[0]).show();
            all_fields = removeByValue(all_fields,error[0]);
        }
//        for (var j=0;j<all_fields.length;j++){
//            $('fieldset #id_em_'+error[0]).attr('class','');
////            $('fieldset #id_error_'+error[0]).hide();
//        }
    }
    else if(check[0] == 'success')
    {   
        
        var html_cont = '<div class="div_cointainer_login"><div class="close"><a href="javascript:void(0);" onclick="tb_remove();"></a></div><div class="register"><strong>Thank you</strong>'+check[1]+'</div><div class="clear"></div></div>';
        $('#'+div_id).html(html_cont);
        tb_show('','#TB_inline?height=505&width=505&inlineId='+div_id,'');
        setTimeout("tb_remove()", 3000);

    }
}

function SubmitFeedback(contact_type){
    var div_id = 'id_feedback_div';
    var name = $('fieldset #id_name');
    var email = $('fieldset #id_email');
    var contact_number = $('fieldset #id_contact_number');
    var message = $('fieldset #id_message');
    var type = $('fieldset #id_type');
    var data = {'name':name.val(),'email':email.val(),'contact_number':contact_number.val(),'message':message.val(),'type':type.val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()};
    var all_fields = ['name','email','contact_number','message','type'];
    jQuery.ajax({
        url: '/feedback/'+contact_type+'/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            ShowFbErrorThickBox(res,div_id,all_fields);
        }
    });
}

function Feedback_msg(msg_id,contact_type,div_id){
    var msg = $('#'+msg_id).val();
    var data = {'message':msg,'type':contact_type};
    var all_fields = ['message','type'];
    jQuery.ajax({
        url: '/feedback/'+contact_type+'/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            ShowFbErrorThickBox(res,div_id,all_fields);
        }
    });
}


function ShowFbErrorThickBox(res, div_id, all_fields){
    var check = res.split('-');
    if( check[0] == 'error')
    {
        var fields = check[1].split('|');
        for (var i=0; i<fields.length;i++)
        {
            var error = fields[i].split(':');
            $('fieldset #id_em_'+error[0]).attr('class','error');
            $('fieldset #id_error_'+error[0]).show();
            if($('fieldset #id_em_'+error[0]).children('em').length == 0){
                $('fieldset #id_em_'+error[0]).append('<em style="padding:0 0 0 100px; color:RED;">this field is required</em>');
            }
            $('fieldset #id_'+error[0]).attr('onfocus','remove_error_class("'+error[0]+'");');
            all_fields = removeByValue(all_fields,error[0]);
        }
        for (var j=0;j<all_fields.length;j++){
            $('#id_em_'+all_fields[j]).attr('class','');
//            $('#id_error_'+error[j]).hide();
        }
    }
    else if(check[0] == 'success')
    {
        var html_cont = '<div class="div_cointainer_login"><div class="close"><a href="javascript:void(0);" onclick="tb_remove();"></a></div><div class="register"><strong>Thank you</strong>'+check[1]+'</div><div class="clear"></div></div>';
        $('#'+div_id).html(html_cont);
        setTimeout("tb_remove()", 3000);

    }
}

function remove_error_class(field_name){
    var field = $('#id_em_'+field_name);
    field.children('em').remove();
    $('fieldset #id_em_'+field_name);
    $('#id_error_'+field_name).hide();
    field.attr('class','');
}

function remove_error_class_from_li(field_name){
    var field = $('fieldset #id_'+field_name);
    field.parent().children('em').remove();
    $('fieldset #id_error_'+field_name).hide();
    field.parent().attr('class','');
    $('#id_error_'+field_name).remove();
}

function ShowHideLabel(defaultval,obj,type)
{
    if(type == 'hide')
    {
        if (obj.value == defaultval)
        {
            obj.value = '';
        }
    }
    else
    {
        if (obj.value == '')
        {
            obj.value = defaultval;
        }
    }
    
    
}


function save_cropped_image(input_id){
    var iframe = $('<iframe name="proxyframe" id="proxyframe" style="display: none" />');
    $("body").append(iframe);
    var form = $('<form id="proxy_upload_form"></form>');
    $("body").append(form);
    form.attr("action", "/institute/ajax-save-image/");
    form.attr("method", "post");
    form.attr("enctype", "multipart/form-data");
    form.attr("encoding", "multipart/form-data");
    form.attr("target", "proxyframe");
    var input_file = $(input_id);
    var input_params = $('<input type="hidden" value="{}" name="crop_dictionary" id="id_cropdict">');
    input_params.attr('value',$("#id_cropdict").val());
    var type = $('<input type="hidden" value="" name="file_type" id="id_type">');
    type.attr('value',$(input_id).attr('name'));
    var appldetail = $('<input type="hidden" value="" name="appldetail" id="id_appldetail">');
    var csrf_token = $('<input type="hidden" value="" name="csrfmiddlewaretoken">');
    csrf_token.attr('value',$('input[name=csrfmiddlewaretoken]').val());
    appldetail.attr('value',$('#id_application_detail').val());
    form.append(input_file);
    form.append(input_params);
    form.append(type);
    form.append(appldetail);
    form.append(csrf_token);


    form.submit();
    $("#proxyframe").load(function () {
        var response = $($("#proxyframe")[0].contentWindow.document.body).text();
        if(response.indexOf('/')!=-1){
                    var image_div = $('<img width="150" height="150" alt="Signature" src="" id="id_image_'+type.val()+'">');
                    image_div.attr('src',response);
            if($('#div_cointainer_photo').children('img').length==0){
                    $('#div_cointainer_photo').append(image_div);
                $('#div_cointainer_photo').toggle();
            }
            else{

                $('#div_cointainer_photo').children('img').attr('src',response);
                $('#div_cointainer_photo').toggle();
            }
        }
        else{
            alert('error in uploading file. try later.')
        }

        $('#id_li_'+type.val()).append(input_file);
        $('body').remove("#proxy_upload_form");
        setTimeout("tb_remove()", 1000);
    });
    $('body').remove("#proxyframe");

}
