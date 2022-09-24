var script = document.createElement('script');
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js";
document.head.appendChild(script);

script.onload = function(){
    tinymce.init({
        "theme": "silver",
        "height": 500,
        "menubar": False,
        "plugins": [
            'advlist autolink lists link image charmap print preview anchor',
            'searchreplace visualblocks code fullscreen insertdatetime media table paste',
            'code help wordcount'
        ],
        "toolbar": [
            'undo redo | formatselect |',
            'bold italic backcolor | alignleft aligncenter ',
            'alignright alignjustify | bullist numlist outdent indent | ',
            'removeformat | help'
        ]
      });
}