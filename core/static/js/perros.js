function getImagenPerro()
{
  $.get("https://dog.ceo/api/breeds/image/random", function(data) {
    $("#dogImage").attr("src", data.message)
  });
}

function getDogBreed()
{
    var cont=0;
    $.get("https://dog.ceo/api/breeds/list", function(data){
        $.each(data.message, function(i, item){
            $("#dogBreed").append("<option value='"+cont+++"'>"+item+"</option>")
        });
    });
}
