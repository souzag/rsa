function getCrip() 
{
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var primeiro_item = document.getElementById("primeiro_item").value
    var segundo_item = document.getElementById("segundo_item").value
    var diretorio = document.getElementById("diretorio").value

    document.getElementById("primeiro_item").value = ""
    document.getElementById("segundo_item").value = ""
    document.getElementById("diretorio").value = ""
    

    var opcoes = 
    {
        scriptPath : path.join(),
        args : [primeiro_item , segundo_item , diretorio]
    }

    var key = new PythonShell('Criptografar/criptografar.py', opcoes);

    key.on('message', function(message) 
    {
        swal(message);
    })
}