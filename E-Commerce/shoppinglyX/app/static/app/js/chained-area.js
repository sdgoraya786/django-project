function get_child_category(parent_category_id) {
    let $ = django.jQuery;
    $.get('/app/ChildCategory/' + parent_category_id, function (resp){
        let child_category_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           child_category_list += '<option value="'+ item.id +'">'+ item.child_cat +'</option>'
        });
        $('#id_child_category').html(child_category_list);
    });
}