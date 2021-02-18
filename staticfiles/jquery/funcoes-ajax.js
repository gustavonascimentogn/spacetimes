function mudar_estado(elemento) {
    console.log(elemento);
    var display = elemento.style.display;
    if(display == "none")
        elemento.style.display = 'block';
    else
        elemento.style.display = 'none';
}

function get_task_status(id_task){
    console.log(id_task);
    var elemento = document.getElementById("img"+id_task);
    console.log(elemento);
    mudar_estado(elemento);
    //token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    //console.log(token);
    $.ajax({
        type: 'POST',
        url: '/arquivos/get_task_status/'+id_task,
        data: {},
        success: function(result){
            console.log(result.status);
            $("#status"+id_task).text(result.status);
            $("#status2"+id_task).text('Status atualizado a cada 5s');
            // Executa novamente a chamada ajax enquanto status == 'STARTED'
            // Se diferente de STARTED significa que o processo já foi finalizado
            //if (result.status == 'STARTED') {
                setTimeout(function(){
                    get_task_status(id_task); //this will send request again and again;
                }, 5000);
            //}
            if (result.status == 'SUCCESS') {
               location.reload();
            }

        }
    });

}