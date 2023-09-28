// verifica se o jquery esta pronto para uso
$(document).ready(function(){
    var baseUrl = 'http://127.0.0.1:8000/'

    // pega o local do botao com a class .delete-btn
    var deleteBtn = $('.delete-btn');

    // botao de busca
    var searchBtn = $('.search-btn');
    var searchForm = $('.search-form');

    // botao de filtro
    var filter = $('#filter');

    $(deleteBtn).on('click', function(e){
        // pausa o evento (no caso o click do botao)
        e.preventDefault()

        // esta vendo o botao que o usuario clicou
        var delLink = $(this).attr('href');
        // pega o valor caso o usuario clique em 'sim';
        var result = confirm('Quer deletar esta tarefa?');
        if(result){
            // continua o processo de delete
            window.location.href = delLink;
        }
        // caso seleciona a opçao 'não', nao acontece nada
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    })

    $(filter).change(function(){
        var filter = $(this).val();
        console.log(filter)
        window.location.href = baseUrl+'?filter='+filter
    })

});