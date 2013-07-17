


    function changeGroup(group_id,wall_id)
    {
        $.get('/institute/wallgroup/'+group_id+'/'+wall_id);
    }

    $("document").ready(function(){
        $(".icon-trash").hide()
        $(".wallGroups").hide()
    });
        $(".form-inline").hover(function(){
            $(this).find(".icon-trash").show()
            $(this).find(".wallGroups").show()
            $(".form-inline").mouseleave(function(){
                $(".icon-trash").hide()
                $(".wallGroups").hide()
            })
           });

    $(".logo").hover(function(){
            $(this).find("#editImage").show()
            $(".logo").mouseleave(function(){
                $(this).find("#editImage").hide()
            })

           });

