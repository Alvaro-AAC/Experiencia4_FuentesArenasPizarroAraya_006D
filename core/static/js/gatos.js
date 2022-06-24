function getImagenGato()
{
    $.get("https://api.thecatapi.com/v1/images/search", function(data){
        $.each(data, function(i, item){
        $("#catImage").attr("src", item.url)
        });
    });
}

function getCatBreed()
{
    var cont=0;
    $.get("https://api.thecatapi.com/v1/breeds", function(data){
        $.each(data, function(i, item){
            $("#catBreed").append("<option value='"+cont+++"'>"+item.name+"</option>")
        });
    });
}
