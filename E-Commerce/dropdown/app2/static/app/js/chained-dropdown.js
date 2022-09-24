// City
$("#id_parent_category").change(function () { 
    var url = $("#productForm").attr("data-child-cat-url"); 
    var parent_category_id = $(this).val(); 
    alert(parent_category_id)
    $.ajax({ 
        url: "{% url 'load_child_cat' %}",
        data: {
            'parent_category': parent_category_id 
        },
        success: function (data) { 
            $("#id_child_category").html(data);
            console.log(data); 
        }
    });
});