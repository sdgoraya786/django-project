function getchildcat(pcat_id) {
    alert(pcat_id)
    let $ = django.jQuery;
    $.get('/app_child_category/' + pcat_id, function (resp){
        alert(resp)
        let child_cat_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           child_cat_list += '<option value="'+ item.id +'">'+ item.child_cat +'</option>'
        });
        $('#id_child_category').html(child_cat_list);
    });
}