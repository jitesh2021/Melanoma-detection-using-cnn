
    function showPreview(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("img_blood");
    preview.src = src;
    preview.style.display = "block";
  }
}

$(document).on('submit','#form',function(e)
                   {
      console.log('hello1');
      e.preventDefault();
      var file_data = $('#myImage').prop('files')[0];
       var form_data = new FormData();
       form_data.append('myImage', file_data);
       console.log('hello2');
      $.ajax({
        contentType: false,
        processData: false,
        type:'POST',
        url:'/pred',
        data:form_data,
        success:function(response)
        {
          response = JSON.parse(response);
          $('#res').html("<h2>Result</h2><h3><strong>Category : </strong>" + response['cat'] ); //+ "</h3><h3><strong>Accuracy : </strong>" +response['acc'] +"</h3>"
        }
      })
    });
  
// $(document).ready(function (e) {
//   $('#upload').on('click', function () {
//       var file_data = $('#myImage').prop('files')[0];
//       var form_data = new FormData();
//       form_data.append('myImage', file_data);
//       e.preventDefault();
//       $.ajax({
//           url: '/pred', // point to server-side controller method
//           dataType: 'text', // what to expect back from the server
//           cache: false,
//           contentType: false,
//           processData: false,
//           data: form_data,
//           type: 'post',
//           success: function (response) {
//                return
//           },
//           error: function (response) {
//                // display error response from the server
//                alert("res")
//           }
//       });
      
//   });
// });